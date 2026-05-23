---
name: copy-markdown-to-translate
description: "Rebuild the repository's to-translate folder by recreating it and copying every .md file into it while preserving relative paths and excluding the destination tree itself. USE FOR: preparing a translation staging area, rebuilding to-translate after docs change, mirroring markdown files for localization. DO NOT USE FOR: translating content, copying non-markdown assets, syncing back from to-translate into source files, or targeting a different destination folder."
argument-hint: "No arguments. This skill always rebuilds the repository root to-translate folder."
---

# Copy Markdown To Translate

Rebuild the repository's `to-translate/` staging tree by deleting any previous copy, recreating it, and copying every Markdown file in the repository into it while preserving the original relative structure and explicitly excluding the destination tree from the source scan.

## When to Use

- You need to create the initial `to-translate/` workspace for translation work.
- Markdown files changed in the repository and you need to rebuild the staging copy.
- You want a safe, repeatable workflow for mirroring only `.md` files without touching source files.

## When Not to Use

- You need to translate or rewrite the copied content.
- You need to copy binary files, images, JSON, or other non-Markdown assets.
- You need bidirectional sync between `to-translate/` and the source tree.
- You need to preserve files already edited inside `to-translate/`; this workflow removes and recreates the staging tree.
- You want to target a destination other than `to-translate/`.

## Pre-conditions

- Run from the repository root.
- The destination folder is always `to-translate/` at the repository root.
- PowerShell is available in the terminal.
- You understand that existing staged files inside `to-translate/` will be removed before copying.

## Procedure

### 1. Confirm the fixed destination

This skill always targets `to-translate/` at the repository root.

### 2. Recreate the staging tree

Run this PowerShell command from the repository root:

```powershell
$root = Get-Location
$target = Join-Path $root 'to-translate'
if (Test-Path -LiteralPath $target) {
    Remove-Item -LiteralPath $target -Recurse -Force
}
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

Deleting and recreating `to-translate/` is required here. That keeps the staging tree an exact mirror of the repository's current Markdown files and prevents orphaned `.md` files from surviving across rebuilds.

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
- The destination contains exactly the same number of `.md` files reported in `SourceCount`.
- A few spot checks confirm structure preservation, for example:
  `README.md -> to-translate/README.md`
  `docs/index.md -> to-translate/docs/index.md`
  `.github/skills/add-community-extension/SKILL.md -> to-translate/.github/skills/add-community-extension/SKILL.md`
- No copied file path includes `to-translate/to-translate/`.
- No stale `.md` files remain from previous runs because the destination was removed before copy.
- The source scan excluded the destination tree and `.git` paths.

If needed, validate with:

```powershell
Test-Path (Join-Path (Get-Location) 'to-translate')
Get-ChildItem -Path . -Recurse -File -Filter *.md |
    Where-Object {
        $_.FullName -notlike "$(Join-Path (Get-Location) 'to-translate')*" -and
        $_.FullName -notlike '*\.git\*'
    } |
    Measure-Object | Select-Object -ExpandProperty Count
Get-ChildItem -Path .\to-translate -Recurse -File -Filter *.md |
    Measure-Object | Select-Object -ExpandProperty Count
Get-ChildItem -Path .\to-translate -Recurse -File -Filter *.md | Select-Object -First 10 FullName
Get-ChildItem -Path .\to-translate -Recurse -File -Filter *.md |
    Where-Object { $_.FullName -like '*to-translate\to-translate\*' }
```

The first command must return `True`, the two count commands must match, and the last command must return no results.

## Common Pitfalls

- Copying from inside `to-translate/` instead of from the repository root.
- Forgetting to exclude the destination directory from `Get-ChildItem` results.
- Re-running the workflow expecting manual edits inside `to-translate/` to survive.
- Flattening paths instead of preserving the original directory structure.
- Assuming this workflow translates files; it only stages copies.
- Assuming this skill accepts a custom destination; it does not.

## Example Prompts

- Create or refresh `to-translate` with every Markdown file from this repo.
- Rebuild the translation staging folder and preserve the source directory structure.
- Mirror all `.md` files into `to-translate` without copying the destination into itself.
- Prepare a fresh Markdown-only tree for translation review.
