---
# cSpell:locale fr
alias: extended-commands-fr
---

# `Extended Commands`

`Extended Commands` est un plugin pour [Magellan][magellan-fr-id] inclus dans la distribution standard et permettant d'automatiser les ordres.  

Une introduction et quelques exemples de scripts sont disponibles sur le [site web officiel].  

La bibliothèque de scripts est accessible via le menu Magellan *`Plugins > Extended Commands > Edit Library...`*.  
Une nouvelle fenêtre s’ouvre sur le côté, proposant un champ de saisie pour renseigner le code, ainsi que des boutons d’exécution et d’enregistrement.  

Vous trouverez ci-dessous des exemples de méta-scripts.  

## Méta-scripts

En général, vous pouvez copier les scripts les uns après les autres, mais il est aussi possible de les diviser en quatre :

1. Importations : copie simplement deux lignes
2. Bibliothèque de fonctions : copie-colle
3. Configuration : cette étape nécessite une configuration manuelle
4. Appels : ici, vous pouvez configurer le comportement de chaque appel

Si vous souhaitez écrire votre propre code, vous trouveras toutes les informations nécessaires dans *`Desktop > Advanced Commands > Help.`*.  
Vous pouvez également consulter la page dans votre navigateur en cliquant sur le bouton « Navigateur ».  

Voici les deux lignes pour l'importation :

```java
import magellan.library.*;
import magellan.library.rules.*;
```

Ci-dessous vous trouverez mes scripts.  

### Méta-script de construction de château

En appelant `metaBurgenbauSchilder()` dans toutes les régions, vous recevrez un `Sign` avec les informations suivantes :

- Taille du château M Moral
- Argent par taille de château
- Pierres pour la prochaine amélioration du château
- Efficacité de la pierre (argent par taille de château / pierre pour la prochaine amélioration du château)

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

### Méta-script d'identification des armées

C'est un peu plus compliqué car cela nécessite une certaine configuration.  
Une documentation plus détaillée sera fournie ultérieurement :

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

### Vérificateur de méta-ordres

C'est un peu plus compliqué. Cela s'appelle `metaCommandChecker("faction#");`.
Cela garantit que les unités qui ont les lignes `// m/mine/stone` ou `// iron or wood` reçoivent les commandes correspondantes.

C'est un peu plus compliqué car cela nécessite une certaine configuration.
Une documentation plus détaillée sera fournie ultérieurement :

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

Pour configurer, vous avez besoin d'une autre fonction dans laquelle chaque identifiant e faction qui doit être attribué à une alliance spécifique a une affectation :

```java
metaFriendFoeCallback(HashMap tmpCallback){
  tmpCallback.put("ii","MOB"); // Monster
  return tmpCallback;
}
```

### Méta-script de vérification des ordres

C'est aussi un peu plus compliqué.  
Se fait en appelant `metaCommandChecker("party#");`.  
Cela signifie que les unités obtiennent les lignes `// m/abbauen/stein` ou avoir également défini les ordres correspondants pour le fer ou le bois.  

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

[site web officiel]: http://magellan.narabi.de/plugins_extcmds_en.php
