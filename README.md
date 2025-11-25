# Qminers Quant Hackathon 2025

Vítej na Qminers Quant Hackathonu!

V tomto repozitáři najdeš vše potřebné k odladění tvého modelu, aby Tě odevzdávací systém ničím nepřekvapil.

Odevzdávací systém beží na webu [hyperion.felk.cvut.cz](http://hyperion.felk.cvut.cz/).

## **Pozor nová úloha - Bookie Rookie**
### Mezi ostřílené bookmakery vstoupil nový hráč. Teprve se učí a jeho kurzy nejsou tak odladěné, dokážeš toho využít?
* `data/bookie_rookie_games.csv` obsahují trénovací data pro novou úlohu.
* V nové úloze se mění pouze částečně data, počateční kapitál a s ním i minimální a maximální sázka.
* Rookie bookmaker umožňuje sázet i na zápasy, kterým se ostřílený bookmaker raději vyhýbá.
* Počáteční kapitál: 100
* Minimální sázka: 1
* Maximální sázka: 20
* Struktura dat a vyhodnocovací smyčka zůtavají stejné jako v https://hyperion.felk.cvut.cz/problem/qqh25qual.
* Úloha je dostupná na https://hyperion.felk.cvut.cz/problem/qqh25qual2 a body z ní se počítají do kvalifikace QQH2025.
* K úloze je taktéž dostupná debug úloha https://hyperion.felk.cvut.cz/problem/qqh25debug2
* Získané body se počítají do kvalifikace QQH2025

### Neváhejte a sázejte i u nového bookmakera!

## Struktura repozitáře
* `problem_info.md` obsahuje detailní [zadání](problem_info.md) úlohy včetně popisu dat, které doporučujeme důkladně pročíst než se pustíš do tvorby vlastního modelu.
* `pyproject.toml` obsahuje `uv` prostředí jaké používá odevzdávací systém.
* `qqh-2025-env.yml` obsahuje `conda` prostředí jaké používá odevzdávací systém.
* `data/games.csv` obsahují trénovací data.
* `src/environment.py` obsahuje evaluační smyčku, která běží v odevzdávacím systému.
* `src/evaluate.py` skript pro spuštění lokáního vyhodnocení tvého modelu na trénovacích datech.
* `src/model.py` obsahuje ukázkový model s metodou `place_bets`.

## Runtime prostředí

Soubory `qqh-2025-env.yml` a `pyproject.toml` obsahují balíčky, které budou dostupné při evaluaci. Doporučujeme toto prostředí používat pro lokální vývoj za účelem zajištění spustitelnosti vašeho kódu. Pro instalaci můžete použít `conda` nebo `uv`.

**`conda` instalace**

1. Nainstaluj si nástroj miniconda: https://www.anaconda.com/docs/getting-started/miniconda/install#quickstart-install-instructions
2. Importuj environment: `conda env create -f qqh-2025-env.yml`
3. Aktivuj enviroment: `conda activate qqh-2025`

**`uv` instalace**

1. Nainstaluj si nástroj uv: https://docs.astral.sh/uv/getting-started/installation/
2. Importuj environment: `uv sync`
3. Aktivuj enviroment: `source .venv/bin/activate`

Vývojová prostředí (IDE) často umí s conda environmenty pracovat (například PyCharm či VS Code).

Pro ověření funčnosti můžeš rovnou spustit evaluaci modelu, který sází náhodně: `python src/evaluate.py`

## Vlastní řešení

Třída, kterou budeš odevzdávat do odevzdávacího systému, se musí jmenovat `Model` a musí obsahovat implementaci metody `place_bets(self, summary: pd.DataFrame, opps: pd.DataFrame, inc: pd.DataFrame)`. Ukázkový model náhodného sázkaře najdeš [zde](src/model.py).

Bližší info najdeš v [zadání](problem_info.md).

**Je zákázáno:**

- Používat k ladění modelů jakákoliv jiná než námi dodaná data.
- Spolupracovat s jinými týmy.
- Manipulovat s odevzdávacím systémem.
- Jakkoliv dolovat data z odevzdávacího systému.
- Spouštět vlastní procesy, komunikovat přes síť a vytvářet soubory v odevzdávacím systému mimo složku `/tmp`.

Porušení pravidel bude vést k vyloučení ze soutěže. Všechna odeslaná řešení se ukládají a mohou být zpětně přezkoumána.

## Evaluace

Evaluace v odevzdávacím systému probíhá na skrytých (validačních) datech. Trénovací data obsahují [zápasy](data/games.csv) ze sezón 1989/90-2010/11.
Validační data obsahují zápasy ze sezón 2011/12-2014/15.
V první iteraci [evaluační smyčky](src/environment.py#L68) obdržíš jako [inkrement](problem_info.md#dataframe-inkrement%C3%A1ln%C3%ADch-dat) všechna trénovací data.

V odevzdávacím systému budeš mít k dispozici pouze 1 cpu (1 vlákno) a 5 GB RAM. Současně může běžet pouze jedna evaluce tvého řešení.

Počet odevzdání je omezen, doporučujeme tedy kód pečlivě odladit na lokálním stroji.

V případě neúspěšného doběhnutí tvého programu se odevzdávací sytém pokouší napovědět příčinu pádu.

- `RTE` = Runtime Error. Nejčastěji kód spadnul na vyjímku, jejíž jméno ti odevzdávací systém (po rozkliknutí testcasu) ukáže. 
- `MLE` = Memory Limit Exceeded. Překročil jsi  pamětový limit. (Může být rozpoznáno jako RTE)
- `TLE` = Time Limit Exceeded. Překročil jsi časový limit.

