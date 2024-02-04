import pandas as pd
from tkinter import *

czcionka_okno = ("Helvetica", 13)


# tworzenie okna wyjątku
def wyjatek(tekst, error):
    okno_wyjatku = Tk()
    okno_wyjatku.title("Błąd")
    okno_wyjatku.geometry("500x100")
    okno_wyjatku.config(bg="#777777")
    Label(okno_wyjatku, text=tekst, font=czcionka_okno, bg="#777777", fg="#E12120").place(x=30, y=30)
    Label(okno_wyjatku, text="Powód:", font=czcionka_okno, bg="#777777").place(x=30, y=60)
    Label(okno_wyjatku, text=error, font=czcionka_okno, bg="#777777").place(x=90, y=60)
    okno_wyjatku.mainloop()


if __name__ == "__main__":
    # deklarowanie adresu + zmienianie formatu na csv
    sheet_url = "https://docs.google.com/spreadsheets/d/1GMU80UGuh-kxdmzZYLPeOxcP5L86D3DTJf8Y2ZWUOnc/edit#gid=0"
    url = sheet_url.replace("/edit#gid=", "/export?format=csv&gid=")

    # czytanie danych z podanego wczesniej adresu
    dane = pd.read_csv(url)

    # tworzenie listy nazw kolumn i oczekiwanej listy
    kolumny = []
    spodziewane_kolumny = ["Bank", "Oprocentowanie", "Kapitalizacje"]
    for col in dane.columns:
        kolumny.append(col)

    # sprawdzam, czy nazwy kolumn pokrywaja sie z planowanymi
    if kolumny != spodziewane_kolumny:
        wyjatek("Błąd programu", "Kolumny mają inne nazwy niż: \"Bank\", \"Oprocentowanie\", \"Kapitalizacje\"")

    # tworzenie okna wyjsciowego
    okno = Tk()
    okno.title("Porównanie banków")
    okno.config(bg="#777777")

    try:
        # próba obliczenia wartości stopy efektywnej
        dane.iloc[:, 1] = dane.iloc[:, 1].astype(float)
        dane["Efektywna"] = round(100 * ((1 + ((dane.iloc[:, 1]) / dane.iloc[:, 2])) ** dane.iloc[:, 2] - 1), 2)

    except Exception as blad:
        wyjatek("Wystapił błąd", blad)

    else:
        # tworzenie ramki, przechowującej kolejne linie wyjściowych danych
        ramka = Text(okno, bg="#777777", font=czcionka_okno)
        ramka.insert(END, "Bank:   oprocentowanie;   l. kapitalizacji w roku;   stopa efektywna\n\n\n")

        # robienie list z kolumn danych
        banki = dane.iloc[:, 0].tolist()
        opr = dane.iloc[:, 1].tolist()
        kapitalizacje = dane.iloc[:, 2].tolist()
        efektywne = dane.iloc[:, 3].tolist()

        # dodawanie danych wyjściowych
        for x in range(len(banki)):
            ramka.insert(END, str(banki[x]) + ":   " + str(round(opr[x] * 100, 2)) + "%;   " + str(kapitalizacje[x]) + ";   " + str(efektywne[x]) + "%\n\n")
        ramka.pack()

        # wywołanie okna
        okno.mainloop()
