from tkinter import *
import tkinter as tk
import sqlite3 
from tkinter import messagebox as MessageBox
raiz = Tk()
myframe = Frame(raiz, width = 800, height = 300)
raiz.geometry("280x160")
raiz.resizable(0,0)
myframe['bg'] = '#49A'
raiz['bg'] = '#49A'
myframe.pack()
raiz.title("CRUD PERSONAS")
c11 = StringVar()
c22 = StringVar()
c33 = StringVar()
c44 = StringVar()
c55 = StringVar()
def window (): 
       raiz.destroy() 
def borrar():
    c1.delete (0,"end")
    c2.delete (0,"end")
    c3.delete (0,"end")
    c4.delete (0,"end")
    c5.delete (0,"end")
def conec ():
    #from sqlite3.dbapi2 import Cursor
    conexion = sqlite3.connect ("BD")
    cursor = conexion. cursor ()
    try: 
        cursor.execute (''' CREATE TABLE PROD2 (ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE VARCHAR (20) , APELLIDOPAT VARCHAR (20), APELLIDOMAT VARCHAR (20), CONTRASEÑA VARCHAR (20)) ''') 
    except sqlite3.OperationalError:  
        MessageBox.showinfo("!Oh, no!", "La base de datos ha sido creada.")  
        conexion.commit ()
        conexion.close ()

def ins ():

   # from sqlite3.dbapi2 import Cursor
    conexion = sqlite3.connect ("BD")
    cursor = conexion. cursor ()

    cursor.execute ("INSERT INTO PROD2 VALUES (NULL, '" + c2.get()+
    "','"+ c3.get()+
    "','" +c4.get()+
    "','" +c5.get()+"')")

    conexion.commit ()
    conexion.close ()


Mymenu = tk.Menu(raiz)  
filemenu = tk.Menu(Mymenu, tearoff=0) 
Mymenu.add_cascade(label='BBDD', menu=filemenu)
filemenu.add_command(label='Conexión', command= conec)
filemenu.add_separator()
filemenu.add_command(label='Salir', command=window)
raiz.config(menu=Mymenu) 
editmenu = tk.Menu(Mymenu, tearoff=0)   
Mymenu.add_cascade(label='CRUD', menu=editmenu)  
editmenu.add_command(label='Crear',command= ins)
editmenu.add_command(label='Leer')
editmenu.add_command(label='Actualizar')
editmenu.add_command(label='Eliminar')
editmenu1 = tk.Menu(Mymenu, tearoff=0) 
Mymenu.add_cascade(label='Editar', menu=editmenu1)   
editmenu1.add_command(label='Borrar datos',command=borrar)
m1 = Label(myframe , text = "ID:")
m1.place(x = 107, y = 10)
m1.config (bg ='#49A',fg ='white')
m2 = Label(myframe , text="Nombre:")
m2.place(x = 75, y = 40)
m2.config (bg ='#49A',fg ='white')
m3 = Label(myframe , text = "Apellido Paterno:")
m3.place(x = 32, y = 70)
m3.config (bg ='#49A',fg ='white')
m4 = Label(myframe , text = "Apellido Materno:")
m4.place(x = 29, y = 100)
m4.config (bg ='#49A',fg ='white')
m5 = Label(myframe , text = "Contraseña:")
m5.place(x = 62, y = 130)
m5.config (bg ='#49A',fg ='white')
c1 = Entry(myframe, textvariable=c11 )
c1.place(x = 140, y = 10)
c2 = Entry(myframe, textvariable=c22 )
c2.place(x = 140, y = 40)
c3 = Entry(myframe, textvariable=c33 )
c3.place(x = 140, y = 70)
c4 = Entry(myframe, textvariable=c44 )
c4.place(x = 140, y = 100)
c5 = Entry(myframe, textvariable=c55 )
c5.place(x = 140, y = 130)
raiz.mainloop() 