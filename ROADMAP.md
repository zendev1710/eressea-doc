# Roadmap

At this moment it's rather a TODO list.

Features to be taken into account (no due date):

- [x] Make internal links mkardown page location-independent (using autorefs plugin?)
- [x] Fix all dead links
- [x] Fix all warnings displayed on `properdocs build` commande
- [x] Fix all markdown lint issues
- [x] order keywords as top-level heading title are between backticks (\`...\`)
- [x] order keywords as all mentioned between backticks (\`...\`)
- [] Translate remainging paragraphs in french
- [x] Fix all spell lint issues in french language
- [x] Fix all spell issues in english language
- [] Fix all spell issues in german language
- [] Update all english magic spell descriptions with the ones in Eressea server source code .po files
- [] Fix orders examples as block codes (especially in german language where it was missed)
- [x] Lore dialogues and narrations as "parchment" style
- [ ] Write formulas with katex
- [ ] Compact tables when columns number is high
- [ ] Column sorting on tables when it would be useful
- [ ] Simple form in pages to test formulas when it would be useful
- [ ] Same page structure between french and english languages
- [ ] Same page structure between english anf german languages
- [ ] Redesign the sitemap (pages organization)
- [ ] Complete contribution guide
- [ ] CI pipeline based on GitHub Actions triggered on a pull request before merging and deploy
- [ ] Review for all the documentation pages written in french language
- [ ] Review for all the documentation pages written in english language
- [ ] Review for all the documentation pages written in german - over time
- [ ] Better tooltips (background color, frame color...)
- [ ] Ony theme color by language
- [ ] Being able to restrict search scope to current language
- [ ] Documentation versioning
- [ ] Icons, emoji and/or svg images
- [ ] Configure markdown-link-check and fix all link lint issues
- [ ] Generate the french documentation as a downloadable PDF
- [ ] Generate the english documentation as a downloadable PDF
- [ ] Generate the german documentation as a downloadable PDF
- [ ] Update documentation with wiki site updates since 2025, 1st december

*Note: These features won'be be necesseray implemented in the above defined order.*

## Review

A page review is achieved when:

- spelling mistakes have been corrected
- same content between the three language-specific pages
- identical or similar formatting etween the three language-specific pages
- above page-related already implemented features have been applyied
- np line exceeds the max length (**to be defined**)

| page                         | FR | EN | DE |
|------------------------------|:--:|:--:|:--:|
| [adamantium][^2]             | ✔️ | ✔️ | ✔️ |
| [alchemy]                    | ✔️ | ✔️ |    |
| [alliances]                  | ✔️ |    |    |
| [amulet-of-true-sight][^1]   | ✔️ | ✔️ | ✔️ |
| [antimagic-crystal][^1]      | ✔️ | ✔️ | ✔️ |
| [armed]                      | ✔️ | ✔️ |    |
| [atlantis]                   | ✔️ | ✔️ |    |
| [auto-event-response]        |    |    |    |
| [auto-learning-chains]       |    |    |    |
| [auto-trading]               |    |    |    |
| [auto-transport]             | ✔️ | ✔️ |    |
| [basics]                     | ✔️ |    |    |
| [birthday-cake][^1]          | ✔️ | ✔️ | ✔️ |
| [buildings-others]           |    |    |    |
| [buildings]                  |    |    |    |
| [castles]                    |    |    |    |
| [christmas-tree]             | ✔️ | ✔️ | ✔️ |
| [christmas]                  | ✔️ | ✔️ | ✔️ |
| [cmd-attack]                 | ✔️ | ✔️ |    |
| [cmd-banner]                 |    |    |    |
| [cmd-buy]                    |    |    |    |
| [cmd-carry]                  |    |    |    |
| [cmd-cast]                   |    |    |    |
| [cmd-claim]                  |    |    |    |
| [cmd-combat]                 |    |    |    |
| [cmd-combatspell]            |    |    |    |
| [cmd-comment-slash]          |    |    |    |
| [cmd-contact]                |    |    |    |
| [cmd-default]                |    |    |    |
| [cmd-describe]               |    |    |    |
| [cmd-destroy]                |    |    |    |
| [cmd-email]                  |    |    |    |
| [cmd-end]                    |    |    |    |
| [cmd-enter]                  |    |    |    |
| [cmd-entertain]              |    |    |    |
| [cmd-eressea]                |    |    |    |
| [cmd-follow]                 |    |    |    |
| [cmd-forget]                 |    |    |    |
| [cmd-give]                   |    |    |    |
| [cmd-group]                  |    |    |    |
| [cmd-grow]                   |    |    |    |
| [cmd-guard]                  |    |    |    |
| [cmd-help]                   |    |    |    |
| [cmd-hide]                   |    |    |    |
| [cmd-language]               |    |    |    |
| [cmd-learn-auto]             |    |    |    |
| [cmd-learn]                  |    |    |    |
| [cmd-leave]                  |    |    |    |
| [cmd-make]                   |    |    |    |
| [cmd-message]                |    |    |    |
| [cmd-move]                   |    |    |    |
| [cmd-name]                   |    |    |    |
| [cmd-next]                   |    |    |    |
| [cmd-number]                 |    |    |    |
| [cmd-option]                 |    |    |    |
| [cmd-origin]                 |    |    |    |
| [cmd-password]               | ✔️ |    |    |
| [cmd-pay-not]                |    |    |    |
| [cmd-piracy]                 |    |    |    |
| [cmd-plant]                  |    |    |    |
| [cmd-prefix]                 |    |    |    |
| [cmd-promote]                |    |    |    |
| [cmd-quit]                   |    |    |    |
| [cmd-recruit]                |    |    |    |
| [cmd-region]                 | ✔️ | ✔️ | ✔️ |
| [cmd-research]               |    |    |    |
| [cmd-reserve]                |    |    |    |
| [cmd-ride]                   |    |    |    |
| [cmd-route]                  |    |    |    |
| [cmd-sell]                   |    |    |    |
| [cmd-comment]                |    |    |    |
| [cmd-show]                   |    |    |    |
| [cmd-sort]                   |    |    |    |
| [cmd-spy]                    |    |    |    |
| [cmd-steal]                  |    |    |    |
| [cmd-tax]                    |    |    |    |
| [cmd-teach]                  |    |    |    |
| [cmd-unit]                   | ✔️ | ✔️ |    |
| [cmd-use]                    |    |    |    |
| [cmd-work]                   |    |    |    |
| [commands-extended]          |    |    |    |
| [commands-list]              |    |    |    |
| [commands-send-from]         |    |    |    |
| [commands-send]              |    |    |    |
| [commands-sequence]          |    |    |    |
| [commands-short-desc]        |    |    |    |
| [commands]                   |    |    |    |
| [cr-format]                  |    |    |    |
| [csmapfx]                    |    |    |    |
| [development]                | ✔️ | ✔️ | ✔️ |
| [echeck]                     |    |    |    |
| [ehmv]                       | ✔️ | ✔️ | ✔️ |
| [eressea-join]               |    |    |    |
| [eressea-story]              |    |    |    |
| [faction-pool]               |    |    |    |
| [factions]                   |    |    |    |
| [familiars]                  |    |    |    |
| [faq]                        |    |    |    |
| [farmers-hike]               |    |    |    |
| [fftools]                    |    |    |    |
| [first-round]                |    |    |    |
| [flaming-sword]              |    |    |    |
| [getting-started-tips]       |    |    |    |
| [herbs]                      |    |    |    |
| [hints]                      |    |    |    |
| [index]                      | ✔️ | ✔️ | ✔️ |
| [introduction]               | ✔️ |    |    |
| [items-pool]                 |    |    |    |
| [items]                      |    |    |    |
| [laen][^1]                   | ✔️ | ✔️ | ✔️ |
| [magellan]                   |    |    |    |
| [magic-school-cerddor]       |    |    |    |
| [magic-school-draig]         |    |    |    |
| [magic-school-gwyrrd]        |    |    |    |
| [magic-school-illaun]        |    |    |    |
| [magic-school-tybied]        |    |    |    |
| [magic-schools]              |    |    |    |
| [magic]                      |    |    |    |
| [mistletoe]                  | ✔️ | ✔️ | ✔️ |
| [monsters]                   | ✔️ | ✔️ |    |
| [optimize-learning]          |    |    |    |
| [optimize-production]        |    |    |    |
| [optimize-transport]         |    |    |    |
| [optimize-way-finding]       |    |    |    |
| [pentagram-and-tirawon]      |    |    |    |
| [plague][^1]                 | ✔️ | ✔️ | ✔️ |
| [play-too-much-if]           |    |    |    |
| [player-pages]               |    |    |    |
| [potions-and-herbs]          |    |    |    |
| [production]                 |    |    |    |
| [puppy-protection]           |    | ✔️ |    |
| [races]                      |    |    |    |
| [reports][^1]                | ✔️ | ✔️ | ✔️ |
| [resources]                  |    |    |    |
| [ring-of-invisibility]       | ✔️ | ✔️ | ✔️ |
| [ring-of-power][^1]          | ✔️ | ✔️ | ✔️ |
| [roads]                      |    |    |    |
| [rules]                      | ✔️ |    |    |
| [sailing]                    |    |    |    |
| [shell]                      | ✔️ | ✔️ | ✔️ |
| [ships]                      |    |    |    |
| [silver]                     |    |    |    |
| [skills-list]                |    |    |    |
| [skills-modifiers]           |    |    |    |
| [skills]                     |    |    |    |
| [snowman]                    | ✔️ | ✔️ | ✔️ |
| [spells-descriptions]        |    |    |    |
| [spells-list]                |    |    |    |
| [sphere-of-invisibility][^1] | ✔️ | ✔️ | ✔️ |
| [stardust]                   | ✔️ | ✔️ | ✔️ |
| [stealth]                    |    |    |    |
| [solar-sail]                 | ✔️ | ✔️ | ✔️ |
| [tactic]                     |    |    |    |
| [terrains]                   | ✔️ |    |    |
| [tips-and-tricks]            |    |    |    |
| [toad]                       | ✔️ | ✔️ | ✔️ |
| [travel]                     |    |    |    |
| [tutorials][^1]              | ✔️ | ✔️ | ✔️ |
| [vorlage]                    |    |    |    |
| [war-tables]                 |    |    |    |
| [war]                        |    |    |    |
| [weekly-report]              |    |    |    |
| [world]                      |    |    |    |

[^1]: Empty page. To be written.
[^2]: The page could benefit from additional content.

[amulet-of-true-sight]: https://zendev1710.github.io/eressea-doc/amulet-of-true-sight "Amulet of True Sight"
[antimagic-crystal]: https://zendev1710.github.io/eressea-doc/antimagic-crystal "Antimagic Crystal"
[birthday-cake]: https://zendev1710.github.io/eressea-doc/birthday-cake "birthday-cake"
[buildings-others]: https://zendev1710.github.io/eressea-doc/buildings-others "buildings-others"
[buildings]: https://zendev1710.github.io/eressea-doc/buildings "buildings"
[stealth]: https://zendev1710.github.io/eressea-doc/stealth "stealth"
[castles]: https://zendev1710.github.io/eressea-doc/castles "castles"
[christmas]: https://zendev1710.github.io/eressea-doc/christmas "Christmas"
[christmas-tree]: https://zendev1710.github.io/eressea-doc/christmas-tree "christmas-tree"
[cmd-attack]: https://zendev1710.github.io/eressea-doc/cmd-attack "cmd-attack"
[cmd-banner]: https://zendev1710.github.io/eressea-doc/cmd-banner "cmd-banner"
[cmd-buy]: https://zendev1710.github.io/eressea-doc/cmd-buy "cmd-buy"
[cmd-carry]: https://zendev1710.github.io/eressea-doc/cmd-carry "cmd-carry"
[cmd-cast]: https://zendev1710.github.io/eressea-doc/cmd-cast "cmd-cast"
[cmd-claim]: https://zendev1710.github.io/eressea-doc/cmd-claim "cmd-claim"
[cmd-combat]: https://zendev1710.github.io/eressea-doc/cmd-combat "cmd-combat"
[cmd-combatspell]: https://zendev1710.github.io/eressea-doc/cmd-combatspell "cmd-combatspell"
[cmd-comment-slash]: https://zendev1710.github.io/eressea-doc/cmd-comment-slash "cmd-comment"
[cmd-contact]: https://zendev1710.github.io/eressea-doc/cmd-contact "cmd-contact"
[cmd-default]: https://zendev1710.github.io/eressea-doc/cmd-default "cmd-default"
[cmd-describe]: https://zendev1710.github.io/eressea-doc/cmd-describe "cmd-describe"
[cmd-destroy]: https://zendev1710.github.io/eressea-doc/cmd-destroy "cmd-destroy"
[cmd-email]: https://zendev1710.github.io/eressea-doc/cmd-email "cmd-email"
[cmd-end]: https://zendev1710.github.io/eressea-doc/cmd-end "cmd-end"
[cmd-enter]: https://zendev1710.github.io/eressea-doc/cmd-enter "cmd-enter"
[cmd-entertain]: https://zendev1710.github.io/eressea-doc/cmd-entertain "cmd-entertain"
[cmd-eressea]: https://zendev1710.github.io/eressea-doc/cmd-eressea "cmd-eressea"
[cmd-follow]: https://zendev1710.github.io/eressea-doc/cmd-follow "cmd-follow"
[cmd-forget]: https://zendev1710.github.io/eressea-doc/cmd-forget "cmd-forget"
[cmd-give]: https://zendev1710.github.io/eressea-doc/cmd-give "cmd-give"
[cmd-group]: https://zendev1710.github.io/eressea-doc/cmd-group "cmd-group"
[cmd-grow]: https://zendev1710.github.io/eressea-doc/cmd-grow "cmd-grow"
[cmd-guard]: https://zendev1710.github.io/eressea-doc/cmd-guard "cmd-guard"
[cmd-help]: https://zendev1710.github.io/eressea-doc/cmd-help "cmd-help"
[cmd-hide]: https://zendev1710.github.io/eressea-doc/cmd-hide "cmd-hide"
[cmd-language]: https://zendev1710.github.io/eressea-doc/cmd-language "cmd-language"
[cmd-learn-auto]: https://zendev1710.github.io/eressea-doc/cmd-learn-auto "cmd-learn-auto"
[cmd-learn]: https://zendev1710.github.io/eressea-doc/cmd-learn "cmd-learn"
[cmd-leave]: https://zendev1710.github.io/eressea-doc/cmd-leave "cmd-leave"
[cmd-make]: https://zendev1710.github.io/eressea-doc/cmd-make "cmd-make"
[cmd-message]: https://zendev1710.github.io/eressea-doc/cmd-message "cmd-message"
[cmd-move]: https://zendev1710.github.io/eressea-doc/cmd-move "cmd-move"
[cmd-name]: https://zendev1710.github.io/eressea-doc/cmd-name "cmd-name"
[cmd-next]: https://zendev1710.github.io/eressea-doc/cmd-next "cmd-next"
[cmd-number]: https://zendev1710.github.io/eressea-doc/cmd-number "cmd-number"
[cmd-option]: https://zendev1710.github.io/eressea-doc/cmd-option "cmd-option"
[cmd-origin]: https://zendev1710.github.io/eressea-doc/cmd-origin "cmd-origin"
[cmd-password]: https://zendev1710.github.io/eressea-doc/cmd-password "cmd-password"
[cmd-pay-not]: https://zendev1710.github.io/eressea-doc/cmd-pay-not "cmd-pay-not"
[cmd-piracy]: https://zendev1710.github.io/eressea-doc/cmd-piracy "cmd-piracy"
[cmd-plant]: https://zendev1710.github.io/eressea-doc/cmd-plant "cmd-plant"
[cmd-prefix]: https://zendev1710.github.io/eressea-doc/cmd-prefix "cmd-prefix"
[cmd-promote]: https://zendev1710.github.io/eressea-doc/cmd-promote "cmd-promote"
[cmd-quit]: https://zendev1710.github.io/eressea-doc/cmd-quit "cmd-quit"
[cmd-recruit]: https://zendev1710.github.io/eressea-doc/cmd-recruit "cmd-recruit"
[cmd-region]: https://zendev1710.github.io/eressea-doc/cmd-region "cmd-region"
[cmd-research]: https://zendev1710.github.io/eressea-doc/cmd-research "cmd-research"
[cmd-reserve]: https://zendev1710.github.io/eressea-doc/cmd-reserve "cmd-reserve"
[cmd-ride]: https://zendev1710.github.io/eressea-doc/cmd-ride "cmd-ride"
[cmd-route]: https://zendev1710.github.io/eressea-doc/cmd-route "cmd-route"
[cmd-sell]: https://zendev1710.github.io/eressea-doc/cmd-sell "cmd-sell"
[cmd-comment]: https://zendev1710.github.io/eressea-doc/cmd-comment "cmd-comment"
[cmd-show]: https://zendev1710.github.io/eressea-doc/cmd-show "cmd-show"
[cmd-sort]: https://zendev1710.github.io/eressea-doc/cmd-sort "cmd-sort"
[cmd-spy]: https://zendev1710.github.io/eressea-doc/cmd-spy "cmd-spy"
[cmd-steal]: https://zendev1710.github.io/eressea-doc/cmd-steal "cmd-steal"
[cmd-tax]: https://zendev1710.github.io/eressea-doc/cmd-tax "cmd-tax"
[cmd-teach]: https://zendev1710.github.io/eressea-doc/cmd-teach "cmd-teach"
[cmd-unit]: https://zendev1710.github.io/eressea-doc/cmd-unit "cmd-unit"
[cmd-use]: https://zendev1710.github.io/eressea-doc/cmd-use "cmd-use"
[cmd-work]: https://zendev1710.github.io/eressea-doc/cmd-work "cmd-work"
[commands-extended]: https://zendev1710.github.io/eressea-doc/commands-extended "commands-extended"
[commands-list]: https://zendev1710.github.io/eressea-doc/commands-list "commands-list"
[commands-send-from]: https://zendev1710.github.io/eressea-doc/commands-send-from-magellan "commands-send-from-magellan"
[commands-send]: https://zendev1710.github.io/eressea-doc/commands-send "commands-send"
[commands-sequence]: https://zendev1710.github.io/eressea-doc/commands-sequence "commands-sequence"
[commands]: https://zendev1710.github.io/eressea-doc/commands "commands"
[cr-format]: https://zendev1710.github.io/eressea-doc/cr-format "cr-format"
[csmapfx]: https://zendev1710.github.io/eressea-doc/csmapfx "csmapfx"
[development]: https://zendev1710.github.io/eressea-doc/development "development"
[echeck]: https://wiki.eressea.de/echeck "echeck"
[ehmv]: https://zendev1710.github.io/eressea-doc/ehmv "ehmv"
[eressea-join]: https://zendev1710.github.io/eressea-doc/eressea-join "eressea-join"
[eressea-story]: https://zendev1710.github.io/eressea-doc/eressea-story "eressea-story"
[faction-pool]: https://zendev1710.github.io/eressea-doc/faction-pool "faction-pool"
[factions]: https://zendev1710.github.io/eressea-doc/factions "factions"
[familiars]: https://zendev1710.github.io/eressea-doc/familiars "familiars"
[faq]: https://wiki.eressea.de/faq "faq"
[farmers-hike]: https://zendev1710.github.io/eressea-doc/farmers-hike "farmers-hike"
[fftools]: https://zendev1710.github.io/eressea-doc/fftools "fftools"
[flaming-sword]: https://zendev1710.github.io/eressea-doc/flaming-sword "flaming-sword"
[getting-started-tips]: https://zendev1710.github.io/eressea-doc/getting-started-tips "getting-started-tips"
[herbs]: https://zendev1710.github.io/eressea-doc/herbs "herbs"
[hints]: https://zendev1710.github.io/eressea-doc/hints "hints"
[index]: https://zendev1710.github.io/eressea-doc/index "home"
[introduction]: https://zendev1710.github.io/eressea-doc/introduction "introduction"
[items-pool]: https://zendev1710.github.io/eressea-doc/items-pool "items-pool"
[items]: https://zendev1710.github.io/eressea-doc/items "items"
[laen]: https://zendev1710.github.io/eressea-doc/laen "laen"
[magellan]: https://wiki.eressea.de/magellan "magellan"
[magic-school-cerddor]: https://zendev1710.github.io/eressea-doc/magic-school-cerddor "magic-school-cerddor"
[magic-school-draig]: https://zendev1710.github.io/eressea-doc/magic-school-draig "magic-school-draig"
[magic-school-gwyrrd]: https://zendev1710.github.io/eressea-doc/magic-school-gwyrrd "magic-school-gwyrrd"
[magic-school-illaun]: https://zendev1710.github.io/eressea-doc/magic-school-illaun "magic-school-illaun"
[magic-school-tybied]: https://zendev1710.github.io/eressea-doc/magic-school-tybied "magic-school-tybied"
[magic-schools]: https://zendev1710.github.io/eressea-doc/magic-schools "magic-schools"
[magic]: https://zendev1710.github.io/eressea-doc/magic "magic"
[mistletoe]: https://zendev1710.github.io/eressea-doc/mistletoe "mistletoe"
[monsters]: https://zendev1710.github.io/eressea-doc/monsters "monsters"
[optimize-learning]: https://zendev1710.github.io/eressea-doc/optimize-learning-chains "optimize-learning-chains"
[optimize-production]: https://zendev1710.github.io/eressea-doc/optimize-production "optimize-production"
[optimize-transport]: https://zendev1710.github.io/eressea-doc/optimize-transport "optimize-transport"
[optimize-way-finding]: https://zendev1710.github.io/eressea-doc/optimize-way-finding "optimize-way-finding"
[pentagram-and-tirawon]: https://zendev1710.github.io/eressea-doc/pentagram-and-tirawon "pentagram-and-tirawon"
[plague]: https://zendev1710.github.io/eressea-doc/plague "Plague"
[play-too-much-if]: https://zendev1710.github.io/eressea-doc/play-too-much-if "play-too-much-if"
[player-pages]: https://zendev1710.github.io/eressea-doc/player-pages "player-pages"
[potions-and-herbs]: https://zendev1710.github.io/eressea-doc/potions-and-herbs "potions-and-herbs"
[production]: https://zendev1710.github.io/eressea-doc/production "production"
[puppy-protection]: https://zendev1710.github.io/eressea-doc/puppy-protection "puppy-protection"
[races]: https://zendev1710.github.io/eressea-doc/races "races"
[reports]: https://zendev1710.github.io/eressea-doc/reports "reports"
[resources]: https://zendev1710.github.io/eressea-doc/resources "resources"
[ring-of-invisibility]: https://zendev1710.github.io/eressea-doc/ring-of-invisibility "Ring of Invisibility"
[ring-of-power]: https://zendev1710.github.io/eressea-doc/ring-of-power "Ring of Power"
[roads]: https://zendev1710.github.io/eressea-doc/roads "roads"
[first-round]: https://zendev1710.github.io/eressea-doc/first-round "first-round"
[rules]: https://zendev1710.github.io/eressea-doc/rules "rules"
[sailing]: https://zendev1710.github.io/eressea-doc/sailing "sailing"
[shell]: https://zendev1710.github.io/eressea-doc/shell "shell"
[ships]: https://zendev1710.github.io/eressea-doc/ships "ships"
[silver]: https://zendev1710.github.io/eressea-doc/silver "silver"
[skills-list]: https://zendev1710.github.io/eressea-doc/skills-list "skills-list"
[skills-modifiers]: https://zendev1710.github.io/eressea-doc/skills-modifiers "skills-modifiers"
[skills]: https://zendev1710.github.io/eressea-doc/skills "skills"
[snowman]: https://zendev1710.github.io/eressea-doc/snowman "snowman"
[spells-descriptions]: https://zendev1710.github.io/eressea-doc/spells-descriptions "spells-descriptions"
[spells-list]: https://zendev1710.github.io/eressea-doc/spells-list "spells-list"
[sphere-of-invisibility]: https://zendev1710.github.io/eressea-doc/sphere-of-invisibility "Sphere of Invisibility"
[stardust]: https://zendev1710.github.io/eressea-doc/stardust "stardust"
[solar-sail]: https://zendev1710.github.io/eressea-doc/solar-sail "solar-sail"
[tactic]: https://zendev1710.github.io/eressea-doc/tactic "tactic"
[terrains]: https://zendev1710.github.io/eressea-doc/terrains "terrains"
[tips-and-tricks]: https://zendev1710.github.io/eressea-doc/tips-and-tricks "tips-and-tricks"
[toad]: https://zendev1710.github.io/eressea-doc/toad "toad"
[travel]: https://zendev1710.github.io/eressea-doc/travel "travel"
[tutorials]: https://zendev1710.github.io/eressea-doc/tutorials "tutorials"
[vorlage]: https://wiki.eressea.de/vorlage "vorlage"
[war-tables]: https://zendev1710.github.io/eressea-doc/war-tables "war-tables"
[war]: https://zendev1710.github.io/eressea-doc/war "war"
[weekly-report]: https://zendev1710.github.io/eressea-doc/weekly-report "weekly-report"
[world]: https://zendev1710.github.io/eressea-doc/world "world"
