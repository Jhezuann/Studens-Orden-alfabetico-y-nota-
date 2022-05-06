from tkinter import *
from ventana import Ventana


def main():
    wn = Tk()
    app = Ventana(780, 260, wn, "Alumnos")

    app.mainloop()


if __name__ == "__main__":
    main()
