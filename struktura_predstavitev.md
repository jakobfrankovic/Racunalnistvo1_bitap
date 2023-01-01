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
Recimo, da imamo podan nek tekst. V tem tekstu bi radi izvedeli, kolikokrat se pojavi nek vzorec. Kako bi to naredili? Vemo, da je tekst dolžine $n$ in vzorec dolžine $m$. Vemo tudi, da je $n \ge m$. Če je vzorec prazen, ali če je $m \ge n$ vrnemo 0. Pogledajmo si naiven pristop: Naredimo zanko po tekstu. Za vsak znak v tekstu z drugo zanko pogledamo v vzorec, če se na naslednjem mestu znaka ujemata. 

Kakšna je časovna zahtevnost tega algoritma v najslabšem primeru? $(n * (n + 1)) / 2$
primer: 
        txt = "AAAAAAAAAAAAAAAAAA"
        pat = "AAAAA"

ali
        txt = "AAAAAAAAAAAAAAAAAB"
        pat = "AAAAB"

Kakšna je časovna zahtevnost v najboljšem primeru? 
        txt = "AABCCAADDEE"
        pat = "FAA"
Najboljši primer je, če prvega znaka vzorca ni v tekstu.
## String matching bitap:
Rešitev za naš začetni problem lahko zelo izboljšamo. Tukaj bomo izrabili dejstvo bitnega paralelisma s katerim bomo lahko zgornji problem točnega iskanja niza zelo pohitrili.
Algoritmi kateri uporabljajo bitni paralelism se uporabljajo na naslednjih področjih: iskanje plagiarisma, rudarjenje podatkov, bioinformatiki (iskanje genov itd.),...

### Bitni paralelism:
Znake v vzorcu in v tekstu prevedemo v bitni zapis in nato operiramo nad tem bitnim zapisom. Zakaj je to hitrejše in kakšne so operacije. Besedo paralelizem si lahko predstavljamo kot neko vzporedno dogajanje. Torej kot že vemo, so dananšnji procesorji zmožni izvajanja več operacij vzporedno (paralelno). Enostaven primer bi bil seštevanje dveh 8 bitnih števil. Če imamo 16 bitni procesor nam lahko ta števila sešteje v enem ciklu (enostavno:manj je ciklov, hitreje lahko izvedemo operacijo). Če imamo večjederni procesor lahko naredimo naenkrat toliko takih računov, koliko imamo jeder. Namesto računanja si sedaj lahko predstavljamo primerjanje znakov med vzorcem in podnizi iz teksta. 
Kako naredimo bitmask: Naredimo bitno reprezentacijo vzorca. Torej recimo, da imamo "ababaaa" Bomo naredili bitno masko za črko "b" in za črko "a". Prvo moramo vzorec gledati iz desne proti levi. Torej bomo imeli 1010111 in 0101000. 

Nato bomo imeli neko začetno stanje kjer bodo same enke. Šli bomo skozi tekst in shiftali v levo naše stanje, ki se bo za vsak znak spreminjalo. Če se bosta črki ujemali(tudi glede na zaporedje), se bo nicla shiftala v levo. Če se črki ujemata bomo videli preko OR operacije na obeh bitnih zapisih. (torej na zapisu stanja in zapisu bitmaska). Stanja si bomo vmes zapomnili. Če pride 0 čisto do leve, pomeni, da smo našli točno ujemanje. Za približno ujemanje pa moramo pogledati vmesna stanja, ki smo si jih zapomnili. Pred tem pa si poglejmo kdaj sta si dva niza priblizno enaka.