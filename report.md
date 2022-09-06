Mijn superpy opdracht.

Ik heb de code zo ingericht dat er een scheiding is gemaakt tussen het aankopen van producten en het verkopen van producten. Bij het maken van een plan heb ik gebruik gemaakt van een flowchart met 4 verschillende swimming-lanes.

start van het programma
inkoop
verkoop
rapporten

De structuur van het programma is hetzelfde
main.py start het programma.
In de controllers staan de functies buy (inkoop) sold (verkoop ) profit(bereken van de winst) en een filecreater ( maakt lege files aan bij de start van het programma)
zodat die later niet meer gecheckt hoeven te worden.
De functies maken gebruik van de classes Product en Purchase.
Het programma word gestart door main.py start.
Hier worden alle files aangemaakt. Dit kan ook worden gebruikt om alles te resetten
Eerst moeten er producten worden toegeveoegd
Het programma houd rekening met de volgende:
Bestaat het product
Update aantal in voorraad zowel bij inkoop als verkoop
Update de status als verkoopdatum is verstreken zowel bij in als verkoop
product kan niet verkocht worden als er geen voorraad is.
Als de voorraad kleiner is dan het aantal gevraagde producten word er melding gemaakt van het aantal nog voorradige producten
Product kan niet verkocht worden als de verkoopdatum is versterken.
