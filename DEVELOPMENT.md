<!-- cspell: -->
# Development

## Requirements

1. [Install PowerShell](https://learn.microsoft.com/en-us/powershell/scripting/install/install-powershell-on-windows?view=powershell-7.5#install-powershell-using-winget-recommended) latest version
2. Install VSCode and some useful extensions in it :
   1. [markdownlint](https://github.com/DavidAnson/vscode-markdownlint)
   2. [Markdown All in One](https://github.com/yzhang-gh/vscode-markdown)
   3. [Markdown Table Prettifier](https://github.com/darkriszty/MarkdownTablePrettify-VSCodeExt)
   4. [Markdown Emoji](https://github.com/mjbvz/vscode-markdown-emoji)
   5. [VS Slug](https://github.com/neptunedesign/vs-slug)
   6. [Sort lines](https://github.com/Tyriar/vscode-sort-lines)
   7. [Trailing Spaces](https://github.com/shardulm94/vscode-trailingspaces.git)
3. Install python 3
4. Install [Node.js](https://nodejs.org/) (npm is used by `task install:dev`)
5. [Install Task](https://taskfile.dev/docs/installation#winget)
6. [Install Coreutils for Windows](https://github.com/microsoft/coreutils) (`winget install Microsoft.Coreutils`)
7. [Install Git for Windows](https://git-scm.com/download/win) — several tasks use POSIX utilities (`find`, `xargs`, `grep`, `sed`) and must be run from **Git Bash** or **WSL**; `Taskfile.yml` marks them with a comment
8. [Install GitHub CLI](https://cli.github.com/) — required by `task deploy`, which creates the GitHub release displayed in the site header

Then install everything (Python packages from `requirements.txt` + npm dev tools) in one go:

```console
task install
```

It runs [`install:mkdocs`](#tasks) (`pip install -r requirements.txt`) then [`install:dev`](#tasks) (`npm install -g markdownlint-cli2 markdown-link-check cspell` and `npm install`, where the cspell dictionaries are resolved from `./node_modules`).

## Tasks

All the tasks are defined in [`Taskfile.yml`](Taskfile.yml) and run with [Task](https://taskfile.dev/) as `task <name>`.

| Task                  | Description                                                                                 | Phase        |
|-----------------------|---------------------------------------------------------------------------------------------|--------------|
| `install`             | Install all the dependencies (Python + npm)                                                 | Setup        |
| `install:mkdocs`      | Install the Python dependencies from `requirements.txt`                                     | Setup        |
| `install:dev`         | Install the npm dev tools and the local dictionaries                                        | Setup        |
| `deps:outdated`       | List the pinned dependencies that have a newer version available                            | Dependencies |
| `deps:update`         | Bump `requirements.txt` to the latest **non-breaking** versions, then install them          | Dependencies |
| `deps:update:all`     | Bump `requirements.txt` to **every** latest version, breaking changes included              | Dependencies |
| `run`                 | Serve the documentation locally (`properdocs serve`)                                        | Develop      |
| `build`               | Build the documentation into `site/` (`properdocs build`)                                   | Build        |
| `lint`                | Run `lint:md`, `lint:spell` and `lint:link`                                                 | Lint         |
| `lint:md`             | Lint all the markdown files with markdownlint                                               | Lint         |
| `lint:md-fr`          | Lint the French markdown files with markdownlint                                            | Lint         |
| `lint:md-de`          | Lint the German markdown files with markdownlint                                            | Lint         |
| `lint:md-en`          | Lint the English markdown files with markdownlint                                           | Lint         |
| `lint:md-on-changes`  | Lint only the markdown files modified against `origin/main` (exit code 2 if none)           | Lint         |
| `lint:spell`          | Spell check all the markdown files with cspell                                              | Lint         |
| `lint:spell-fr`       | Spell check the French markdown files with cspell                                           | Lint         |
| `lint:spell-de`       | Spell check the German markdown files with cspell                                           | Lint         |
| `lint:spell-en`       | Spell check the English markdown files with cspell                                          | Lint         |
| `lint:spell-changes`  | Spell check only the modified markdown files (exit code 2 if none)                          | Lint         |
| `lint:link`           | Lint all the markdown links with markdown-link-check                                        | Lint         |
| `lint:link-fr`        | Lint the French markdown links with markdown-link-check                                     | Lint         |
| `lint:link-de`        | Lint the German markdown links with markdown-link-check                                     | Lint         |
| `lint:link-en`        | Lint the English markdown links with markdown-link-check                                    | Lint         |
| `lint:link-changes`   | Lint the links of the modified markdown files (exit code 2 if none)                         | Lint         |
| `lint:link:all`       | Lint all the markdown links with markdown-link-check                                        | Lint         |
| `lint:link:wget`      | Crawl the running local server with `wget --spider`                                         | Lint         |
| `lint:link:permalink` | Check that every modified page defines a `permalink`                                        | Lint         |
| `deploy`              | Check the git state, lint, publish on GitHub Pages, refresh the version shown in the header | Deploy       |

The `lint:*-fr`, `lint:*-de` and `lint:*-en` variants restrict a linter to one language; `lint:*-changes` restricts it to what you actually touched and is the fastest way to review a local edit.

> The `lint:link*` tasks query external websites: they are a **maintenance** tool, run when you want, never a gate. `task deploy` deliberately runs only `lint:md` and `lint:spell`, so an unavailable third-party site cannot block a valid publication.

## Workflow

| Phase                    | When                                        | Tasks                                                                                                     |
|--------------------------|---------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| **1. Setup**             | Once, and after a `requirements.txt` change | `task install`                                                                                            |
| **2. Write**             | While authoring                             | `task run` → <http://127.0.0.1:8000/eressea-doc/>                                                         |
| **3. Review**            | Before each commit                          | `task lint:md-on-changes` + `task lint:spell-changes` + `task lint:link-changes`, or the full `task lint` |
| **4. Publish your work** | After the review is green                   | `git add …` → `git commit …` → `git push`                                                                 |
| **5. Deploy**            | When `origin/main` should be live           | `task deploy`                                                                                             |
| **6. Maintain**          | From time to time                           | `task deps:outdated`, then `task deps:update`                                                             |

**Phase 5 — `task deploy`** does, in order, and stops at the first failure:

1. **git state** — refuses to run if the working tree is dirty or if the branch differs from its upstream (ahead *or* behind). This matters because `properdocs gh-deploy` builds the **working tree**, and the release tag needs the commit to exist on GitHub: without the check you would publish untraceable content and then fail on the version, leaving a half-done deploy.
2. **`lint:md`** then **`lint:spell`** — deterministic, local linters only.
3. **`properdocs gh-deploy`** — pushes the built site to the `gh-pages` branch.
4. **GitHub release** — creates a release whose tag (`0.9.24`) is what [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) displays as the repository version in the header, then drops the previous rolling release. A tag that exists locally (`0.9`, …) is a real release and is never deleted.
   Its notes are a build stamp (`Documentation build <version> (<sha>)`) **prepended** to the list of commits GitHub generates since the previous release (`--generate-notes`), so the release page always shows what changed without anyone writing it. The title is passed explicitly, otherwise GitHub would invent one.

> Material reads the version **client side** from `releases/latest` and caches it in `sessionStorage`: after a deploy, open a **new tab** (or clear the session storage) to see the new number.

## Building the web site

With [Task](#tasks) : `task build`.

Equivalent, in a **PowerShell** console from the folder containing the `docs` folder: `properdocs build` or `properdocs build *> build.log`.

## Running in local mode

With [Task](#tasks) : `task run`.

Equivalent, in a **PowerShell** console from the folder containing the `docs` folder:

- To run the web site in local: `Start-Process properdocs serve &`, then go to the web site: <http://127.0.0.1:8000/eressea-doc/>
- To stop the web site: `Stop-Process -Name python`

On your computer, to get changes after browser page update: `properdocs serve --livereload`.
<!--
For an auto-reload much faster: `mkdocs serve --dirtyreload`.
-->

## Before deploying on production site

`task deploy` runs `lint:md` and `lint:spell` for you and aborts if either fails, so this step is **automatic**. Run it manually only when you want to check something on its own:

- `task lint:md` — markdown structure
- `task lint:spell` — spelling, all three languages (`task lint:spell-fr` for French only)
- `task lint:link` — external links, **not** part of the deploy gate because it depends on third-party websites being up

`task lint:md-on-changes` and `task lint:spell-changes` are the quick variants while you are still editing.

## Deployment on GitHub

```console
task deploy
```

- the git state is checked first (clean tree, branch in sync with its upstream)
- `lint:md` and `lint:spell` must pass
- site content is updated on the **`gh-pages`** branch
- the updated branch is deployed on <https://zendev1710.github.io/eressea-doc/>
- a GitHub release is created, which updates the version displayed in the site header and carries auto-generated release notes

If the git check fails, nothing is published: commit and push first.

In case of GitHub authentication problem:

- Goto <https://github.com/settings/tokens/new>
- Create a token (scopes: repo, workflow, gist)
- $env:GH_TOKEN = "<token>"
- gh auth status

## Python useful commands

### List of packages installed versions

`pip list`

To know which of them have a newer release, prefer `task deps:outdated`, which compares against `requirements.txt` and tells you what a `task deps:update` would change.

### Check a package version

`pip show <package name>`

Example :

`pip show mkdocs-material`

### Update packages dependencies

`task deps:update` bumps only the versions that are not breaking and installs them; `task deps:update:all` also takes the major version jumps. Both rewrite `requirements.txt`, so review the diff before committing :

```console
task deps:update
git diff requirements.txt
```

The helper behind them is [`scripts/update_requirements.py`](scripts/update_requirements.py), usable on its own :

```console
python scripts/update_requirements.py            # report only, no change
python scripts/update_requirements.py --write    # rewrite requirements.txt
python scripts/update_requirements.py --write --stable
```
