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

### Približna enakost:
Torej ponovimo od prej in vpeljimo približno enakost.
Recimo, da gledamo  nek tekst T, ki ima dolžino n = |T|. V tem tekstu iščemo vzorec P, ki ima dolžino |P| = m. 
Poglejmo si hkrati en ob drugem vzorec in nek podniz za katerega želimo izvedeti, koliko si je podoben z vzorcem. Vidimo, da so si kje kakšne črke različne. Torej kako bi definirali za koliko sta si podobna? 

Vpeljimo nekaj definicij distanc:
Hammingova distanca: Vzorec in podniz sta enake dolžine, gledamo koliko črk moramo zamenjati, da pridemo iz enega niza v drugega. Ena zamenjava črk naj ima ceno 1. Torej hočemo narediti oba niza enaka s čim nižjo ceno.

Kaj pa, če nas zanima tudi približnost, ko vzorec in podniz nista enake dolžine. Vpeljimo Levenshteinovo distanco.

Levenshteinova distanca: Tukaj bodo ceno 1 imeli poleg spreminjanja črk tudi vstavljanje in brisanje. Torej, oba niza bosta enaka, če pri enem npr. zbrišemo znak ali pa ga pri drugem dodamo. Torej iščemo najnižjo ceno, da oba niza postaneta enaka. To bi znalo pomeniti, da je distanca simetrična.

Poglejmo si za obe distanci: 

Pri spremembi črk: lahko spremenimo na enem nizu ali na drugem

dodajanje: Lahko na enem nizu dodamo ali pa na drugem izbrišemo. Obe operaciji imata ceno 1.

Torej to pomeni, da sta obe distanci, Hammingova kot tudi Levenshteinova simetrični. Kaj pa, če je vzorec popolnoma enak podnizu s katerim ga primerjamo. V tem primeru je cena 0, saj nam ni potrebno narediti nobene operacije. 

Še enkrat si poglejmo kako lahko vse te informacije združimo v nek bolj kompakten zapis:

Imamo razdaljo $d(x,y)$. Med dvema nizoma $x$ in $y$. Cena ene transformacije (torej recimo vstavljanja, bisanja ali spreminjanja), ki $x$ spremeni naj bo $\delta(x,y) = c$ (v našem primeru naj to pomeni eno vstavljanje, brisanje, spreminjanje s ceno $c = 1$, ki se izvede na $x$). Torej kot smo rekli, iščemo minimalno ceno, torej iščemo $\min \sum \delta(x,y)$, da bo naslednja operacija $\delta(x,y) = 0$, z drugimi besedami, da si bosta niza enaka. Tukaj tudi vidimo simetričnost, saj je $\delta(x,y) = \delta(y,x) = c$ (kot smo prej rekli recimo nekje vstavimo, drugje pa zbrišemo).

Združimo vse do česar smo v tem razdelku prišli: 

i) $d(x,y) \geq 0 \,\,\,$ in $\,\,\,(d(x,y) = 0 \iff x = y)$

ii) $d(x,y) = d(y,x)$ 

Mogoče nas to že na kaj spominja?

iii)$d(x,z) \leq d(x,y) + d(y,z)$

Lahko rečemo, da prostor nizov tvori metrični prostor. Torej imamo obe razdalji, tako Hammingovo kot Levenshteinovo definirano kot metriko.

Ceni, da preidemo iz enega niza v drugega lahko rečemo tudi št. napak, ki jih bomo označili s $k$. Koliko je nek niz napačen lahko nato pogledamo z razmerjem $\alpha = \frac{k}{m}$