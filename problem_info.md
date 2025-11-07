## Úvod do sportovního sázení

Sportovní sázení je hra dvou hráčů: bookmakera a sázkaře.
Úlohou bookmakera je nabízet sázkařům příležitosti k sázkám s cílem maximalizovat svůj vlastní získ.
Blíží-li se tedy například nějaké basketbalové utkání dvou týmů, bookmaker vypíše tzv. kurzy na možné výsledky.
Sázkař si může zvolit, na které zápasy a výsledky by si chtěl vsadit.
V případě, že si sázkař vsadí na výsledek, který nastane, vyhrává sázkař vloženou sázku vynásobenou kurzem bookmakera.
Pokud daný výsledek nenastane, sázkař svou sázku prohrál.

**Příklad:**
Pro první zápas Vancouver - Nashville vypíše bookmaker kurzy 2.08 na výhru domácích (Vancouver) a 1.72 na vítězství Nashvillu.
Pro druhý zápas Anaheim - New Jersey vypíše bookmaker kurzy 1.19 na výhru Anaheimu a 4.55 na vítězství New Jersey.
Sázkař, který má k dispozici 1000 Kč, se rozhodne vsadit 100 Kč na vítězství domácího Vancouveru, tedy na kurz 2.08, a 50 Kč na vítězství hostujících z New Jersey, tedy na kurz 4.55. Po vsazení vkladů má na svém kontě 850 Kč. Předpokládejmě, že obě utkání skončí výhrou domácích, tedy Vancouveru a Anaheimu. Z prvního zápasu sázkař vyhrává 2.08 x 100 = 208 Kč. Sázka 50 Kč na druhý zápas propadá, jelikož vyhrál Anaheim a nikoliv New Jersey. Ve finále má sázkař na kontě 1058 Kč. 

## Zadání

Vaším úkolem bude naprogramovat co nejúspešnějšího sázkaře. V naší soutěži však nebude rozhodovat počet shlédnutých zápasů, nýbrž vaše schopnost navrhnout, implementovat a otestovat model, který se naučí predikovat výsledky nadcházejících zápasů z historických dat. 

Váš sázkař je reprezentován třídou [`Model`](src/model.py) s metodou `place_bets`, skrze kterou každý den, kdy jsou na trhu nějaké sázkařské příležitosti, obdržíte shrnutí, sázkařské příležitosti a inkrement dat. Od vás budeme očekávat sázky, které si přejete uskutečnit. Jelikož jednotlivé ročníky soutěží (sezóny) trvají několik měsíců, bude se váš model muset v průběhu sezóny adaptovat na nové výsledky a formu hráčů.

## Datové typy

