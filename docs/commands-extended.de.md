---
# cSpell:locale de
alias: extendedcommands
---
# ExtendedCommands

ndedCommands sind ein Plugin für [Magellan], das im Standardlieferumfang enthalten ist und mit dem man Befehle automatisieren kann.

Auf der [offiziellen Seite] gibt es eine Einführung und ein paar Beispielscripte.

Die Script-Bibliothek versteckt sich im Magellan Menü: Plugins -&gt; Erweiterte Befehle -&gt; Bibliothek Bearbeiten... Es geht seitlich ein neuer View auf, mit einer grossen Textarea zum Code eingeben, sowie Buttons zum Ausführen und Speichern.

Was folgt sind Metas Beispielskripte. Einen anderen Ansatz verfolgen der E3CommandParser von Solthar.

## Metas Skripte

Generell kann man die Scripte einem nach dem anderen reinkopieren, aber ich hab es bei mir in 4 Teile aufgeteilt:

1. Imports: Nur 2 Zeilen reinkopieren.
2. Funktionenbibliothek: Einfach reinkopieren
3. Konfiguration: Hier muss man etwas Hand anlegen
4. Aufrufe: Da kann man halt jeweils einstellen was man tun will.

Wenn man selber was schreiben will findet man unter Desktop-&gt;Erweiterte Befehle Hilfe alles was man braucht. Mittels Button "Browser" kann man sich die Seite auch im Browser anzeigen lassen.

Achja, hier sind die 2 Zeilen für den Import:

    import magellan.library.*;
    import magellan.library.rules.*;

Hier sind meine vorgefertigten Scripts:

### Meta's BurgenbauSchilder

Ein Aufruf von `metaBurgenbauSchilder()` bekommt man in allen Regionen ein Schild mit folgenden Infos: Burggrösse M Moral Silber pro Burgengrösse / Stein für nächsten Burgupgrade Steineffizienz (=Silber pro Burgengrösse / Stein für nächsten Burgupgrade)

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
            if (building.getSize()>burggroesse){// TODO check ob Gebäude = Burg
              burggroesse = building.getSize();
            }
          }
          silberpool = region.getSilver();
          if (burggroesse<10) nextBurgUpgrade = 10;
          else if (burggroesse<50) nextBurgUpgrade = 50;
          else if (burggroesse<250) nextBurgUpgrade = 250;
          else if (burggroesse<1250) nextBurgUpgrade = 1250;
          else if (burggroesse<6250) nextBurgUpgrade = 6250;
          else nextBurgUpgrade = 0;//wird noch dauern bis ich es brauche
          stein2Upgrade = nextBurgUpgrade - burggroesse;
          steinEffizienz = silberpool/stein2Upgrade;
          signtext = ""+burggroesse+" M"+moral;
          region.addSign(new Sign( signtext ));
          signtext = ""+silberpool/100+"$/"+stein2Upgrade+"S";
          region.addSign(new Sign( signtext ));
          signtext = ""+steinEffizienz/100+","+steinEffizienz%100;//+"="+steinEffizienz;
          if (steinEffizienz>10000) signtext = "**" + signtext + "**";
          else if (steinEffizienz>1000) signtext = "*" + signtext + "*";
          region.addSign(new Sign( signtext ));
        }
      }
    }

### Meta's FreundFeindSchilder

