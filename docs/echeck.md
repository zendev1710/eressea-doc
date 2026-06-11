---
# cSpell:locale en
alias: echeck
---
<!-- disable some rules due to autorefs plugin usage -->
<!-- markdownlint-disable MD041 MD042 -->
[](){ #echeck-id }

# ECheck

**ECheck** is the orders checker that also works on the Eressea server.  

ECheck is not perfect and not complete.  
There can be both false negative and false positive reports.  
So if ECheck doesn't report any errors, it doesn't necessarily mean that the orders are correct.  
If ECheck reports errors, it does not necessarily mean that the orders are invalid.  
Especially when there are rule changes or rare items, ECheck doesn't always know immediately.  
ECheck is intended more as an aid to check the orders again if necessary.  

ECheck can be accessed in different ways:

- When sending orders, ECheck is automatically called and the response email from the server contains the result.
  Here we only check for warning level 1 (see below)
- In Magellan. Here you can set the options as desired.
  Magellan can also add the "meta commands" automatically.
  These are comments that help ECheck, for example, to check silver consumption.
  However, there is actually no reason to use Magellan's ECheck anymore, since Magellan's own mechanisms (Syntax Check and "Open Problems") are more reliable and can do more
- On the command line (command prompt “cmd” on Windows, in any terminal on Linux).
  Then you have to specify the parameters listed below.

There are different warning levels controlled by command line parameters.  
With`-w1` only syntax errors are output.  
The steps `w2` until `w4` issue additional warnings, for example about silver consumption, teachers or routes.  
The `noxxx` parameters can also suppress certain warnings.  
ECheck normally assumes that you are entering German orders for E2.  
English orders can be checked, for example, with the `-Len` parameter.  

## Usage

```console
Usage: ./echeck [options] <orders file>

  -Ppfad  Path information for the additional files; the locale de is appended
  -Rgame  Read additional files from the game subdirectory; Default setting: e2
  -       Uses stdin instead of an input file.
  -b      suppresses warnings and errors (letter)
  -q      does not expect any information on people/silver in [] at UNIT
  -rnnn   Sets recruitment cost to nnn silver
  -c      writes the warnings and errors in a compiler-like form
  -m      writes the warnings and errors for Magellan
  -e      writes the checked file to stdout, error to stderr
  -E      writes the checked file to stdout, error to stdout
  -ofile  writes the checked file to the file 'file'
  -Ofile  writes errors to file 'file'
  -h      shows this little help
  -hs     shows list of keywords for tokens.txt
  -hb     shows list of orders for orders.txt
  -hp     shows list of parameters for parameter.txt
  -hr     shows list of directions for directions.txt
  -hm     shows list of messages for messages.txt
  -hf     shows list of files that ECheck is trying to read
  -s      uses stderr for warnings, errors etc., not stdout
  -p      shortens some expenses for piping
  -l      simuliert Silberpool-Funktion
  -n      Does not count NameMe comments (;;) as a line
  -noxxx  No xxx warnings. xxx can be:
    ship  Unit controls ship and may not have command
    route no check for cyclic ROUTE
    lost  Unit loses silver and items
  -w[n]   Level n warnings (default: 4)
     1    mainly syntax errors
     4    almost all warnings
     5    teacher/student
  -x      Line countingab PARTEI instead of the beginning of the file
  -Lloc   Sets locale loc
  -vm.l   Mainversion.Level - für Test, ob richtige ECheck-Version
  -Q      Quiet
  -C      Compact edition
```

## See also

- [Send in orders][sending-orders]

## External links and downloads

- [Current downloads for Windows (echeck.exe) and Linux (echeck)]
- [ECheck Sourcecode]
- [An outdated version of ECheck for Windows]

<!-- From [https://wiki.eressea.de/index.php?title=ECheck&oldid=7268] -->

[Current downloads for Windows (echeck.exe) and Linux (echeck)]: https://www.eressea.kn-bremen.de/downloads
[ECheck Sourcecode]: https://github.com/eressea/echeck
[An outdated version of ECheck for Windows]: https://www.eressea.de/files/echeck.zip
