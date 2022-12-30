# Struktura predstavitve: bitap algoritm
## Kazalo:
1. [Uvod](#uvod)
2. [String mathcing bitap](#String matching bitap:)
3. [Example](#example)
4. [Example](#example)
5. [Example](#example)

## Uvod  <a name="uvod"></a> :  
### (Naive matching algo, lahek primer.)
Prvo si bomo pogledali problem in nato iz tega problema postopoma prešli na bitap algoritem.

Začetni problem:
Recimo, da imamo podan nek tekst. V tem tekstu bi radi našli podniz, ki je enak nekemu vzorcu. Kako bi to naredili? Če si pogledamo naiven pristop: Naredimo zanko po tekstu. Za vsak znak v tekstu z zanko pogledamo čez vzorec, če se znaka ujemata.

## String matching bitap:
Rešitev za naš začetni problem lahko zelo izboljšamo. Tukaj bomo izrabili dejstvo bitnega paralelisma s katerim bomo lahko zgornji problem točnega iskanja niza zelo pohitrili.
Algoritmi kateri uporabljajo bitni paralelism se uporabljajo na naslednjih področjih: iskanje plagiarisma, rudarjenje podatkov, bioinformatiki (iskanje genov itd.),...

### Bitni paralelism:
Znake v vzorcu in v tekstu prevedemo v bitni zapis in nato operiramo nad tem bitnim zapisom. Zakaj je to hitrejše in kakšne so operacije. Besedo paralelizem si lahko predstavljamo kot neko vzporedno dogajanje. Torej kot že vemo, so dananšnji procesorji zmožni izvajanja več operacij vzporedno (paralelno). Enostaven primer bi bil seštevanje dveh 8 bitnih števil. Če imamo 16 bitni procesor nam lahko ta števila sešteje z eno operacijo. Če imamo večjederni procesor lahko naredimo naenkrat toliko takih računov, koliko imamo jeder.
