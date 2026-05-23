<div align="center">
    <img src="./media/logo_large.webp" alt="Spec Kit Logo" width="200" height="200"/>
    <h1>🌱 Spec Kit</h1>
    <h3><em>Construa software de alta qualidade mais rápido.</em></h3>
</div>

<p align="center">
    <strong>Um kit de ferramentas de código aberto que permite você focar em cenários de produto e resultados previsíveis em vez de codificar cada peça do zero baseado em intuição.</strong>
</p>

<p align="center">
    <a href="https://github.com/github/spec-kit/releases/latest"><img src="https://img.shields.io/github/v/release/github/spec-kit" alt="Latest Release"/></a>
    <a href="https://github.com/github/spec-kit/stargazers"><img src="https://img.shields.io/github/stars/github/spec-kit?style=social" alt="GitHub stars"/></a>
    <a href="https://github.com/github/spec-kit/blob/main/LICENSE"><img src="https://img.shields.io/github/license/github/spec-kit" alt="License"/></a>
    <a href="https://github.github.io/spec-kit/"><img src="https://img.shields.io/badge/docs-GitHub_Pages-blue" alt="Documentation"/></a>
</p>

---

## Índice

- [🤔 O que é Desenvolvimento Orientado a Especificações?](#-o-que-é-desenvolvimento-orientado-a-especificações)
- [⚡ Primeiros Passos](#-primeiros-passos)
- [📽️ Visão Geral em Vídeo](#️-visão-geral-em-vídeo)
- [🧩 Extensões da Comunidade](#-extensões-da-comunidade)
- [🎨 Predefinições da Comunidade](#-predefinições-da-comunidade)
- [🚶 Passos a Passo da Comunidade](#-passos-a-passo-da-comunidade)
- [🛠️ Amigos da Comunidade](#️-amigos-da-comunidade)
- [🤖 Integrações de Agentes de Codificação IA Suportadas](#-integrações-de-agentes-de-codificação-ia-suportadas)
- [🔧 Referência da CLI Specify](#-referência-da-cli-specify)
- [🧩 Personalizando o Spec Kit: Extensões e Predefinições](#-personalizando-o-spec-kit-extensões-e-predefinições)
- [📚 Filosofia Central](#-filosofia-central)
- [🌟 Fases de Desenvolvimento](#-fases-de-desenvolvimento)
- [🎯 Objetivos Experimentais](#-objetivos-experimentais)
- [🔧 Pré-requisitos](#-pré-requisitos)
- [📖 Saiba Mais](#-saiba-mais)
- [📋 Processo Detalhado](#-processo-detalhado)
- [🆘 Suporte](#-suporte)
- [🙏 Agradecimentos](#-agradecimentos)
- [📄 Licença](#-licença)

## 🤔 O que é Desenvolvimento Orientado a Especificações?

O Desenvolvimento Orientado a Especificações **inverte o jogo** do desenvolvimento de software tradicional. Por décadas, o código foi rei — as especificações eram apenas andaimes que construíamos e descartávamos assim que o "trabalho real" de codificação começava. O Desenvolvimento Orientado a Especificações muda isso: **as especificações se tornam executáveis**, gerando diretamente implementações funcionais em vez de apenas guiá-las.

## ⚡ Primeiros Passos

### 1. Instale a CLI Specify

Requer **[uv](https://docs.astral.sh/uv/)** ([instalar uv](./docs/install/uv.md)). Substitua `vX.Y.Z` pela tag mais recente em [Releases](https://github.com/github/spec-kit/releases):

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git@vX.Y.Z
```

Consulte o [Guia de Instalação](./docs/installation.md) para métodos alternativos, verificação, atualização e solução de problemas.

### 2. Inicialize um projeto

```bash
specify init my-project --integration copilot
cd my-project
```

### 3. Estabeleça os princípios do projeto

Inicie seu agente de codificação no diretório do projeto. A maioria dos agentes expõe o spec-kit como comandos slash `/speckit.*`; Codex CLI em modo skills usa `$speckit-*` em vez disso.

Use o comando **`/speckit.constitution`** para criar os princípios governantes e diretrizes de desenvolvimento do seu projeto que guiarão todo o desenvolvimento subsequente.

```bash
/speckit.constitution Create principles focused on code quality, testing standards, user experience consistency, and performance requirements
```

### 4. Crie a especificação

Use o comando **`/speckit.specify`** para descrever o que você quer construir. Foque no **o quê** e **por quê**, não na pilha de tecnologia.

```bash
/speckit.specify Build an application that can help me organize my photos in separate photo albums. Albums are grouped by date and can be re-organized by dragging and dropping on the main page. Albums are never in other nested albums. Within each album, photos are previewed in a tile-like interface.
```

### 5. Crie um plano de implementação técnica

Use o comando **`/speckit.plan`** para fornecer sua pilha de tecnologia e escolhas de arquitetura.

```bash
/speckit.plan The application uses Vite with minimal number of libraries. Use vanilla HTML, CSS, and JavaScript as much as possible. Images are not uploaded anywhere and metadata is stored in a local SQLite database.
```

### 6. Divida em tarefas

Use **`/speckit.tasks`** para criar uma lista de tarefas acionáveis a partir do seu plano de implementação.

```bash
/speckit.tasks
```

### 7. Execute a implementação

Use **`/speckit.implement`** para executar todas as tarefas e construir sua funcionalidade de acordo com o plano.

```bash
/speckit.implement
```

Para instruções detalhadas passo a passo, consulte nosso [guia completo](./spec-driven.md).

## 📽️ Visão Geral em Vídeo

Quer ver o Spec Kit em ação? Assista nossa [visão geral em vídeo](https://www.youtube.com/watch?v=a9eR1xsfvHg&pp=0gcJCckJAYcqIYzv)!

[![Cabeçalho do vídeo do Spec Kit](/media/spec-kit-video-header.jpg)](https://www.youtube.com/watch?v=a9eR1xsfvHg&pp=0gcJCckJAYcqIYzv)

## 🧩 Extensões da Comunidade

Extensões contribuídas pela comunidade adicionam novos comandos, hooks e capacidades ao Spec Kit. Veja a lista completa na página [Extensões da Comunidade](https://github.github.io/spec-kit/community/extensions.html).

> [!NOTE]
> Extensões da comunidade são criadas e mantidas independentemente por seus respectivos autores. Os mantenedores apenas verificam se as entradas do catálogo estão completas e corretamente formatadas — eles **não revisam, auditam, endossam ou dão suporte ao código da extensão em si**. Revise o código-fonte da extensão antes da instalação e use por sua conta e risco.

Para enviar sua própria extensão, consulte o [Guia de Publicação de Extensões](extensions/EXTENSION-PUBLISHING-GUIDE.md).

## 🎨 Predefinições da Comunidade

Predefinições contribuídas pela comunidade personalizam o comportamento do Spec Kit — substituindo modelos, comandos e terminologia sem alterar nenhuma ferramenta. Veja a lista completa na página [Predefinições da Comunidade](https://github.github.io/spec-kit/community/presets.html).

> [!NOTE]
> Predefinições da comunidade são contribuições de terceiros e não são mantidas pela equipe do Spec Kit. Revise-as cuidadosamente antes do uso e consulte a página de documentação acima para o aviso completo.

Para enviar sua própria predefinição, consulte o [Guia de Publicação de Predefinições](presets/PUBLISHING.md).

## 🚶 Passo a Passo da Comunidade

Veja o Desenvolvimento Orientado a Especificações em ação em diferentes cenários com passo a passo contribuídos pela comunidade; encontre a lista completa na página [Passo a Passo da Comunidade](https://github.github.io/spec-kit/community/walkthroughs.html).

## 🛠️ Amigos da Comunidade

Projetos da comunidade que estendem, visualizam ou constroem sobre o Spec Kit. Veja a lista completa na página [Amigos da Comunidade](https://github.github.io/spec-kit/community/friends.html).

## 🤖 Integrações de Agentes de Codificação IA Suportadas

O Spec Kit funciona com mais de 30 agentes de codificação IA — tanto ferramentas CLI quanto assistentes baseados em IDE. Veja a lista completa com notas e detalhes de uso no guia [Integrações de Agentes de Codificação IA Suportadas](https://github.github.io/spec-kit/reference/integrations.html).

Execute `specify integration list` para ver todas as integrações disponíveis na sua versão instalada.

## Comandos Barra Disponíveis

Após executar `specify init`, seu agente de codificação IA terá acesso a estes comandos barra para desenvolvimento estruturado. Para integrações que suportam modo skills, passar `--integration <agent> --integration-options="--skills"` instala agent skills ao invés de arquivos de prompt de comando barra.

#### Comandos Principais

Comandos essenciais para o fluxo de trabalho de Desenvolvimento Orientado a Especificações:

| Comando                  | Agent Skill            | Descrição                                                                    |
| ------------------------ | ---------------------- | ---------------------------------------------------------------------------- |
| `/speckit.constitution`  | `speckit-constitution` | Criar ou atualizar princípios de governança e diretrizes de desenvolvimento |
| `/speckit.specify`       | `speckit-specify`      | Definir o que você quer construir (requisitos e histórias de usuário)       |
| `/speckit.plan`          | `speckit-plan`         | Criar planos técnicos de implementação com sua stack tecnológica escolhida  |
| `/speckit.tasks`         | `speckit-tasks`        | Gerar listas de tarefas acionáveis para implementação                        |
| `/speckit.taskstoissues` | `speckit-taskstoissues`| Converter listas de tarefas geradas em issues do GitHub para rastreamento   |
| `/speckit.implement`     | `speckit-implement`    | Executar todas as tarefas para construir a funcionalidade de acordo com o plano |

#### Comandos Opcionais

Comandos adicionais para qualidade e validação aprimoradas:

| Comando              | Agent Skill            | Descrição                                                                                                                                         |
| -------------------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `/speckit.clarify`   | `speckit-clarify`      | Esclarecer áreas subespecificadas (recomendado antes de `/speckit.plan`; anteriormente `/quizme`)                                                |
| `/speckit.analyze`   | `speckit-analyze`      | Análise de consistência e cobertura entre artefatos (executar após `/speckit.tasks`, antes de `/speckit.implement`)                              |
| `/speckit.checklist` | `speckit-checklist`    | Gerar checklists de qualidade personalizados que validam completude, clareza e consistência de requisitos (como "testes unitários para inglês")  |

## 🔧 Referência da CLI Specify

Para detalhes completos de comandos, opções e exemplos, consulte a [Referência da CLI](https://github.github.io/spec-kit/reference/overview.html).

## 🧩 Personalizando o Spec Kit: Extensões e Predefinições

O Spec Kit pode ser adaptado às suas necessidades através de dois sistemas complementares — **extensões** e **predefinições** — além de substituições locais do projeto para ajustes pontuais:

| Prioridade | Tipo de Componente                                | Localização                      |
| ---------: | ------------------------------------------------- | -------------------------------- |
|      ⬆ 1   | Sobrescritas Locais do Projeto                    | `.specify/templates/overrides/`  |
|        2   | Presets — Personalizar núcleo e extensões         | `.specify/presets/templates/`    |
|        3   | Extensões — Adicionar novas capacidades           | `.specify/extensions/templates/` |
|      ⬇ 4   | Núcleo do Spec Kit — Comandos e templates SDD integrados | `.specify/templates/`     |

- **Templates** são resolvidos em **tempo de execução** — o Spec Kit percorre a pilha de cima para baixo e usa a primeira correspondência.
- Sobrescritas locais do projeto (`.specify/templates/overrides/`) permitem fazer ajustes pontuais para um único projeto sem criar um preset completo.
- **Comandos de extensões/presets** são aplicados no **momento da instalação** — quando você executa `specify extension add` ou `specify preset add`, os arquivos de comando são escritos nos diretórios dos agentes (por exemplo, `.claude/commands/`).
- Se múltiplos presets ou extensões fornecem o mesmo comando, a versão de maior prioridade prevalece. Na remoção, a versão de próxima prioridade mais alta é restaurada automaticamente.
- Se não existirem sobrescritas ou personalizações, o Spec Kit usa seus padrões integrados.

### Extensões — Adicionar Novas Capacidades

Use **extensões** quando você precisar de funcionalidades que vão além do núcleo do Spec Kit. Extensões introduzem novos comandos e templates — por exemplo, adicionando fluxos de trabalho específicos de domínio que não são cobertos pelos comandos SDD integrados, integrando-se com ferramentas externas ou adicionando fases de desenvolvimento inteiramente novas. Elas expandem *o que o Spec Kit pode fazer*.

```bash
# Buscar extensões disponíveis
specify extension search

# Instalar uma extensão
specify extension add <nome-da-extensão>
```

Por exemplo, extensões podem adicionar integração com Jira, revisão de código pós-implementação, rastreabilidade de testes do Modelo V ou diagnósticos de saúde do projeto.

Consulte a [referência de Extensões](https://github.github.io/spec-kit/reference/extensions.html) para o guia completo de comandos. Navegue pelas [extensões da comunidade](#-extensões-da-comunidade) acima para ver o que está disponível.

### Presets — Personalizar Fluxos de Trabalho Existentes

Use **presets** quando você quiser alterar *como* o Spec Kit funciona sem adicionar novas capacidades. Presets sobrescrevem os templates e comandos que vêm com o núcleo *e* com as extensões instaladas — por exemplo, impondo um formato de especificação orientado à conformidade, usando terminologia específica de domínio ou aplicando padrões organizacionais a planos e tarefas. Eles personalizam os artefatos e instruções que o Spec Kit e suas extensões produzem.

```bash
# Buscar presets disponíveis
specify preset search

# Instalar um preset
specify preset add <nome-do-preset>
```

Por exemplo, presets podem reestruturar templates de especificação para exigir rastreabilidade regulatória, adaptar o fluxo de trabalho para se adequar à metodologia que você usa (por exemplo, Agile, Kanban, Waterfall, jobs-to-be-done ou domain-driven design), adicionar portões obrigatórios de revisão de segurança aos planos, impor ordenação de tarefas com testes primeiro ou localizar todo o fluxo de trabalho para um idioma diferente. A [demonstração pirate-speak](https://github.com/mnriem/spec-kit-pirate-speak-preset-demo) mostra o quão profunda a personalização pode ser. Múltiplos presets podem ser empilhados com ordenação de prioridade.

Consulte a [referência de Presets](https://github.github.io/spec-kit/reference/presets.html) para o guia completo de comandos, incluindo ordem de resolução e empilhamento de prioridades.

### Quando Usar Qual

| Objetivo | Use |
| --- | --- |
| Adicionar um novo comando ou fluxo de trabalho | Extensão |
| Personalizar o formato de especificações, planos ou tarefas | Preset |
| Integrar uma ferramenta ou serviço externo | Extensão |
| Impor padrões organizacionais ou regulatórios | Preset |
| Distribuir templates reutilizáveis específicos de domínio | Ambos — presets para sobrescritas de template, extensões para templates agrupados com novos comandos |

## 📚 Filosofia Central

O Desenvolvimento Orientado por Especificações é um processo estruturado que enfatiza:

- **Desenvolvimento orientado por intenção** onde as especificações definem o "*o quê*" antes do "*como*"
- **Criação de especificações ricas** usando guias e princípios organizacionais
- **Refinamento em múltiplas etapas** em vez de geração de código de uma só vez a partir de prompts
- **Dependência intensa** nas capacidades avançadas de modelos de IA para interpretação de especificações

## 🌟 Fases de Desenvolvimento

| Fase                                        | Foco                        | Atividades Principais                                                                                                                                              |
| ------------------------------------------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Desenvolvimento 0-para-1** ("Greenfield") | Gerar do zero                | <ul><li>Começar com requisitos de alto nível</li><li>Gerar especificações</li><li>Planejar etapas de implementação</li><li>Construir aplicações prontas para produção</li></ul> |
| **Exploração Criativa**                     | Implementações paralelas    | <ul><li>Explorar soluções diversas</li><li>Suportar múltiplas pilhas tecnológicas e arquiteturas</li><li>Experimentar com padrões de UX</li></ul>                  |
| **Aprimoramento Iterativo** ("Brownfield")  | Modernização brownfield     | <ul><li>Adicionar recursos iterativamente</li><li>Modernizar sistemas legados</li><li>Adaptar processos</li></ul>                                                  |

## 🎯 Objetivos Experimentais

Nossa pesquisa e experimentação focam em:

### Independência tecnológica

- Criar aplicações usando pilhas tecnológicas diversas
- Validar a hipótese de que o Desenvolvimento Orientado por Especificações é um processo não vinculado a tecnologias específicas, linguagens de programação ou frameworks

### Restrições empresariais

- Demonstrar desenvolvimento de aplicações de missão crítica
- Incorporar restrições organizacionais (provedores de nuvem, pilhas tecnológicas, práticas de engenharia)
- Suportar sistemas de design empresariais e requisitos de conformidade

### Desenvolvimento centrado no usuário

- Construir aplicações para diferentes coortes de usuários e preferências
- Suportar várias abordagens de desenvolvimento (desde vibe-coding até desenvolvimento nativo de IA)

### Processos criativos e iterativos

- Validar o conceito de exploração de implementação paralela
- Fornecer fluxos de trabalho robustos de desenvolvimento iterativo de recursos
- Estender processos para lidar com tarefas de atualização e modernização

## 🔧 Pré-requisitos

- **Linux/macOS/Windows**
- Agente de codificação IA [suportado](#-integrações-de-agentes-de-codificação-ia-suportadas).
- [uv](https://docs.astral.sh/uv/) para gerenciamento de pacotes (recomendado) ou [pipx](https://pypa.github.io/pipx/) para instalação persistente
- [Python 3.11+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)

Se você encontrar problemas com um agente, por favor abra uma issue para que possamos refinar a integração.

## 📖 Saiba Mais

- **[Metodologia Completa de Desenvolvimento Orientado por Especificações](./spec-driven.md)** - Mergulho profundo no processo completo
- **[Passo a Passo Detalhado](#-processo-detalhado)** - Guia de implementação passo a passo

---

## 📋 Processo Detalhado

<details>
<summary>Clique para expandir o passo a passo detalhado</summary>

Você pode usar a CLI Specify para inicializar seu projeto, o que trará os artefatos necessários para o seu ambiente. Execute:

```bash
specify init <project_name>
```

Ou inicialize no diretório atual:

```bash
specify init .
# ou use a flag --here
specify init --here
# Pular confirmação quando o diretório já tiver arquivos
specify init . --force
# ou
specify init --here --force
```

![CLI Specify inicializando um novo projeto no terminal](./media/specify_cli.gif)

Em um terminal interativo, você será solicitado a selecionar a integração do agente de codificação que está usando. Em sessões não interativas, como CI ou execuções canalizadas, `specify init` usa como padrão o GitHub Copilot, a menos que você passe `--integration`. Você também pode especificar proativamente a integração diretamente no terminal:

```bash
specify init <project_name> --integration copilot
specify init <project_name> --integration gemini
specify init <project_name> --integration codex

# Ou no diretório atual:
specify init . --integration copilot
specify init . --integration codex --integration-options="--skills"

# ou use a flag --here
specify init --here --integration copilot
specify init --here --integration codex --integration-options="--skills"

# Forçar mesclagem em um diretório atual não vazio
specify init . --force --integration copilot

# ou
specify init --here --force --integration copilot
```

A CLI verificará se você tem Claude Code, Gemini CLI, Cursor CLI, Qwen CLI, opencode, Codex CLI, Qoder CLI, Tabnine CLI, Kiro CLI, Pi, Forge, Goose ou Mistral Vibe instalado. Se você não tiver, ou preferir obter os modelos sem verificar as ferramentas corretas, use `--ignore-agent-tools` com seu comando:

```bash
specify init <project_name> --integration copilot --ignore-agent-tools
```

### **PASSO 1:** Estabelecer princípios do projeto

Vá para a pasta do projeto e execute seu agente de codificação. Em nosso exemplo, estamos usando `claude`.

![Inicializando ambiente Claude Code](./media/bootstrap-claude-code.gif)

Você saberá que as coisas estão configuradas corretamente se vir os comandos `/speckit.constitution`, `/speckit.specify`, `/speckit.plan`, `/speckit.tasks` e `/speckit.implement` disponíveis.

O primeiro passo deve ser estabelecer os princípios orientadores do seu projeto usando o comando `/speckit.constitution`. Isso ajuda a garantir tomadas de decisão consistentes em todas as fases de desenvolvimento subsequentes:

```text
/speckit.constitution Create principles focused on code quality, testing standards, user experience consistency, and performance requirements. Include governance for how these principles should guide technical decisions and implementation choices.
```

Este passo cria ou atualiza o arquivo `.specify/memory/constitution.md` com as diretrizes fundamentais do seu projeto que o agente de codificação referenciará durante as fases de especificação, planejamento e implementação.

### **PASSO 2:** Criar especificações do projeto

Com os princípios do projeto estabelecidos, você agora pode criar as especificações funcionais. Use o comando `/speckit.specify` e então forneça os requisitos concretos para o projeto que deseja desenvolver.

> [!IMPORTANT]
> Seja o mais explícito possível sobre *o que* você está tentando construir e *por quê*. **Não foque na pilha de tecnologia neste momento**.

Um exemplo de prompt:

```text
Develop Taskify, a team productivity platform. It should allow users to create projects, add team members,
assign tasks, comment and move tasks between boards in Kanban style. In this initial phase for this feature,
let's call it "Create Taskify," let's have multiple users but the users will be declared ahead of time, predefined.
I want five users in two different categories, one product manager and four engineers. Let's create three
different sample projects. Let's have the standard Kanban columns for the status of each task, such as "To Do,"
"In Progress," "In Review," and "Done." There will be no login for this application as this is just the very
first testing thing to ensure that our basic features are set up. For each task in the UI for a task card,
you should be able to change the current status of the task between the different columns in the Kanban work board.
You should be able to leave an unlimited number of comments for a particular card. You should be able to, from that task
card, assign one of the valid users. When you first launch Taskify, it's going to give you a list of the five users to pick
from. There will be no password required. When you click on a user, you go into the main view, which displays the list of
projects. When you click on a project, you open the Kanban board for that project. You're going to see the columns.
You'll be able to drag and drop cards back and forth between different columns. You will see any cards that are
assigned to you, the currently logged in user, in a different color from all the other ones, so you can quickly
see yours. You can edit any comments that you make, but you can't edit comments that other people made. You can
delete any comments that you made, but you can't delete comments anybody else made.
```

Depois que este prompt for inserido, você deverá ver o Claude Code iniciar o processo de planejamento e elaboração de especificações. O Claude Code também acionará alguns dos scripts integrados para configurar o repositório.

Uma vez que este passo seja concluído, você deverá ter um novo branch criado (por exemplo, `001-create-taskify`), bem como uma nova especificação no diretório `specs/001-create-taskify`.

A especificação produzida deve conter um conjunto de histórias de usuário e requisitos funcionais, conforme definido no modelo.

Nesta etapa, o conteúdo da pasta do seu projeto deve se assemelhar ao seguinte:

```text
└── .specify
    ├── memory
    │  └── constitution.md
    ├── scripts
    │  └── bash
    │      ├── check-prerequisites.sh
    │      ├── common.sh
    │      ├── create-new-feature.sh
    │      ├── setup-plan.sh
    │      └── setup-tasks.sh
    ├── specs
    │  └── 001-create-taskify
    │      └── spec.md
    └── templates
        ├── plan-template.md
        ├── spec-template.md
        └── tasks-template.md
```

### **PASSO 3:** Esclarecimento da especificação funcional (obrigatório antes do planejamento)

Com a especificação de linha de base criada, você pode prosseguir e esclarecer quaisquer requisitos que não foram capturados adequadamente na primeira tentativa.

Você deve executar o fluxo de trabalho estruturado de esclarecimento **antes** de criar um plano técnico para reduzir retrabalho posteriormente.

Ordem preferida:

1. Use `/speckit.clarify` (estruturado) – questionamento sequencial baseado em cobertura que registra respostas em uma seção de Esclarecimentos.
2. Opcionalmente, faça um acompanhamento com refinamento ad-hoc de forma livre se algo ainda parecer vago.

Se você intencionalmente quiser pular o esclarecimento (por exemplo, spike ou protótipo exploratório), declare isso explicitamente para que o agente não bloqueie em esclarecimentos faltantes.

Exemplo de prompt de refinamento de forma livre (após `/speckit.clarify` se ainda necessário):

```text
Para cada projeto de exemplo ou projeto que você criar, deve haver um número variável de tarefas entre 5 e 15
tarefas para cada um, distribuídas aleatoriamente em diferentes estados de conclusão. Certifique-se de que há pelo menos
uma tarefa em cada estágio de conclusão.
```

Você também deve pedir ao Claude Code para validar o **Review & Acceptance Checklist**, marcando as coisas que foram validadas/atendem aos requisitos e deixar desmarcadas as que não atendem. O seguinte prompt pode ser usado:

```text
Leia a lista de verificação de revisão e aceitação, e marque cada item na lista se a especificação da funcionalidade atender aos critérios. Deixe vazio se não atender.
```

É importante usar a interação com o Claude Code como uma oportunidade para esclarecer e fazer perguntas sobre a especificação - **não trate a primeira tentativa como final**.

### **PASSO 4:** Gerar um plano

Agora você pode ser específico sobre a pilha tecnológica e outros requisitos técnicos. Você pode usar o comando `/speckit.plan` que está integrado no template do projeto com um prompt como este:

```text
Vamos gerar isso usando .NET Aspire, usando Postgres como banco de dados. O frontend deve usar
Blazor server com quadros de tarefas com arrastar e soltar, atualizações em tempo real. Deve haver uma API REST criada com uma API de projetos,
API de tarefas e uma API de notificações.
```

A saída deste passo incluirá uma série de documentos de detalhes de implementação, com sua árvore de diretórios se assemelhando a isto:

```text
.
├── CLAUDE.md
├── memory
│  └── constitution.md
├── scripts
│  └── bash
│      ├── check-prerequisites.sh
│      ├── common.sh
│      ├── create-new-feature.sh
│      ├── setup-plan.sh
│      └── setup-tasks.sh
├── specs
│  └── 001-create-taskify
│      ├── contracts
│      │  ├── api-spec.json
│      │  └── signalr-spec.md
│      ├── data-model.md
│      ├── plan.md
│      ├── quickstart.md
│      ├── research.md
│      └── spec.md
└── templates
    ├── CLAUDE-template.md
    ├── plan-template.md
    ├── spec-template.md
    └── tasks-template.md
```

Verifique o documento `research.md` para garantir que a pilha tecnológica correta seja usada, com base em suas instruções. Você pode pedir ao Claude Code para refiná-lo se algum dos componentes se destacar, ou até mesmo fazer com que ele verifique a versão instalada localmente da plataforma/framework que você deseja usar (por exemplo, .NET).

Além disso, você pode querer pedir ao Claude Code para pesquisar detalhes sobre a pilha tecnológica escolhida se for algo que está mudando rapidamente (por exemplo, .NET Aspire, frameworks JS), com um prompt como este:

```text
Quero que você percorra o plano de implementação e os detalhes de implementação, procurando áreas que poderiam
se beneficiar de pesquisa adicional, já que .NET Aspire é uma biblioteca em rápida mudança. Para aquelas áreas que você identificar que
requerem pesquisa adicional, quero que você atualize o documento de pesquisa com detalhes adicionais sobre as versões específicas
que vamos usar nesta aplicação Taskify e gere tarefas de pesquisa paralelas para esclarecer
quaisquer detalhes utilizando pesquisa na web.
```

Durante esse processo, você pode descobrir que o Claude Code fica travado pesquisando a coisa errada - você pode ajudar a direcioná-lo na direção correta com um prompt como este:

```text
Acho que precisamos dividir isso em uma série de etapas. Primeiro, identifique uma lista de tarefas
que você precisaria fazer durante a implementação das quais não tem certeza ou que se beneficiariam
de pesquisa adicional. Escreva uma lista dessas tarefas. E então, para cada uma dessas tarefas,
quero que você inicie uma tarefa de pesquisa separada para que o resultado final seja que estamos pesquisando
todas essas tarefas muito específicas em paralelo. O que vi você fazendo foi que parecia que você estava
pesquisando .NET Aspire em geral e não acho que isso vai nos ajudar muito neste caso.
Essa pesquisa é muito ampla. A pesquisa precisa ajudar você a resolver uma questão específica e direcionada.
```

> [!NOTE]
> O Claude Code pode ser muito entusiasmado e adicionar componentes que você não pediu. Peça para esclarecer a justificativa e a origem da mudança.

### **ETAPA 5:** Fazer o Claude Code validar o plano

Com o plano em vigor, você deve fazer o Claude Code revisá-lo para garantir que não há peças faltando. Você pode usar um prompt como este:

```text
Agora quero que você vá e audite o plano de implementação e os arquivos de detalhes da implementação.
Leia-o com o objetivo de determinar se há uma sequência de tarefas que você precisa estar fazendo que são óbvias
ao ler isso. Porque não sei se há informação suficiente aqui. Por exemplo, quando olho para a implementação
principal, seria útil referenciar os lugares apropriados nos detalhes da implementação onde pode encontrar
a informação enquanto percorre cada etapa na implementação principal ou no refinamento.
```

Isso ajuda a refinar o plano de implementação e ajuda você a evitar possíveis pontos cegos que o Claude Code perdeu em seu ciclo de planejamento. Uma vez que a passagem de refinamento inicial esteja completa, peça ao Claude Code para passar pela lista de verificação mais uma vez antes de você poder chegar à implementação.

Você também pode pedir ao Claude Code (se tiver a [CLI do GitHub](https://docs.github.com/pt/github-cli/github-cli) instalada) para criar um pull request do seu branch atual para o `main` com uma descrição detalhada, para garantir que o esforço seja devidamente rastreado.

> [!NOTE]
> Antes de fazer o agente implementar, também vale a pena solicitar ao Claude Code que verifique os detalhes para ver se há peças sobre-engenheiradas (lembre-se - ele pode ser muito entusiasmado). Se componentes ou decisões sobre-engenheirados existirem, você pode pedir ao Claude Code para resolvê-los. Certifique-se de que o Claude Code siga a constituição em `.specify/memory/constitution.md` como a peça fundamental que ele deve aderir ao estabelecer o plano.

### **ETAPA 6:** Gerar divisão de tarefas com /speckit.tasks

Com o plano de implementação validado, você pode agora dividir o plano em tarefas específicas e acionáveis que podem ser executadas na ordem correta. Use o comando `/speckit.tasks` para gerar automaticamente uma divisão detalhada de tarefas do seu plano de implementação:

```text
/speckit.tasks
```

Esta etapa cria um arquivo `tasks.md` no diretório de especificação da sua funcionalidade que contém:

- **Divisão de tarefas organizada por história de usuário** - Cada história de usuário se torna uma fase de implementação separada com seu próprio conjunto de tarefas
- **Gerenciamento de dependências** - As tarefas são ordenadas para respeitar dependências entre componentes (por exemplo, modelos antes de serviços, serviços antes de endpoints)
- **Marcadores de execução paralela** - Tarefas que podem ser executadas em paralelo são marcadas com `[P]` para otimizar o fluxo de trabalho de desenvolvimento
- **Especificações de caminhos de arquivo** - Cada tarefa inclui os caminhos de arquivo exatos onde a implementação deve ocorrer
- **Estrutura de desenvolvimento orientado a testes** - Se testes forem solicitados, tarefas de teste são incluídas e ordenadas para serem escritas antes da implementação
- **Validação de checkpoint** - Cada fase de história de usuário inclui checkpoints para validar funcionalidade independente

O tasks.md gerado fornece um roteiro claro para o comando `/speckit.implement`, garantindo implementação sistemática que mantém qualidade de código e permite entrega incremental de histórias de usuário.

### **ETAPA 7:** Implementação

Quando estiver pronto, use o comando `/speckit.implement` para executar seu plano de implementação:

```text
/speckit.implement
```

O comando `/speckit.implement` irá:

- Validar que todos os pré-requisitos estão no lugar (constituição, especificação, plano e tarefas)
- Analisar a divisão de tarefas de `tasks.md`
- Executar tarefas na ordem correta, respeitando dependências e marcadores de execução paralela
- Seguir a abordagem TDD definida no seu plano de tarefas
- Fornecer atualizações de progresso e tratar erros apropriadamente

> [!IMPORTANT]
> O agente de codificação executará comandos CLI locais (como `dotnet`, `npm`, etc.) - certifique-se de ter as ferramentas necessárias instaladas na sua máquina.

Uma vez que a implementação esteja completa, teste a aplicação e resolva quaisquer erros de tempo de execução que podem não estar visíveis nos logs da CLI (por exemplo, erros do console do navegador). Você pode copiar e colar tais erros de volta para seu agente de codificação para resolução.

</details>

---

## 🆘 Suporte

Para suporte, por favor abra uma [issue no GitHub](https://github.com/github/spec-kit/issues/new). Aceitamos relatórios de bugs, solicitações de funcionalidades e perguntas sobre o uso do Desenvolvimento Orientado a Especificações.

## 🙏 Agradecimentos

Este projeto é fortemente influenciado e baseado no trabalho e pesquisa de [John Lam](https://github.com/jflam).

## 📄 Licença

Este projeto é licenciado sob os termos da licença de código aberto MIT. Por favor, consulte o arquivo [LICENSE](./LICENSE) para os termos completos.
