---
# cSpell:locale en
alias: extended-commands
---
# Extended Commands

ExtendedCommands is a plugin for [[magellan]] that is included as standard and can be used to automate orders.

There is an introduction and a few example scripts on the [official site].

The script library is hidden in the Magellan menu: *`Plugins > Advanced Commands > Edit Library...`*.
A new view opens on the side, with a large text area for entering code, as well as buttons for executing and saving.

What follows are meta example scripts.

## Meta scripts

In general you can copy the scripts one after the other, but I divided it into 4 parts:

1. Imports: Copy only 2 lines.
2. Function library: Simply copy it in
3. Configuration: Here you have to lend a little hand
4. Views: You can set what you want to do.

If you want to write something yourself, you can find everything you need under *`Desktop > Advanced Commands > Help*`.
You can also display the page in the browser using the “Browser” button.

Oh yes, here are the 2 lines for the import:

```java
import magellan.library.*;
import magellan.library.rules.*;
```

Here are my pre-made scripts:

### Meta castle building signs

A call from `metaBurgenbauSchilder()` in all regions you will receive a sign with the following information: Castle size M Morale Silver per castle size /stone for the next castle upgrade Stone efficiency (= Silver per castle size /stone for the next castle upgrade)

```java
/*********************************************
*        Meta's BurgenbauSchilder            *
* Version 0.5                                *
*********************************************/
metaBurgenbauSchilder() {
  int moral;
  int burggroesse;
  int silberpool;
  int bauern;
  int nextBurgUpgrade;
  int stein2Upgrade;
  int steinEffizienz;
  String signtext;
  for (Region region : world.regions().values()) {
    bauern = region.getPeasants();
    region.clearSigns();
    if (bauern > 0){
      moral = region.getMorale();
      burggroesse = 0;
      for (Building building : region.buildings()){
        if (building.getSize()>burggroesse){// TODO check whether building = castle
          burggroesse = building.getSize();
        }
      }
      silberpool = region.getSilver();
      if (burggroesse<10) nextBurgUpgrade = 10;
      else if (burggroesse<50) nextBurgUpgrade = 50;
      else if (burggroesse<250) nextBurgUpgrade = 250;
      else if (burggroesse<1250) nextBurgUpgrade = 1250;
      else if (burggroesse<6250) nextBurgUpgrade = 6250;
      else nextBurgUpgrade = 0; // it will be a while before I need it
      stein2Upgrade = nextBurgUpgrade - burggroesse;
      steinEffizienz = silberpool/stein2Upgrade;
      signtext = ""+burggroesse+" M"+moral;
      region.addSign(new Sign( signtext ));
      signtext = ""+silberpool/100+"$/"+stein2Upgrade+"S";
      region.addSign(new Sign( signtext ));
      signtext = ""+steinEffizienz/100+","+steinEffizienz%100; //+"="+steinEffizienz;
      if (steinEffizienz>10000) signtext = "**" + signtext + "**";
      else if (steinEffizienz>1000) signtext = "*" + signtext + "*";
      region.addSign(new Sign( signtext ));
    }
  }
}
```

### Meta friend enemy signs

This is a bit more complicated as it requires some configuration. More detailed documentation will be provided later:

