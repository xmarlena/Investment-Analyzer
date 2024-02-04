# sekcja importu
from tkinter import *
from functools import partial

czcionka_okno = ("Helvetica", 13)


# funkcja wyznaczająca nominalną stopę procentową
def nom(efektywna, kapitalizacje):
    try:
        efektywna = float(efektywna.get())
        kapitalizacje = int(kapitalizacje.get())

    except ValueError as error:
        wyjatek("Niepoprawne dane wejściowe.", error)
    except Exception as error:
        wyjatek("Niespodziewany błąd", error)
    else:
        if kapitalizacje < 1 or efektywna < 0:
            wyjatek("Błąd programu.", "Podana stopa i liczba kapitalizacji muszą być dodatnie.")
        else:
            global gl_nominalna, gl_efektywna, okno
            gl_efektywna = efektywna
            efektywna = efektywna / 100
            gl_nominalna = (((efektywna + 1) ** (1 / kapitalizacje)) - 1) * kapitalizacje
            gl_nominalna = round(100 * gl_nominalna, 2)
            okno.destroy()

    # ((okresy)v(efektywna+1)-1)*okresy = nominalna
    # nominalna i efektywna to procenty zamienione na ułamki dziesiętne


# funkcja wyznaczająca efektywną
def ef(nominalna, kapitalizacje):
    try:
        nominalna = float(nominalna.get())
        kapitalizacje = int(kapitalizacje.get())

    except ValueError as error:
        wyjatek("Niepoprawne dane wejściowe.", error)
    except Exception as error:
        wyjatek("Niespodziewany błąd", error)
    else:
        if kapitalizacje < 1 or nominalna < 0:
            wyjatek("Błąd programu.", "Podana stopa i liczba kapitalizacji muszą być dodatnie.")
        else:
            global gl_nominalna, gl_efektywna
            gl_nominalna = nominalna
            nominalna = nominalna / 100
            gl_efektywna = (1 + (nominalna / kapitalizacje)) ** kapitalizacje - 1
            gl_efektywna = round(100 * gl_efektywna, 2)
            okno.destroy()


# tworzenie okna wyjątku
def wyjatek(tekst, error):
    okno_wyjatku = Tk()
    okno_wyjatku.title("Błąd")
    okno_wyjatku.geometry("500x100")
    okno_wyjatku.config(bg="#777777")
    Label(okno_wyjatku, text=tekst, font=czcionka_okno, bg="#777777", fg="#E12120").place(x=30, y=30)
    Label(okno_wyjatku, text="Powód:", font=czcionka_okno, bg="#777777").place(x=30, y=60)
    Label(okno_wyjatku, text=error, font=czcionka_okno, bg="#777777").place(x=90, y=60)


if __name__ == "__main__":

    # tworzenie pól wejściowych
    okno = Tk()
    okno.title("Kalkulator stóp procentowych")
    okno.geometry("600x300")
    okno.config(bg="#777777")
    Label(okno, text="Stopa procentowa: [%]", font=czcionka_okno, bg="#777777").place(x=30, y=30)
    Label(okno, text="Roczna liczba kapitalizacji: ", font=czcionka_okno, bg="#777777").place(x=30, y=60)
    Label(okno, text="Zamień na stopę:", font=czcionka_okno, bg="#777777").place(x=30, y=150)

    pole_stopa = Entry(okno, width=10, bg="#aaaaaa")
    pole_kap = Entry(okno, width=10, bg="#aaaaaa")
    pole_stopa.place(x=250, y=30)
    pole_kap.place(x=250, y=60)

    # łączenie funkcji z ich argumentami
    nomi = partial(nom, pole_stopa, pole_kap)
    efe = partial(ef, pole_stopa, pole_kap)

    Button(okno, text="nominalną", command=nomi, bg="#888888").place(x=200, y=130)
    Button(okno, text="efektywną ", command=efe, bg="#888888").place(x=200, y=170)

    okno.mainloop()

    # ----------------------------------------------------------------------------------------------------------------

    # tworzenie pól wyjściowych:
    try:
        wyjscie = Tk()
        wyjscie.geometry("300x100")
        wyjscie.title("Kalkulator stop procentowych")
        wyjscie.config(bg="#777777")
        Label(wyjscie, text="Stopa nominalna = ", font=czcionka_okno, bg="#777777").place(x=30, y=30)
        Label(wyjscie, text="Stopa efektywna = ", font=czcionka_okno, bg="#777777").place(x=30, y=60)
        Label(wyjscie, text=gl_nominalna, font=czcionka_okno, bg="#777777").place(x=200, y=30)
        Label(wyjscie, text=gl_efektywna, font=czcionka_okno, bg="#777777").place(x=200, y=60)

        wyjscie.mainloop()

    except Exception as blad:
        wyjatek("Wystapilo przerwanie programu", blad)
