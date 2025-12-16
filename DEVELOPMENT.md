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
4. Install [mkdocs](https://www.mkdocs.org/user-guide/installation/): `pip install mkdocs`
5. Install [mkdocs-material](https://squidfunk.github.io/mkdocs-material/getting-started/#installation): `pip install mkdocs-material`
6. Install other needed mkdocs plugins:
   1. [mkdocs-static-i18n](https://ultrabug.github.io/mkdocs-static-i18n/getting-started/installation/): `pip install mkdocs-static-i18n[material]`
   2. [mkdocs-alias-plugin](https://github.com/EddyLuten/mkdocs-alias-plugin?tab=readme-ov-file#installation): `pip install mkdocs-alias-plugin`
   3. [mkdocs-redirects](https://github.com/mkdocs/mkdocs-redirects) (optional): `pip install mkdocs-redirects`

## Building the web site

In a PowerShell console, from the folder containing the `docs` folder:  `mkdocs build` or `mkdocs build *> build.log`

## Running in local mode

In a PowerShell console, from the folder containing the `docs` folder:

- To run the web site in local: `Start-Process mkdocs serve &`, then go to the web site: <http://127.0.0.1:8000/eressea-doc/>
- To stop the web site: `Stop-Process -Name python`

## Deployment on GitHub

- `mkdocs gh-deploy`: <https://zendev1710.github.io/eressea-doc/> should be then updated