```java
/*********************************************
*        Meta's Friend enemy signs           *
* Version 0.6                                *
*********************************************/
metaFreundFeindSchilder(String type) {
  if (type.equals("people")){ // just counting people
    HashMap people;
    String allianceName;
    for (Region region : world.regions().values()) {
      people = new HashMap();
      for (Unit unit : region.units()) {
        allianceName = metaGetFriendFoeInfo(unit.getFaction());
        if (people.containsKey(allianceName)) { 
    people.put(allianceName, 
        people.get(allianceName)
        +unit.getPersons());
        } else {
          people.put(allianceName, unit.getPersons());
        }
      }
      region.clearSigns();
      Iterator iterator = people.keySet().iterator();
      String signtext = "";
      while (iterator.hasNext()) {
        String allianceStr = iterator.next();
        int amount = people.get(allianceStr);
        signtext = allianceStr + ":" + amount;
        Sign sign = new Sign( signtext );
        region.addSign(sign);
      } 
    }
  }
  else if (type.equals("soldier")){
    HashMap people;
    HashMap soldiers;
    HashMap heros;
    String friendFoeInfo;
    for (Region region : world.regions().values()) { // all regions
      people = new HashMap();
      soldiers = new HashMap();
      heros = new HashMap();
      for (Unit unit : region.units()) { // Add up
        friendFoeInfo = metaGetFriendFoeInfo(unit.getFaction());
        if (!(people.containsKey(friendFoeInfo))) { // if empty init
          people.put(friendFoeInfo,0);
        }
        if (!(soldiers.containsKey(friendFoeInfo))) {//wenn leer init
          soldiers.put(friendFoeInfo,0);
        }
        if (!(heros.containsKey(friendFoeInfo))) { // if empty init
          heros.put(friendFoeInfo,0);
        }
        if (!metaUnitIsSoldier(unit)){ // no soldiers
          people.put(friendFoeInfo,people.get(friendFoeInfo)+unit.getPersons());
        } else if (unit.isHero()){ // Heroes
          heros.put(friendFoeInfo,heros.get(friendFoeInfo)+unit.getPersons());
        } else { // soldiers
          soldiers.put(friendFoeInfo,soldiers.get(friendFoeInfo)+unit.getPersons());
        }
      }
      region.clearSigns();
      Iterator iterator = people.keySet().iterator();
      String signtext = "";
      while (iterator.hasNext()) {
        String ffi = iterator.next(); // Friend foe info
        int p = people.get(ffi);
        int s = soldiers.get(ffi);
        int h = heros.get(ffi);
        signtext = ffi + ":"+ p;
        if (s>0) signtext = signtext+"+"+s;
        if (h>0) signtext = signtext+"+"+h+"H";
        Sign sign = new Sign( signtext );
        region.addSign(sign);
      }
    }
  }
}

boolean metaUnitIsSoldier(unit) { // a little shortened from the Helper
  Collection items = unit.getItems();
  ItemCategory weapons = world.rules.getItemCategory(StringID.create("weapons"), false);
  for (Item item : items) {
    ItemCategory itemCategory = item.getItemType().getCategory();
    if (itemCategory == null) {continue;}
    if (itemCategory.equals(weapons)) {
      Skill useSkill = item.getItemType().getUseSkill();
      if (useSkill != null) {
        for (Skill skill : unit.getSkills()) {
          if (useSkill.getSkillType().equals(skill.getSkillType())) {
            return true;
          }
        }
      }
    }
  }
  return false;
}

String metaGetFriendFoeInfo(Faction faction){
  String factionId = faction.getID().toString();
  HashMap tmpCallback = new HashMap();
  tmpCallback = metaFriendFoeCallback(tmpCallback);
  if (tmpCallback.containsKey(factionId)){
    return tmpCallback.get(factionId).toString();
  } else {
    return factionId;
  }
}

metaDiplomatieListe(String chefdiplomat,String outputType){
  Unit unit = world.getUnit(UnitID.createUnitID(chefdiplomat,36));
  String factionString;
  String allianceId;
  List mitInfoListe = new ArrayList();
  List ohneInfoListe = new ArrayList();

  //magellan.library.utils.OrderedHashtable col = world.factions();
  for (Faction faction : world.factions().values()){
    AllianceGroup alliance = faction.getAlliance();
    if (alliance==null) allianceId = "?";
    else allianceId = alliance.getID().toString();
    if (outputType.equals("code")){
      factionString = "tmpCallback.put(\""+faction.getID().toString()+"\",\""+metaGetFriendFoeInfo(faction)+"\");/"+"/"+faction.getName();
    } else {
      factionString = ""+faction.getName()+","+faction.getID().toString();
      factionString = factionString + ","+allianceId+","+faction.getRace();
      factionString = factionString + ","+faction.getPersons()+","+faction.getRace();
      factionString = factionString + ","+faction.getSpellSchool()+","+faction.getScore();
    }
    unit.addOrderAt(0,factionString);
  }
  unit.addOrderAt(0,"/"+"/ TODO Factionliste rauskopieren");
}
```

To configure, you need another function in which each faction number that is to be assigned to a specific alliance has an assignment:

```java
metaFriendFoeCallback(HashMap tmpCallback){
  tmpCallback.put("ii","MOB"); // Monster
  return tmpCallback;
}
```

### Meta orders checker

This is also a little more complicated.
Is done using `metaCommandChecker("party#");` called.
This means that units get the lines `// m/abbauen/stein` or have also set the corresponding commands for iron or wood.

