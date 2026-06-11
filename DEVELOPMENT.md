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
4. Install [ProperDocs](https://properdocs.org/) (continuation of MkDocs 1): `pip install properdocs`
5. Install [mkdocs-material](https://squidfunk.github.io/mkdocs-material/getting-started/#installation): `pip install mkdocs-material`
6. Install other needed MkDocs plugins:
   1. [mkdocs-static-i18n](https://ultrabug.github.io/mkdocs-static-i18n/getting-started/installation/): `pip install mkdocs-static-i18n[material]`
   2. [mkdocs-alias-plugin](https://codeberg.org/luten/mkdocs-alias-plugin#installation): `pip install mkdocs-alias-plugin`
   3. [mkdocs-redirects](https://github.com/mkdocs/mkdocs-redirects) (optional): `pip install mkdocs-redirects`
   4. [mkdocs-table-reader](https://github.com/timvink/mkdocs-table-reader-plugin): `pip install mkdocs-table-reader-plugin`
   5. [mkdocs-autorefs](https://github.com/mkdocstrings/autorefs): `pip install mkdocs-autorefs`
7. [Install Task](https://taskfile.dev/docs/installation#winget)
8. [Install Coreutils for Windows](https://github.com/microsoft/coreutils)(`winget install Microsoft.Coreutils`)

## Building the web site

In a **PowerShell** console, from the folder containing the `docs` folder: `properdocs build` or `properdocs build *> build.log`.

## Running in local mode

In a **PowerShell** console, from the folder containing the `docs` folder:

- To run the web site in local: `Start-Process properdocs serve &`, then go to the web site: <http://127.0.0.1:8000/eressea-doc/>
- To stop the web site: `Stop-Process -Name python`

On your computer, to get changes after browser page update: `properdocs serve --livereload`.  
<!--
For an auto-reload much faster: `mkdocs serve --dirtyreload`.  
-->

## Deployment on GitHub

`properdocs gh-deploy`:

- site content is updated on the `gh-deploy` repository branch
- Updated branch is deployed on <https://zendev1710.github.io/eressea-doc/>, which should be then updated

## Python useful commands

### list of packages installed versions

`pip list`

Results :

```console
...
mkdocs                     1.6.1
mkdocs-alias-plugin        0.10.1
mkdocs-get-deps            0.2.0
mkdocs-material            9.7.1
mkdocs-material-extensions 1.3.1
mkdocs-redirects           1.2.2
mkdocs-static-i18n         1.3.0
...
```
