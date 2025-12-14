# Development

## Requirements

## Building the web site

In a PowerShell console, from the folder containing the `docs` folder:  `mkdocs build` or `mkdocs build *> build.log`

## Running in local mode

In a PowerShell console, from the folder containing the `docs` folder:

- To run the web site in local: `mkdocs serve &`, then go to the web site: <http://127.0.0.1:8000/eressea-doc/>
- To stop the web site: `Stop-Process -Name python`

## Deployment on GitHub

- `mkdocs gh-deploy`: <https://zendev1710.github.io/eressea-doc/> should be then updated