V metodě `place_bets` se v jednotlivých argumentech setkáte celkem se čtyřmi datovými typy - `summary` obsahující [Summary DataFrame](#summary-dataframe), `opps` obsahující [Opps DataFrame](#opps-dataframe) a `inc` [Games DataFrame](#games-dataframe). Posledním pátým typem je odevzdávaný [Bets DataFrame](#bets-dataframe).

### Summary DataFrame

Summary dataframe obsahuje informace o současném stavu sázkařského prostředí. Dozvíte se v něm aktuální datum a jaké prostředky máte k dispozici.

|    |   Bankroll | Date       |   Min_bet |   Max_bet |
|---:|-----------:|:-----------|----------:|----------:|
|  0 |    1000    | 1993-11-06 |    1      |    100    |

<table>
<tr>
<td>

- **Bankroll** - Aktuální stav vašeho konta
- **Date** - Aktuální datum 
</td>
<td>

- **Min_bet** - Minimální možná nenulová sázka
- **Max_bet** - Maximální možná sázka
</td>
</tr>
</table>

### Opps DataFrame

Sázkařské příležitosti obsahují zápasy hrané v nadcházejících dnech. Příležitosti jsou platné do data konání zápasu (včetně). Je tedy možné vsadit na danou příležitost **vícekrát**. Vámi dříve vsazené částky budete mít k dispozici ve sloupcích `BetH`, `BetA` a `BetD`. Taktéž si povšimněte, že u zápasu s ID 21 je kurz na remízu `0.0`, což znamená, že v daný zápas nemůže skončit remízou.

| ID | Season |       Date | HID | AID | OddsH | OddsA |OddsD | BetH | BetA | BetD |
| -: | -----: | ---------: | --: | --: | ----: | ----: | ---: | ---: | ---: | ---: |
| 15 |  1993  | 1993-11-06 |  22 |  41 |  1.93 |  1.91 | 6.25 | 10.0 |  0.0 |  0.0 |
| 16 |  1993  | 1993-11-06 |  12 |  24 |  1.41 |  3.04 | 5.60 |  0.0 |  7.0 |  0.0 |
| 17 |  1993  | 1993-11-06 |   1 |  17 |  1.52 |  2.65 | 6.20 |  0.0 |  0.0 |  0.0 |
| 18 |  1993  | 1993-11-06 |   2 |  42 |  1.49 |  2.74 | 5.30 |  5.0 |  0.0 |  0.0 |
| 19 |  1993  | 1993-11-07 |  13 |  19 |  1.47 |  2.82 | 6.40 |  0.0 |  0.0 |  0.0 |
| 20 |  1993  | 1993-11-07 |  21 |  11 |  1.50 |  2.69 | 0.00 |  0.0 |  0.0 |  0.0 |

<table>
<tr>
<td>

- **ID** - Unikátní identifikátor zápasu (index tabulky)
- **Season** - Označení sezóny zápasu
- **Date** - Datum konání zápasu 
- **HID** - Unikátní identifikátor domácího týmu
- **AID** - Unikátní identifikátor hostujícího týmu

</td>
<td>

- **OddsH** - Kurz na výhru domácího týmu
- **OddsA** - Kurz na výhru hostujícího týmu
- **OddsD** - Kurz na remízu
- **BetH** - Vaše dřívější sázky na výhru domácího týmu
- **BetA** - Vaše dřívější sázky na výhru hostujícího týmu
- **BetD** - Vaše dřívější sázky na remízu

</td>
</tr>
</table>


### Inkrementální data
Inkrementální data obsahují výsledky a statistiky, které jste doposud neviděli. [Games DataFrame](#games-dataframe) obsahuje informace o parametrech odehraných zápasů. Počítejte s tím, že první inkrement který uvidíte, bude obsahovat i zápasy staršího data (z předcházejících sezón). 

#### Games DataFrame

|   ID | Season |       Date | HID | AID | OddsH | OddsA | OddsD |     H |     A |     D | HS | AS | Special | H_PEN | A_PEN | H_MAJ | A_MAJ | H_PPG | A_PPG | H_SHG | A_SHG | H_SV | A_SV | H_PIM | A_PIM | H_SOG | A_SOG | H_BLK_S | A_BLK_S | H_HIT | A_HIT | H_BLK | A_BLK | H_FO | A_FO | H_P1 | A_P1 | H_P2 | A_P2 | H_P3 | A_P3 | H_OT | A_OT | H_SO | A_SO |
| ---: | -----: | ---------: | --: | --: | ----: | ----: | ----: | ----: | ----: | ----: | -: | -: | ------: | ----: | ----: | ----: | ----: | ----: | ----: | ----: | ----: | ---: | ---: | ----: | ----: | ----: | ----: | ------: | ------: | ----: | ----: | ----: | ----: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 15 |   1993 | 1993-11-06 |  18 |   9 | 1.35 |  2.35 |   0.0 | False |  True | False |  5 |  6 |     |     3 |     5 |     0 |     0 |     1 |     3 |     0 |     1 |   23 |   41 |     6 |    10 |    46 |    28 |      15 |       2 |    14 |    17 |     1 |    12 |   50 |   28 |    2 |    2 |    1 |    3 |    2 |    0 |      |      |      |      |
| 16 |   1993 | 1993-11-06 |  22 |  20 | 1.41 |  2.14 |   0.0 |  True | False | False |  6 |  3 |         |     5 |     5 |     0 |     0 |     1 |     2 |     0 |     0 |   36 |   27 |    10 |    10 |    33 |    39 |      10 |       6 |    11 |    15 |     6 |     8 |   34 |   33 |    2 |    1 |    1 |    2 |    3 |    0 |      |      |      |      |
| 17 |   1993 | 1993-11-06 |  24 |   9 | 1.37 |  2.28 |   0.0 | False |  True | False |  3 |  4 |         |     9 |    11 |     0 |     0 |     3 |     0 |     0 |     1 |   21 |   34 |    18 |    22 |    37 |    25 |       8 |       4 |    21 |    19 |     4 |     8 |   34 |   29 |    2 |    2 |    0 |    2 |    1 |    0 |      |      |      |      |
| 18 |   1993 | 1993-11-06 |  10 |  18 | 1.43 |  2.09 |   0.0 |  True | False | False |  4 |  2 |         |     2 |     4 |     0 |     0 |     1 |     0 |     0 |     0 |   31 |   15 |     4 |     8 |    19 |    33 |      10 |      11 |     9 |    11 |    11 |    10 |   30 |   41 |    3 |    0 |    0 |    1 |    1 |    1 |      |      |      |      |
| 19 |   1993 | 1993-11-07 |   1 |   5 | 1.44 |  2.08 |   0.0 | False |  True | False |  1 |  2 |     |     7 |     7 |     2 |     1 |     1 |     1 |     0 |     0 |   26 |   33 |    34 |    24 |    34 |    27 |      14 |      11 |    13 |     7 |    10 |    14 |   35 |   31 |    0 |    1 |    0 |    0 |    1 |    0 |      |      |      |      |
| 20 |   1993 | 1993-11-07 |  15 |  19 | 1.84 |  1.55 |   0.0 | False |  True | False |  2 |  6 |         |    15 |    14 |     3 |     3 |     1 |     2 |     0 |     0 |   32 |   26 |    60 |    58 |    28 |    38 |       6 |      10 |    34 |    19 |    10 |     5 |   43 |   30 |    0 |    3 |    1 |    1 |    1 |    2 |      |      |      |      |


<table> <tr> <td>

**ID** - Unikátní identifikátor zápasu (index tabulky)

**Season** - Označení sezóny zápasu

**Date** - Datum konání zápasu

**HID** - Unikátní identifikátor domácího týmu

**AID** - Unikátní identifikátor hostujícího týmu

**OddsH** - Kurz na výhru domácího týmu

**OddsA** - Kurz na výhru hostujícího týmu

**OddsD** - Kurz na remízu

**H** - Přepínač, zda vyhrál domácí tým

**A** - Přepínač, zda vyhrál hostující tým

**D** - Přepínač, zda zápas skončil remízou

**HS** - Počet gólů domácího týmu

**AS** - Počet gólů hostujícího týmu

**Special** - Speciální příznak zápasu (prodloužení (OT), nájezdy (PS), kontumace(DW))

</td> <td>

**H_PEN** - Počet menších trestů (vyloučení) domácího týmu

**A_PEN** - Počet menších trestů (vyloučení) hostujícího týmu

**H_MAJ** - Počet vyšších trestů domácího týmu

**A_MAJ** - Počet vyšších trestů hostujícího týmu

**H_PPG** - Počet gólů domácího týmu v přesilovce

**A_PPG** - Počet gólů hostujícího týmu v přesilovce

**H_SHG** - Počet gólů domácího týmu v oslabení

**A_SHG** - Počet gólů hostujícího týmu v oslabení

**H_SV** - Počet zákroků brankáře domácího týmu

**A_SV** - Počet zákroků brankáře hostujícího týmu

**H_PIM** - Celkový počet trestných minut domácího týmu

**A_PIM** - Celkový počet trestných minut hostujícího týmu

**H_SOG** - Počet střel na branku domácího týmu

**A_SOG** - Počet střel na branku hostujícího týmu

**H_BLK_S** - Počet zblokovaných střel domácího týmu

**A_BLK_S** - Počet zblokovaných střel hostujícího týmu



</td> <td>

**H_HIT** - Počet hitů (body checků) domácího týmu

**A_HIT** - Počet hitů (body checků) hostujícího týmu

**H_BLK** - Počet bloků domácího týmu

**A_BLK** - Počet bloků hostujícího týmu

**H_FO** - Počet vyhraných vhazování domácího týmu

**A_FO** - Počet vyhraných vhazování hostujícího týmu

**H_P1** - Počet gólů domácího týmu v 1. třetině

**A_P1** - Počet gólů hostujícího týmu v 1. třetině

**H_P2** - Počet gólů domácího týmu v 2. třetině

**A_P2** - Počet gólů hostujícího týmu v 2. třetině

**H_P3** - Počet gólů domácího týmu v 3. třetině

**A_P3** - Počet gólů hostujícího týmu v 3. třetině

**H_OT** - Počet gólů domácího týmu v prodloužení

**A_OT** - Počet gólů hostujícího týmu v prodloužení

**H_SO** - Počet gólů domácího týmu v nájezdech

**A_SO** - Počet gólů hostujícího týmu v nájezdech

</td> </tr> </table>

### Bets DataFrame

Tento DataFrame očekáváme jako vaší odpověď z metody `place_bets`. I pokud nechcete pokládat žádné sázky, musíte poslat (alespoň prázdný) `DataFrame`.

| ID | BetH | BetA | BetD |
| -: | ---: | ---: | ---: |
| 15 | 10.0 |  0.0 |  0.0 |
| 16 |  0.0 |  7.0 |  0.0 |
| 17 |  0.0 |  0.0 |  0.0 |
| 18 |  5.0 |  0.0 |  0.0 |
| 19 |  0.0 |  0.0 |  0.0 |
| 20 |  0.0 |  0.0 |  0.0 |


- **ID** - Index odpovídajícího zápasu z [Opps DataFrame](#opps-dataframe) (index tabulky)
- **BetH** - Vaše sázky na výhru domácího týmu
- **BetA** - Vaše sázky na výhru hostujícího týmu
- **BetD** - Vaše sázky na remízu

## Technické náležitosti

- Veškerá data kolující mezi vaším modelem a bookmakerem jsou uložená v `pandas.DataFrame`.
- Komunikace mezi vámi a bookmakerem probíhá přes std in/out. Nemusíte se ničeho obávat, serializaci jsme vyřešili za vás, ale **raději se vyvarujte používání stdout v odevzdávaném řešení**.
- **Pokud bookmakerovi pošlete sázky na jiné příležitosti, než které vám přisly, budou ignorovány.**
- **Pokud nebudete mít dostatek prostředků pro vaše sázky, budou ignorovány.**
- **Sázky > max_bet a sázky < min_bet budou ignorovány.**

## Časté problémy

- Nejčastější chyba v upload systému je spojena s tím, že se váš kód v evaluační smyčce na hyperionu dostane do stavu, na který není připraven.
  - Například "RTE: KeyError" - zkontrolujte si zda je váš kód připravený na prázdný Dataframe příležitostí, nově se vyskytující ID týmu, apod.

Veškeré dotazy, problémy a náměty směřujte na qqh@fel.cvut.cz
