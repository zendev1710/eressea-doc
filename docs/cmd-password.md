---
# cSpell:locale en
alias: cmd-password
---
# PASSWORD

**`PASSWORD`**`["new-password"]`  

This resets the password.  
You must always use it together with the [[cmd-eressea]] order from the next orders file onwards.  
Only letters and numbers are allowed in the password.  
If it contains illegal characters, these will be replaced by random allowed characters.  
`PASSWORD` without parameters sets a randomly generated password.  

At the beginning, each faction is assigned a random password.  

Example:

```text
; in the second week of the month hearth fire
ERESSEA 11 "OldPassword"
PASSWORD "Incorrect" ; no effect
UNIT 75
    PASSWORD "MoftZga" ; That applies from the next round!
    [...]
        
; in the last week of the month hearth fire
ERESSEA 11 "MoftZga"
[...]
```

Caution:

- The password is the only place in the orders file that is case sensitive
- The password must be set by a unit
- The password that was valid in the last turn or the one that was set in the last turn always applies to the respective orders file.
  The password from the last train is still valid even if several orders files were sent in for the current train in which different passwords were set
- The password was only successfully reset if the corresponding message was also included in the evaluation: "The password was changed to "blabla"

<!-- From [https://wiki.eressea.de/index.php?title=PASSWORD&oldid=6276] -->
