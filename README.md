# Investment Analyzer (PL)

Program analizuje lokaty bankowe.

## Projekt składa się z 4 plików:
- **main.py** - główny plik, wywołujący kolejne,
- **lokata.py** - program obliczający wartość danej inwestycji,
- **kalkulator.py** - program obliczający stopę efektywna i nominalną,
- **banki.py** - program porównujący oferty wprowadzone do arkusza kalkulacyjnego.

Do poprawnego działania potrzebne są:
* tkinter (wszystkie programy)
* matplotlib (main.py, lokata.py)
* pandas (main.py, lokata.py, banki.py)
* functools (lokata.py, kalkulator.py)


## Działanie poszególnych programów:

### main.py:
Program służy do otwierania trzech pozostałych programów. Aby zapewnić poprawne działanie, wszystkie pliki projektu muszą znajdować się w jednym miejscu. W przeciwnym wypadku program może mieć problem z otworzeniem plików - wtedy należy w kodzie podać ich dokładną lokalizację na dysku.


### lokata.py:
Program przyjmuje od użytkownika wartości:
* stopa procentowa - nieujemny ułamek dziesiętny z kropką, bez znaku procentów (np. 7,5% -> 7.5);
* wysokość wpłat - nieujemna liczba całkowita, bez symbolu zł (np. 300 zł -> 300), wpłaty odbywają się raz w każdym okresie kapitalizacji;
* liczba kapitalizacji w roku - dodatnia liczba całkowita;
* lata oszczędzania - dodatnia liczba całkowita;
* wkład początkowy - nieujemna liczba całkowita, bez symbolu zł (np. 1000 zł -> 1000).
Jeżeli dane nie spełniają wymienionych wymogów, wyświetla się komunikat błędu.
W przeciwnym wypadku otwiera się okno wyjścia, gdzie wypisane są zaoszczędzone kwoty w każdym z okresów oszczędzania (1 pełen okres to rok). Istnieje możliwość wyświetlenia wykresu, pokazującego zależność między upływem czasu a zgromadzonymi funduszami.

### kalkulator.py:
Program przyjmuje od użytkownika wartości:
* stopa procentowa - stopa procentowa - nieujemny ułamek dziesiętny z kropką, bez znaku procentów (np. 7,5% -> 7.5);
* roczna liczba kapitalizacji - dodatnia liczba całkowita.
Użytkownik wybiera, czy chce daną liczbę przeliczyć ze stopy efektywnej na nominalną, czy na odwrót. W ekranie wyjściowym pojawiają się obie stopy - ta podana przez użytkownika oraz wyliczona przez program.

### banki.py:
Program pobiera dane z arkusza kalkulacyjnego online, w którym można dowolnie zmieniać informacje.  
Adres: **[LINK](https://docs.google.com/spreadsheets/d/1GMU80UGuh-kxdmzZYLPeOxcP5L86D3DTJf8Y2ZWUOnc/edit#gid=0)**   
Aby program zadziałał, arkusz musi mieć nagłówki: "Bank", "Oprocentowanie", "Kapitalizacje". Przy nazwach nie mogą znaleźć się żadne inne znaki, w tym spacje.   
Arkusz przechowuje nazwę banku, nominalną stopę procentową podaną w postaci ułamka dziesiętnego z kropką (np. 7,5% -> 0.075) oraz liczbę kapitalizacji w trakcie roku w postaci liczby całkowitej.
Następnie program dla podanych w arkuszu stóp nominalnych (te są domyślnymi podawanymi przez banki) oblicza stopy efektywne, tym samym pozwalając na porównanie skali zysków w ciągu roku.
