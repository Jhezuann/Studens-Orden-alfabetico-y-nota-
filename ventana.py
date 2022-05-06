from cProfile import label
from tkinter import *
from tkinter import ttk

listaEstudiantes = []


class Ventana(Frame, object):

    def __init__(self, width: int, height: int,  master=None, title=""):

        self.master = master

        if self.master != None:
            self.master.title(title)

        self.title = title
        self.width = width
        self.height = height
        super().__init__(master, width=self.width, height=self.height)
        self.pack()

        self.EntryName = StringVar()
        self.EntryLastName = StringVar()
        self.EntryNote = IntVar()

        self.create_widgets(160, 260, "yellow")

    def orderNames(self):
        self.grid.delete(*self.grid.get_children())
        for index, (id, nombre, apellido, nota) in enumerate(sorted(listaEstudiantes, key=lambda x: x[1])):
            self.grid.insert("", index, text=id,
                             values=(nombre, apellido, nota))

    def orderNote(self, reverse=False):

        self.grid.delete(*self.grid.get_children())

        for index, (id, nombre, apellido, nota) in enumerate(sorted(listaEstudiantes, key=lambda x: x[3], reverse=reverse)):
            self.grid.insert("", index, text=id,
                             values=(nombre, apellido, nota))

    def refreshGrid(self):
        self.grid.delete(*self.grid.get_children())
        for index, (id, nombre, apellido, nota) in enumerate(listaEstudiantes):
            self.grid.insert("", index, text=id,
                             values=(nombre, apellido, nota))

    def guardar(self):
        id = len(listaEstudiantes) + 1
        nombre = self.EntryName.get()

        if nombre == "":
            return

        apellido = self.EntryLastName.get()
        if apellido == "":
            return

        nota = self.EntryNote.get()
        if nota == 0:
            return

        listaEstudiantes.append((id, nombre, apellido, nota))
        print(len(listaEstudiantes))
        self.refreshGrid()

    def create_widgets(self, width: int, height: int, bg="blue"):
        frame1 = Frame(self, bg=bg)
        frame1.place(x=0, y=0, width=width, height=height)

        ordenarPor = Label(frame1, text='Ordenar por:',
                           bg="yellow", fg="black")
        ordenarPor.place(x=45, y=10)

        self.bt1 = Button(frame1, text="Alfabetico",
                          command=self.orderNames, bg="white", fg="black")
        self.bt1.place(x=40, y=50, width=80, height=30)

        self.bt2 = Button(frame1, text="De merito(Mayor a menor)",
                          command=lambda: self.orderNote(reverse=True), bg="white", fg="black")
        self.bt2.place(x=5, y=100, width=150, height=30)

        self.bt3 = Button(frame1, text="De merito(Menor a mayor)",
                          command=lambda: self.orderNote(reverse=False), bg="white", fg="black")
        self.bt3.place(x=5, y=150, width=150, height=30)

        frame2 = Frame(self, bg="blue")
        frame2.place(x=165, y=0, width=200, height=height)

        label1 = Label(frame2, text='Nombre:', bg="blue", fg="white")
        label1.place(x=3, y=5)

        self.nombreCaja = Entry(frame2, textvariable=self.EntryName)
        self.nombreCaja.place(x=3, y=25, width=100, height=20)

        label2 = Label(frame2, text='Apellido:', bg="blue", fg="white")
        label2.place(x=3, y=60)

        self.apelldioCaja = Entry(frame2, textvariable=self.EntryLastName)
        self.apelldioCaja.place(x=3, y=80, width=100, height=20)

        label3 = Label(frame2, text='Nota:', bg="blue", fg="white")
        label3.place(x=3, y=115)

        self.notaCaja = Entry(frame2, textvariable=self.EntryNote)
        self.notaCaja.place(x=3, y=135, width=100, height=20)

        btGuardar = Button(frame2, text="Guardar",
                           command=self.guardar, bg="green", fg="white")
        btGuardar.place(x=60, y=210, width=60, height=30)

        self.grid = ttk.Treeview(self, columns=(
            "col1", "col2", "col3"))

        self.grid.column("#0", width=50)
        self.grid.column("col1", width=60, anchor=CENTER)
        self.grid.column("col2", width=60, anchor=CENTER)
        self.grid.column("col3", width=60, anchor=CENTER)

        self.grid.heading("#0", text="N°", anchor=CENTER)
        self.grid.heading("col1", text="Nombre", anchor=CENTER)
        self.grid.heading("col2", text="Apellido", anchor=CENTER)
        self.grid.heading("col3", text="Nota", anchor=CENTER)

        for (id, nombre, apellido, nota) in listaEstudiantes:
            self.grid.insert("", id, text=id, values=(
                nombre, apellido, nota))

        self.grid.place(x=370, y=0, width=420, height=260)
