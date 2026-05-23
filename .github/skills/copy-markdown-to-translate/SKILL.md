---
name: copy-markdown-to-translate
description: "Create or refresh a to-translate folder by copying every .md file from the repository into it while preserving relative paths and excluding the destination tree itself. USE FOR: preparing a translation staging area, rebuilding to-translate after docs change, mirroring markdown files for localization. DO NOT USE FOR: translating content, copying non-markdown assets, or syncing back from to-translate into source files."
argument-hint: "Optional destination folder name or scope constraints"
---

# Copy Markdown To Translate

Create or refresh a translation staging tree by copying every Markdown file in the repository into a destination folder, preserving the original relative structure and explicitly excluding the destination folder from the source scan.

## When to Use

- You need to create the initial `to-translate/` workspace for translation work.
- Markdown files changed in the repository and you need to rebuild the staging copy.
- You want a safe, repeatable workflow for mirroring only `.md` files without touching source files.

## When Not to Use

- You need to translate or rewrite the copied content.
- You need to copy binary files, images, JSON, or other non-Markdown assets.
- You need bidirectional sync between `to-translate/` and the source tree.
- You need to preserve files already edited inside `to-translate/`; this workflow overwrites staged copies.

## Pre-conditions

- Run from the repository root.
- The destination folder is intended to live at the repository root, normally `to-translate`.
- PowerShell is available in the terminal.
- You understand that existing copied `.md` files in the destination may be overwritten.

## Procedure

### 1. Confirm the destination

Default to `to-translate` at the repository root unless the user explicitly asks for a different destination.

### 2. Create or refresh the staging tree

Run this PowerShell command from the repository root:

```powershell
$root = Get-Location
$target = Join-Path $root 'to-translate'
New-Item -ItemType Directory -Force -Path $target | Out-Null
$files = Get-ChildItem -Path $root -Recurse -File -Filter *.md |
    Where-Object {
        $_.FullName -notlike "$target*" -and
        $_.FullName -notlike "*\.git\*"
    }
foreach ($file in $files) {
    $relative = $file.FullName.Substring($root.Path.Length + 1)
    $destination = Join-Path $target $relative
    $destinationDir = Split-Path -Parent $destination
    New-Item -ItemType Directory -Force -Path $destinationDir | Out-Null
    Copy-Item -LiteralPath $file.FullName -Destination $destination -Force
}
[pscustomobject]@{
    SourceCount = $files.Count
    CopiedCount = (Get-ChildItem -Path $target -Recurse -File -Filter *.md).Count
} | Format-List
```

### 3. Protect against recursive copying

The source scan must exclude the destination tree with:

```powershell
$_.FullName -notlike "$target*"
```

Do not remove that condition. Without it, subsequent runs can re-copy files already staged inside `to-translate/` and create nested duplication.

### 4. Preserve relative paths

The destination path must be built from the source file path relative to the repository root:

```powershell
$relative = $file.FullName.Substring($root.Path.Length + 1)
$destination = Join-Path $target $relative
```

Do not flatten the output. The workflow is only correct if a file like `docs/index.md` becomes `to-translate/docs/index.md`.

## Validation

Consider the workflow complete only when all checks pass:

- The folder `to-translate/` exists at the repository root.
- The destination contains the same number of `.md` files reported in `SourceCount`.
- A few spot checks confirm structure preservation, for example:
  `README.md -> to-translate/README.md`
  `docs/index.md -> to-translate/docs/index.md`
  `.github/skills/add-community-extension/SKILL.md -> to-translate/.github/skills/add-community-extension/SKILL.md`
- No copied file path includes `to-translate/to-translate/`.
- The source scan excluded the destination tree and `.git` paths.

If needed, validate with:

```powershell
Test-Path (Join-Path (Get-Location) 'to-translate')
Get-ChildItem -Path .\to-translate -Recurse -File -Filter *.md | Select-Object -First 10 FullName
Get-ChildItem -Path .\to-translate -Recurse -File -Filter *.md |
    Where-Object { $_.FullName -like '*to-translate\to-translate\*' }
```

The last command must return no results.

## Common Pitfalls

- Copying from inside `to-translate/` instead of from the repository root.
- Forgetting to exclude the destination directory from `Get-ChildItem` results.
- Flattening paths instead of preserving the original directory structure.
- Assuming this workflow translates files; it only stages copies.
- Re-running the workflow after manually editing staged files without acknowledging that copies may be overwritten.

## Example Prompts

- Create or refresh `to-translate` with every Markdown file from this repo.
- Rebuild the translation staging folder and preserve the source directory structure.
- Mirror all `.md` files into `to-translate` without copying the destination into itself.
- Prepare a fresh Markdown-only tree for translation review.
