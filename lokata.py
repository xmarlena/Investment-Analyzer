# Program obliczający wartość danej inwestycji.
# Wszystko na podstawie podanych wkładów, rat, rodzaju kapitalizacji, stóp procentowych itp.

import matplotlib.pyplot as plt     # tworzenie wykresów
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *               # dodawanie GUI
from functools import partial       # dodawanie argumentów do funkcji (używane przy Button z tkintera)
from pandas import DataFrame  # podstawa tworzenia wykresów


# stałe ułatwiające tworzenie okien
ODY = 30
ODX = 30
LDX = 300
czcionka_okno = ("Helvetica", 13)


def inwestycja(stopa, rata, kapitalizacje, lata, wp):
    # stopa - okresowa stopa procentowa
    # liczba_rat - całkowita liczba okresów kapitalizacji w roku
    # rata - okresowa wpłata
    # kapitalizacje - ilosc okresow w trakcie roku, kiedy odesetki beda kapitalizowane a rata wplacana
    # lata - liczba lat planowanej inwestycji
    # wp - wpłata początkowa

    stopa = stopa / (100 * kapitalizacje)  # zmienianie stopy z procentów na ułamek dziesiętny dla okresu
    lokata = [wp]

    for i in range(kapitalizacje * lata):
        nowa_wartosc = lokata[i] * (1 + stopa) + rata  # obl. najnowszego stanu lokaty
        lokata.append(round(nowa_wartosc, 2))  # dodanie nowego stanu lokaty do listy

    okresy = []
    for i in range(kapitalizacje * lata + 1):
        okresy.append("{:.2f}".format(i / kapitalizacje))

    return lokata, okresy


def lokata_wczytywanie(stopa, lata, rata, wp, kapitalizacja):
    try:
        global lokata_stopa, lokata_lata, lokata_rata, lokata_wp, lokata_kapitalizacje
        lokata_stopa = float(stopa.get())
        lokata_lata = int(lata.get())
        lokata_rata = int(rata.get())
        lokata_wp = int(wp.get())
        lokata_kapitalizacje = int(kapitalizacja.get())

    except ValueError as error:
        wyjatek("Niepoprawne dane wejściowe.", error)
    except Exception as error:
        wyjatek("Niespodziewany błąd", error)
    else:
        if lokata_lata == 0 or lokata_kapitalizacje == 0:
            wyjatek("Błąd programu.", "Podane lata i liczba kapitalizacji nie mogą wynosić 0.")
        elif lokata_kapitalizacje < 0 or lokata_wp < 0 or lokata_rata < 0 or lokata_lata < 0 or lokata_stopa < 0:
            wyjatek("Błąd programu.", "Podane parametry nie moga być ujemne.")
        else:
            global okno
            okno.destroy()


def wyw_wykres(okresy, lokata):
    global wyjscie
    wyjscie.destroy()

    okno_wykres = Tk()
    okno_wykres.title("Wykres")

    okresy = map(float, okresy)
    dane = {"Okres": okresy, "Zgromadzone fundusze": lokata}
    dane = DataFrame(dane)

    figura = plt.Figure(dpi=100)  # tworzenie figury, która będzie przechowywała wykres
    figura_wykres = figura.add_subplot()  # dodawanie wykresu do figury
    wykr = FigureCanvasTkAgg(figura, okno_wykres)
    wykr.get_tk_widget().pack()  # robienie z wykresu widżetu, pakowanie go

    dane = dane[["Okres", "Zgromadzone fundusze"]].groupby("Okres").sum()
    dane.plot(kind="line", legend="True", ax=figura_wykres, color="#ff0000", fontsize=10)

    figura_wykres.set_title("Fundusze zgromadzone w kolejnych okresach")
    figura_wykres.set_ylabel("Zaoszczędzona kwota")

    okno_wykres.mainloop()


