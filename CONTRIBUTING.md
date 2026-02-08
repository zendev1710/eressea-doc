# Contributing

<!--
Material for MkDocs is an actively maintained and constantly improved project
that serves a diverse user base with varying backgrounds and needs. In order to
effectively address the needs of all our users, evaluate change requests, and
fix bugs, we maintainers need to put in a lot of work. We have devoted
significant effort to creating better templates for our issue tracker,
optimizing the processes for our users to report bugs, request features or
changes, contribute to the project, or exchange with our community.

Given the wealth of valuable knowledge contained in numerous issues and
discussions, we consider our [issue tracker] and [discussion board] to serve as
a crucial __knowledge base__ that is an important addition to our [documentation]
and brings value to both new and experienced users of Material for MkDocs.

  [discussion board]: https://github.com/squidfunk/mkdocs-material/discussions
  [issue tracker]: https://github.com/squidfunk/mkdocs-material/issues
  [documentation]: https://squidfunk.github.io/mkdocs-material/

## How to contribute

### Creating an issue

#### [Report a bug]

    __Something is not working?__ Report a bug in Material for MkDocs by
    creating an issue with a reproduction

#### [Report a docs issue]

    __Missing information in our docs?__ Report missing information or
    potential inconsistencies in our documentation

#### [Request a change]

    __Want to submit an idea?__ Propose a change, feature request, or
    suggest an improvement

#### [Ask a question]

    __Have a question or need help?__ Ask a question on our [discussion board]
    and get in touch with our community

### Contributing to documentation

#### [Add a translation]

    __Missing support for your language?__ Add missing translations for a new
    or already supported language

#### [Create a pull request]

    __Want to create a pull request?__ Learn how to create a comprehensive
    and useful pull request (PR)s

  [Report a bug]: docs/contributing/reporting-a-bug.md
  [Report a docs issue]: docs/contributing/reporting-a-docs-issue.md
  [Request a change]: docs/contributing/requesting-a-change.md
  [Ask a question]: https://github.com/squidfunk/mkdocs-material/discussions
  [Add a translation]: docs/contributing/adding-translations.md
  [Create a pull request]: docs/contributing/making-a-pull-request.md
-->

## Markdown

### Add links

### Use aliases

The MkDocs **alias** plugin should be used when it's possible.  
Why ? Because we don't want to specify a relative path to a markdown page, e.g. `./magic/magic-schhools.md#draig`, otherwise links would be broken when reorganizing pages folders.

So we can write:

- a link to a page like this: `[[page-alias|text]]`
- a link to an anchor like this: `[[page-alias#my-section|text]]`

Caution:

- if `page-alias` is not a defined alias, `mkdocs serve` command could fail with a Python exception error.
- anchor must be **slugifyied** (for german and french pages)

Limitations:

- ```[[page-alias|`MAKE [number] HORSE`]]``` is not converted in a link (due to `[` and `]` surrounding `number`)
- `[[page-alias|text]]` cannot be a markdown table cell value (due to pipe charcater)

When above limitation is encountered, ass a workaround, the link must be written without alias usage:

- `[text](link)`, or
- `[text][footnote-link]` and `[footnote-link]: ./my-page.md#mu-anchor` (footnote pattern)

### Use tooltips for french pages

As Eressea only manages german and english languages, tooltips on link are recommended when it's useful. Write:

- `[[skills-list#riding|l'équitation]]{title="Riding"}`
- `[[skills-list#perception|perception]]` (no tooltip, as in french and english languages, it's the same word)
