from tkinter import *

# importy potrzebne, by lokata.py zadziałała
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def wyjatek(tekst, error):  # tworzenie okna wyjątku
    okno_wyjatku = Tk();
    okno_wyjatku.title("Błąd");
    okno_wyjatku.geometry("500x100");
    okno_wyjatku.config(bg="#777777")
    Label(okno_wyjatku, text=tekst, font=czcionka_okno, bg="#777777", fg="#E12120").place(x=30, y=30)
    Label(okno_wyjatku, text="Powód:", font=czcionka_okno, bg="#777777").place(x=30, y=60)
    Label(okno_wyjatku, text=error, font=czcionka_okno, bg="#777777").place(x=90, y=60)


# otwieranie programu lokata
def lokata():
    try:
        program.destroy()
        with open("lokata.py", encoding="utf-8") as lokata:
            exec(lokata.read())
    except Exception as blad:
        wyjatek("Nie udało się uruchomić programu lokata", blad)


# otwieranie programu kalkulator
def kalkulator():
    try:
        program.destroy()
        with open("kalkulator.py", encoding="utf-8") as kalkulator:
            exec(kalkulator.read())
    except Exception as blad:
        wyjatek("Nie udało się uruchomić programu kalkulator", blad)


# otwieranie programu banki
def banki():
    try:
        program.destroy()
        with open("banki.py", encoding="utf-8") as banki:
            exec(banki.read())
    except Exception as blad:
        wyjatek("Nie udało się uruchomić programu lokata", blad)


czcionka_okno = ("Helvetica", 13)


# tworzenie interfejsu graficznego
if __name__ == "__main__":
    program = Tk()
    program.title("Lokata")
    program.geometry("650x300")  # szerokość x wysokość
    program.config(bg="#777777")

    Label(program, text="Program obliczający wartość danej inwestycji.", font=czcionka_okno, bg="#777777").place(x=100, y=30)
    Label(program, text="Program obliczający stopę efektywną i nominalną.", font=czcionka_okno, bg="#777777").place(x=100, y=90)
    Label(program, text="Program porównujący oferty wprowadzone do arkusza kalkulacyjnego.", font=czcionka_okno, bg="#777777").place(x=100, y=150)

    Button(program, text="Lokata      ", command=lokata, bg="#888888").place(x=30, y=30)
    Button(program, text="Kalkulator", command=kalkulator, bg="#888888").place(x=30, y=90)
    Button(program, text="Banki        ", command=banki, bg="#888888").place(x=30, y=150)

    program.mainloop()