def wyjatek(tekst, error):  # tworzenie okna wyjątku
    okno_wyjatku = Tk()
    okno_wyjatku.title("Błąd")
    okno_wyjatku.geometry("500x100")
    okno_wyjatku.config(bg="#777777")
    Label(okno_wyjatku, text=tekst, font=czcionka_okno, bg="#777777", fg="#E12120").place(x=30, y=30)
    Label(okno_wyjatku, text="Powód:", font=czcionka_okno, bg="#777777").place(x=30, y=60)
    Label(okno_wyjatku, text=error, font=czcionka_okno, bg="#777777").place(x=90, y=60)


def type_essa():  # f. testowa
    print("essa")


# --------------------------------------------------------------------------------------------------------------------

# właściwy program:
if __name__ == "__main__":  # unikam robienia rzeczy globalnie

    # tworzenie okna
    okno = Tk()
    okno.title("Lokata")
    okno.geometry("600x300")  # szerokość x wysokość
    okno.config(bg="#777777")

    # podpisy
    Label(okno, text="Stopa procentowa [%]", font=czcionka_okno, bg="#777777").place(x=ODX, y=ODY)
    Label(okno, text="Wysokość wpłat [zł]", font=czcionka_okno, bg="#777777").place(x=ODX, y=2 * ODY)
    Label(okno, text="Liczba kapitalizacji w roku", font=czcionka_okno, bg="#777777").place(x=ODX, y=3 * ODY)
    Label(okno, text="Lata oszczędzania", font=czcionka_okno, bg="#777777").place(x=ODX, y=4 * ODY)
    Label(okno, text="Wkład początkowy [zł]", font=czcionka_okno, bg="#777777").place(x=ODX, y=5 * ODY)

    # pola wejścia
    pole_stopa = Entry(okno, width=30, bg="#aaaaaa")
    pole_rata = Entry(okno, width=30, bg="#aaaaaa")
    pole_kapitalizacja = Entry(okno, width=30, bg="#aaaaaa")
    pole_lata = Entry(okno, width=30, bg="#aaaaaa")
    pole_wp = Entry(okno, width=30, bg="#aaaaaa")

    # wrzucanie argumentów do funkcji używając partial (command przy Button nie przyjmuje argumentów)
    wczytywanie = partial(lokata_wczytywanie, pole_stopa, pole_lata, pole_rata, pole_wp, pole_kapitalizacja)

    Button(okno, text="Zatwierdź", command=wczytywanie, bg="#888888").place(x=LDX, y=6 * ODY)

    # rozmieszczanie pól wejścia
    pole_stopa.place(x=LDX, y=ODY)
    pole_rata.place(x=LDX, y=2 * ODY)
    pole_kapitalizacja.place(x=LDX, y=3 * ODY)
    pole_lata.place(x=LDX, y=4 * ODY)
    pole_wp.place(x=LDX, y=5 * ODY)
    okno.mainloop()

    # obliczanie lokaty
    try:
        lista_lokata, lista_okresy = inwestycja(lokata_stopa, lokata_rata, lokata_kapitalizacje, lokata_lata, lokata_wp)
    except Exception as blad:
        wyjatek("Nastąpiło niespodziewane przerwanie programu.", blad)


    # -----------------------------------------------------------------------------------------------------

    # tworzenie pól wyjściowych:
    wyjscie = Tk()
    wyjscie.title("Oszczędności w kolejnych okresach")
    wyjscie.config(bg="#777777")

    # wrzucanie argumentów do funkcji używając partial (command przy Button nie przyjmuje argumentów)
    wykres = partial(wyw_wykres, lista_okresy, lista_lokata)
    przycisk_wykres = Button(wyjscie, text=" Wyświetl wykres ", command=wykres, bg="#888888")
    przycisk_wykres.pack()  # dodawanie przycisku wywołującego wykres

    ramka = Text(wyjscie, bg="#777777", font=czcionka_okno)
    ramka.insert(END, "Okres:    Zaoszczędzona kwota\n")  # dodanie nagłówka

    # dodawanie kolejnych lat (okresów) i odpowiadających kwot
    for x in range(lokata_kapitalizacje * lokata_lata + 1):
        ramka.insert(END, str(lista_okresy[x]) + ":      " + str(lista_lokata[x]) + "\n")
    ramka.pack()

    wyjscie.mainloop()