Das ist etwas komplizierter, da es etwas an Konfiguration erfordert. Genauere Doku wird noch nachgeliefert:

    /*********************************************
    *        Meta's FreundFeindSchilder          *
    * Version 0.6                                *
    *********************************************/
    metaFreundFeindSchilder(String type) {
      if (type.equals("people")){//einfach nur Leute zählen
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
        for (Region region : world.regions().values()) {//alle Regionen
          people = new HashMap();
          soldiers = new HashMap();
          heros = new HashMap();
          for (Unit unit : region.units()) {//zusammenzaehlen
            friendFoeInfo = metaGetFriendFoeInfo(unit.getFaction());
            if (!(people.containsKey(friendFoeInfo))) {//wenn leer init
              people.put(friendFoeInfo,0);
            }
            if (!(soldiers.containsKey(friendFoeInfo))) {//wenn leer init
              soldiers.put(friendFoeInfo,0);
            }
            if (!(heros.containsKey(friendFoeInfo))) {//wenn leer init
              heros.put(friendFoeInfo,0);
            }
            if (!metaUnitIsSoldier(unit)){//keine Soldaten
              people.put(friendFoeInfo,people.get(friendFoeInfo)+unit.getPersons());
            } else if (unit.isHero()){//helden
              heros.put(friendFoeInfo,heros.get(friendFoeInfo)+unit.getPersons());
            } else {//soldaten
              soldiers.put(friendFoeInfo,soldiers.get(friendFoeInfo)+unit.getPersons());
            }
          }
          region.clearSigns();
          Iterator iterator = people.keySet().iterator();
          String signtext = "";
          while (iterator.hasNext()) {
            String ffi = iterator.next();//friendFoeInfo
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


    boolean metaUnitIsSoldier(unit) {//etwas gekürzt aus dem Helper
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

Zur Konfiguration braucht man noch eine weitere Funktion, in der jede Parteinummer die einem speziellen Allianz zugeteilt werden soll, eine Zuordnung:

    metaFriendFoeCallback(HashMap tmpCallback){
    tmpCallback.put("ii","MOB");//Monster
    return tmpCallback;
    }

### Meta's BefehlsChecker

Auch das ist etwas komplizierter. Wird mittels metaBefehlChecker("partei#"); aufgerufen. Dadurch bekommen Einheiten die die Zeilen `// m/abbauen/stein` bzw. auch für eisen oder holz gesetzt haben, die entsprechenden Befehle.

    /*********************************************
    *        Meta's BefehlsChecker               *
    * Version 0.6                                *
    *********************************************/

    metaBefehlChecker(String factionId){
      String metaPrefix = "/" + "/ m/"; //gibt sonst probleme mit Kommentarzeichen
      List metaBefehlsListe;// Befehle mit "// m/"
      List genBefehlsListe;// Befehle mit " ;m"
      List tmpBefehlsListe;//sonstige Befehle
      for (Region region : world.regions().values()) { //alle Regionen
        for (Unit unit : region.units()) { //alle Einheiten
          if (unit.getFaction().getID().toString().equals(factionId)) { //eigene Einheiten
            metaBefehlsListe = new ArrayList();//init fuer neue Einheit
            genBefehlsListe = new ArrayList();//init fuer neue Einheit
            tmpBefehlsListe = new ArrayList();//init fuer neue Einheit
            for (String befehl : unit.getOrders()){
              if (befehl.startsWith(metaPrefix)){//metaBefehle suchen
                metaBefehlsListe.add(befehl);
              } else if (!(befehl.endsWith(" ;m"))){//nichtgenerierte Befehle aufheben
                tmpBefehlsListe.add(befehl);
              } //generierte Befehle kommen weg - sollen neu generiert werden!
            }
            if (metaBefehlsListe.size()>0){ //einheit mit metaBefehlen
              for (String befehl : metaBefehlsListe) {//metaBefehle abarbeiten
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
              unit.setOrdersChanged(true); //scheint aber nicht zu funktionieren ;o(
              //unit.setOrdersConfirmed(true); //das kommt, sobald das Script aus der Beta ist.
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
      } else {//Tiefencheck
        int ressLevel = metaGetRegionRessourceLevel(unit.getRegion(),itemName);
        int ressAmount = metaGetRegionRessourceAmount(unit.getRegion(),itemName);
        if (ressLevel > unitLevel) istAbbauMoeglich =false;//zu tief
        if (ressLevel == unitLevel) {//genug in Ebene noch da?
          if (ressAmount < (abbauMenge/2)) {// halbe wegen Gebäude
            istAbbauMoeglich = false;//per default wird mal nicht abgebaut
            genBefehlsListe.add("/" + "/ TODO abbauen/"+itemName+"/menge ;m");//noch was da, aber nicht genug für maxauslastung
          }
        }
      }
      if (metaGetUnitItem(unit,"Silber")<unterhaltSilber) {
        if (istAbbauMoeglich==true){//wenn abbau eh nicht möglich, dann auch kein Silbercheck
          genBefehlsListe.add("/" + "/ TODO abbauen/"+itemName+"/silber ;m");//nicht genug Silber für Gebäudeunterhalt
        }
        istAbbauMoeglich = false;
      }    
      if (istAbbauMoeglich==true) {
        if (abbauMenge % 2 == 1) abbauMenge--;//gerade wegen Gebäudeeinsparung
        genBefehlsListe.add("MACHEN "+abbauMenge+" "+itemName+" ;m");
      } else {
        genBefehlsListe.add("LERNEN "+skillName+" ;m");
        genBefehlsListe.add("BEZAHLEN NICHT ;m");
      }
      if (itemName.equals("Eisen")){//wenn Laen abbaubar dann Todo
        int laenLevel = metaGetRegionRessourceLevel(unit.getRegion(),"Laen");
        if (laenLevel <= unitLevel){
            genBefehlsListe.add("/" + "/ TODO abbauenTODO abbauen/"+itemName+"/laen ;m");
        }
      }
    }

    int metaGetUnitItem(Unit unit,String itemName){
      Item items = unit.getModifiedItem(new ItemType(StringID.create("Silber")));
      if (items==null) return 0;//garnix da!
      else return items.getAmount();
    }

    int metaGetRegionRessourceLevel(Region region,String itemName){
      RegionResource regRess = region.getResource(new ItemType(StringID.create(itemName)));
      if (regRess==null) return 999;//garnix da!
      else return regRess.getSkillLevel();
    }

    int metaGetRegionRessourceAmount(Region region,String itemName){
      RegionResource regRess = region.getResource(new ItemType(StringID.create(itemName)));
      if (regRess==null) return 0;//garnix da!
      else return regRess.getAmount();
    }

    int metaGetUnitSkillLevel(Unit unit, String skillName) {//eigentlich aus Helper kopiert
      Collection skills = unit.getSkills();
      if (skills != null) {
        for (Skill skill : skills) {
          if (skill.getSkillType().getName().equalsIgnoreCase(skillName))
            return skill.getLevel();
          }
        }
      return 0;
    } 

<!-- From [https://wiki.eressea.de/index.php?title=ExtendedCommands&oldid=5882] -->

[Magellan]: http://magellan-client.sf.net
[offiziellen Seite]: http://magellan.narabi.de/plugins_extcmds_en.php
