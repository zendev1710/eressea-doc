---
# cSpell:locale fr
alias: envoi-des-ordres-depuis-magellan
---
# Envoi des ordres depuis Magellan

<!-- TODO: magellan screenshot 400X134 - should be where in the page ? -->
![Sending commands with Magellan using Gmail as an example](./assets/images/orders-sending-gmail.png "Sending commands with Magellan using Gmail as an example")

[[magellan]] offre la possibilité d'[[envoi-des-ordres|envoyer les ordres par email]] directement depuis le programme.  
L'avantage est d'éliminer le risque d'erreurs causées par la copie dans le programme de messagerie ou le webmailer.  

De plus, aucun formatage automatique n'est effectué que le serveur Eressea ne saurait comprendre, comme par exemple :

- un formatage HTML
- des sauts de ligne non désirés,
- des bannières automatiques
- l'encodage de caractères spéciaux, notamment les caractères avec trémas

Pour recevoir une copie de l'e-mail, vous pouvez envoyer une copie des ordres à votre propre adresse mél.  
Pour ce faire, vous devez effectuer les réglages appropriés dans Magellan, y compris la configuration du serveur SMTP du fournisseur de messagerie.  

Les données sont généralement obtenues grâce à l'aide du fournisseur, pour certaines, les données sont indiquées ci-dessous.  
De plus, le fournisseur peut devoir accorder explicitement une autorisation pour des programmes externes.  

## Dans Magellan

Pour définir la configuration pour l'envoi d'email, aller dans `File => Orders - dialog...`.  

<!-- cspell:disable -->
**Sender's address:** votre email  
**SMTP server:** celui du fournisseur de messagerie (voir ci-dessous)  
**Port:** celui du fournisseur de messagerie  
**Username:** votre nom d'utilisateur auprès du fournisseur de messagerie  
**Password:** votre mot de passe pour le fournisseur de messagerie, **pas** le mot de passe des ordres Eressea  
**Recipient address:** <eressea-server@eressea.kn-bremen.de>  
**Subject:** ERESSEA 2 ORDERS  
 **CC:** Facultatif, par exemple votre propre adresse  
**Copy to sender:** Envoie également les ordres à l'adresse de l'expéditeur  
**Use SSL/TLS:** cryptage des e-mails; doit être sélectionné si possible si c'est pris en charge par le fournisseur de messagerie (en cas de doute, essayez-le)  
**Use authentication:** habituellement nécessaire  
**always ask:** Demande le mot de passe du fournisseur de messagerie à chaque fois que vous envoyez l'e-mail, il n'est donc pas nécessaire de l'enregistrer dans Magellan  
**Use values from CR:** Remplit automatiquement l'adresse et le sujet du destinataire si les données sont dans le CR  
<!-- cspell:enable -->

Une fois les réglages effectués, vous pourrez envoyer directement l'e-mail avec `File => Orders - mail`.  

Pour certains fournisseurs de messagerie bien connus, voici les valeurs requises, telles que connues actuellement.

### GMX

Dans l'interface GMX, il sera nécessaire d’accorder une autorisation externe pour l'envoi d'email par une application tierce.
[Ce lien de support GMX] explique comment procéder.  

La configuration correspondante devrait ressembler à ceci :

<!-- TODO: frame surrrounding the image -->
![GMX - Autorisation](./img-gmx-enable-third-party-apps.png "Exemple de configuration d'autorisation dans GMX")

Pour pouvoir renseigner la bonne configuration dans Magellan, vous pouvez consulter les pages d'aide GMX suivantes :

- configuration du serveur SMTP : [support GMX - Serveur SMTP]
- autres paramètres SMTP : [support GMX - SMTP]

*Exemple de configuration GMX dans Magellan.*

<!-- TODO: frame surrrounding the image -->
![GMX - Configuration email](./img-gmx-email-settings.png "Exemple de configuration email GMX dans Magellan")

<!-- cspell:disable -->
**Sender's address:** votre adresse e-mail GMX (suffixée par @gmx.com)  
**SMTP server:** mail.gmx.com  
**Port:** 587 (avec TLS) ou 465 (avec SSL)  
**Username:** votre nom d'utilisateur GMX (soit votre adresse email GMX, soit votre identifiant)  
**Password:** votre mot de passe d'accès GMX (pas le mot de passe des ordres Eressea)  
**Use SSL:** cocher l'option (avec port 465, sinon non)  
**Use TLS:** cocher l'option (avec port 587, sinon non)  
**Use authentication:** cocher l'option  
<!-- cspell:enable -->

### Gmail

<!-- TODO: - should be where in the page ? -->
![Sending commands with Magellan using Gmail as an example](./assets/images/orders-sending-gmail.png "Sending commands with Magellan using Gmail as an example")

<!-- cspell:disable -->
**Sender's:** votre email sur Gmail  
**SMTP server:** smtp.googlemail.com  
**Port:** 465  
**Username:** votre nom d'utilisateur Gmail  
**Password:** votre mot de passe Gmail (pas le mot de passe des ordres Eressea)  
**Use SSL:** cocher l'option  
**Use TLS:** peu importe, les deux fonctionnent  
**Use authentication:** cocher l'option  
<!-- cspell:enable -->

!!! warning "Attention"
    À partir du 30 mai 2022 au plus tard, cela ne fonctionnera plus simplement avec le mot de passe Gmail ([applications non sécurisées et Gmail]).  
    Au lieu de cela, vous devez configurer ce que l'on appelle un mot de passe d'utilisation de l'application.  
    La documentation Gmail révèle plus de détails : [mot de passe de l'application et Gmail].  
    Au lieu du mot de passe Gmail, vous entrez simplement le mot de passe de l'application dans Magellan.  

### Freenet

<!-- cspell:disable -->
**Return address:** votre email Freenet  
**SMTP server:** mx.freenet.de  
**Port:** 587  
**Username:** votre nom d'utilisateur Freenet  
**Password:** votre mot de passe Freenet, **pas** le mot de passe des ordres Eressea  

**Use SSL:** oui  
**Use TLS:** oui  
**Use authentication:** oui  
<!-- cspell:enable -->

### Posteo

<!-- TODO: orders sending with Posteo 400X159 - should be where in the page ? -->
![Sending in commands with Magellan using Posteo as an example](./assets/images/orders-sending-posteo.png "Sending in commands with Magellan using Posteo as an example")

<!-- cspell:disable -->
**Return address:** votre email Posteo  
**SMTP server:** posteo.de  
**Port:** 465  
**Username:** votre email Posteo  
**Password:** votre mot de passe Posteo, **pas** le mot de passe des ordres Eressea  

**Use SSL:** oui  
**Use TLS:** oui  
**Use authentication:** oui  
<!-- cspell:enable -->

<!-- From [https://wiki.eressea.de/index.php?title=Befehle\_von\_Magellan\_verschicken&oldid=7407] -->

[Support GMX - SMTP]: https://support.gmx.fr/pop-imap/index.html
[Support GMX - Serveur SMTP]: https://support.gmx.fr/pop-imap/pop3/serverdata.html
[ce lien de support GMX]: https://support.gmx.fr/pop-imap/toggle.html
[applications non sécurisées et Gmail]: https://support.google.com/accounts/answer/6010255
[mot de passe de l'application et Gmail]: https://support.google.com/accounts/answer/185833
