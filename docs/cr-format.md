---
# cSpell:locale en
alias: cr-format
---
# CR Format

Der CR besteht aus Blocks, Attributen und Listeneinträge. Ein Block entspricht meist einem Objekt, ein Attribut einer Variablen des Objektes. Blöcke können Unterblöcke haben.

## Blocks

Names and number of blocks are not predefined. Depending on the game and version, different blocks may be contained in a file. It is entirely legitimate to create a subset of the blocks, for example to turn a complete report into 'just' a map.

Blocks are designated by a single capitalized word consisting only of the letters A-Z. Blocks can have an identifier consisting of one or more signed 32-bit integers. The ids are unique, so each can only appear once in a CR per block. The id can be followed by ';' A separate comment will follow, but this should be avoided.

Blocks without id are always subblocks of the last previous block with id. A block of this type may occur multiple times, but only once per parent block (they are, so to speak, unique with respect to the id of the parent block).

Examples:

    ```text
    VERSION 16
    REGION -3 -7
    REGIONSBOTSCHAFTEN
    ```

## Attributes

Names and number of attributes are not predefined. An attribute consists of two parts: value and tag. The tag should consist of letters and numbers, but should not contain spaces. The value is either a list of one or more integers, or a string written in quotation marks. Value and day are separated from each other by a semicolon.

Since version 35, an attribute may only appear once within a block. In CR versions prior to 35, there were some blocks that violated this rule, such as the ADDRESSES block.

Examples:

    ```text
    0 0;Bergbau
    "Xandaryl";Insel
    172;Runde
    ```

## List entries

Attributes without a tag must be treated separately. These are entries in a list of commands, messages, etc. In terms of structure, they are equivalent to string attributes, but do not have a semicolon or tag at the end of the line.

Example:

    ```text
    "MAKE Haus"
    "Thorin; ein Recke"
    "Thorin (thor) konnte kein Silber verdienen"
    ```

## Tips for implementation

It is best to parse the CR line by line. After reading a line, you first check whether it is a block: blocks are the only ones that begin with a letter. If it is not one but begins with a '-' or a number, then it is an integer attribute. If it begins with a '"', it is a string or list entry.

### About blocks

You parse blocks by reading the name of the block (up to the first space) and then the ids separated by spaces. Pay attention to any comments (for Eressea CRs before version 36)!

### Integer attributes

Die Zahl identifizieren, indem man bis zum ';' liest. Danach den Namen des Tags lesen, bis zum Ende der Zeile. Zu beachten ist, das möglicherweise noch Leerzeichen am Ende der Zeile oder um das ';' herum stehen könnten.

### About list entries

Read until the next '"'. Be careful, there can certainly be semicolons in the string. If the '"' is no longer followed by a semicolon, it is a list element, otherwise it is a string attribute.

### String attributes

The string has already been read so the ';' skip, and find the name of the tag. Again, watch out for spaces around the semicolon or at the end of the line.

### Fallstricke

- An integer attribute can consist of several numbers, such as skills. The number of integers is not necessarily the same for attributes with the same name, and it may not always be 2 (currently it is, but this is left open for future expansion)
- Blank lines: There shouldn't actually be any blank lines in the CR. But a good parser should be able to handle it
- Invalid lines: CRs are often garbled because a mail tool or editor has wrapped the lines. In this case, a warning should definitely be issued and the attribute should be ignored
- CR/LF: Mac, Unix and Windows each store the end of a line differently. The parser should be able to recognize all formats
- Capitalization: The spelling of the tags should be unique, i.e. not mixed and not converted. A good parser will still recognize two tags as the same if they differ in capitalization
- Umlauts: Both strings and tags can contain umlauts. A good parser recognizes the common transliteration of German umlauts and sets, for example, trees = trees, desert = desert
- End of file: It can happen that there is no line break after the last line of the CR

## Reserved blocks and tags

- VERSION is the block that describes the file. It is the first block in the CR. A good parser should process multiple VERSIONs blocks in its input, and treat this case as if a second report had been read in (example: cat 1.cr 2.cr 3.cr | parser)
- Round is a tag containing the age of the block. Blocks within a CR can be dated differently, if, for example, a report was compiled from information collected over several rounds. Das Runde-Attribut sollte das Datum der aktuellsten Informationen über den Block angeben. It is inherited across sub-blocks, so if these blocks represent newer or older versions, they should get their own round attribute. CRs without turn information are best treated as being from turn 0
- Configuration is a tag in the version block. It can be used to describe the content of the CR, z.b. with the name of the tool that created it or a description. For example, “mercator-map”, “EMap-export”. The value "Standard" is reserved for the Eressea server

## See also

- [CR-Format Details] collected and prepared by tww

<!-- From [https://wiki.eressea.de/index.php?title=CR\_Format&oldid=5847] -->

[CR-Format Details]: http://dose.0wnz.at/thewhitewolf/cr-format