```java
/*********************************************
*        Meta's Command checker              *
* Version 0.6                                *
*********************************************/

metaBefehlChecker(String factionId){
  String metaPrefix = "/" + "/ m/"; // Otherwise there will be problems with comment characters
  List metaBefehlsListe; // Commands with "//m/"
  List genBefehlsListe; // Commands with " ;m"
  List tmpBefehlsListe; // Other Commands
  for (Region region : world.regions().values()) { //all regions
    for (Unit unit : region.units()) { // all units
      if (unit.getFaction().getID().toString().equals(factionId)) { //own units
        metaBefehlsListe = new ArrayList();// init for new unit
        genBefehlsListe = new ArrayList();// init for new unit
        tmpBefehlsListe = new ArrayList();// init for new unit
        for (String befehl : unit.getOrders()){
          if (befehl.startsWith(metaPrefix)){ // search metacommands
            metaBefehlsListe.add(befehl);
          } else if (!(befehl.endsWith(" ;m"))){ // cancel ungenerated commands
            tmpBefehlsListe.add(befehl);
          } // generated commands are removed -should be regenerated!
        }
        if (metaBefehlsListe.size()>0){ // unity with meta commands
          for (String befehl : metaBefehlsListe) { // Process meta commands
            if (befehl.startsWith("abbauen",5)){
              if (befehl.startsWith("eisen",13)) metaAbbauenSub (unit,befehl,genBefehlsListe,"Eisen","Bergbau",500);
              if (befehl.startsWith("stein",13)) metaAbbauenSub (unit,befehl,genBefehlsListe,"Steine","Steinbau",250);
              if (befehl.startsWith("holz",13)) metaAbbauenSub (unit,befehl,genBefehlsListe,"Holz","Holzfällen",250);
            }
          }
          unit.clearOrders();
          unit.addOrders(metaBefehlsListe);
          unit.addOrders(genBefehlsListe);
          unit.addOrders(tmpBefehlsListe);
          unit.setOrdersChanged(true); // but doesn't seem to work ;o(
          //unit.setOrdersConfirmed(true); //this will come as soon as the script is out of beta.
        }
      }
    }
  }
}

metaAbbauenSub (Unit unit, String befehl, List genBefehlsListe, String itemName,String skillName,int unterhaltSilber){
  boolean istAbbauMoeglich=true;
  int unitLevel = metaGetUnitSkillLevel(unit,skillName);
  int abbauMenge = (unit.getPersons() * (unitLevel + 1));
  if (itemName.equals("Holz")){//genug Baum+Schössling?
    int baum = metaGetRegionRessourceAmount(unit.getRegion(),"Bäume");
    int schoessling = metaGetRegionRessourceAmount(unit.getRegion(),"Schößlinge");
    if (baum+schoessling == 0) istAbbauMoeglich = false;
  } else { // Tiefencheck
    int ressLevel = metaGetRegionRessourceLevel(unit.getRegion(),itemName);
    int ressAmount = metaGetRegionRessourceAmount(unit.getRegion(),itemName);
    if (ressLevel > unitLevel) istAbbauMoeglich =false;//zu tief
    if (ressLevel == unitLevel) { // enough level still there?
      if (ressAmount < (abbauMenge/2)) { // half because of building
        istAbbauMoeglich = false; // per default wird mal nicht abgebaut
        genBefehlsListe.add("/" + "/ TODO abbauen/"+itemName+"/menge ;m"); // There is still something there, but not enough for maximum utilization
      }
    }
  }
  if (metaGetUnitItem(unit,"Silber")<unterhaltSilber) {
    if (istAbbauMoeglich==true){ // If dismantling is not possible anyway, then no silver check either
      genBefehlsListe.add("/" + "/ TODO abbauen/"+itemName+"/silber ;m"); // not enough silver for building maintenance
    }
    istAbbauMoeglich = false;
  }
  if (istAbbauMoeglich==true) {
    if (abbauMenge % 2 == 1) abbauMenge--; // precisely because of building savings
    genBefehlsListe.add("MACHEN "+abbauMenge+" "+itemName+" ;m");
  } else {
    genBefehlsListe.add("LERNEN "+skillName+" ;m");
    genBefehlsListe.add("BEZAHLEN NOT ;m");
  }
  if (itemName.equals("Eisen")){ // if Laen is degradable then Todo
    int laenLevel = metaGetRegionRessourceLevel(unit.getRegion(),"Laen");
    if (laenLevel <= unitLevel){
        genBefehlsListe.add("/" + "/ TODO abbauenTODO abbauen/"+itemName+"/laen ;m");
    }
  }
}

int metaGetUnitItem(Unit unit,String itemName){
  Item items = unit.getModifiedItem(new ItemType(StringID.create("Silber")));
  if (items==null) return 0; // nothing there!
  else return items.getAmount();
}

 int metaGetRegionRessourceLevel(Region region,String itemName){
   RegionResource regRess = region.getResource(new ItemType(StringID.create(itemName)));
   if (regRess==null) return 999; // nothing there!
   else return regRess.getSkillLevel();
 }

int metaGetRegionRessourceAmount(Region region,String itemName){
  RegionResource regRess = region.getResource(new ItemType(StringID.create(itemName)));
  if (regRess==null) return 0; // nothing there!
  else return regRess.getAmount();
}

int metaGetUnitSkillLevel(Unit unit, String skillName) { // actually copied from Helper
  Collection skills = unit.getSkills();
  if (skills != null) {
    for (Skill skill : skills) {
      if (skill.getSkillType().getName().equalsIgnoreCase(skillName))
        return skill.getLevel();
      }
    }
  return 0;
}
```

<!-- From [https://wiki.eressea.de/index.php?title=ExtendedCommands&oldid=5882] -->

<!-- TODO: add to magellan.md -->
<!-- [Magellan]: http://magellan-client.sf.net -->
[official site]: http://magellan.narabi.de/plugins_extcmds_en.php
