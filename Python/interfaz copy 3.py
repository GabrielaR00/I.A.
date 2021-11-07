from tkinter import *
from tkinter import colorchooser

from tkinter import Canvas, Tk, ttk, Frame, Button, Widget, messagebox, filedialog, Scale, HORIZONTAL, ALL
import PIL.ImageGrab as ImageGrab

ventana = Tk()
ventana.title("Pixel Art 1.0")
ventana.configure (bd=10)

canvas = Canvas (ventana, width=701, height=701, bg="Gainsboro")
canvas.grid(column=0, row=0, columnspan=2)

# frame principal comandos y canvas de dibujo

# frame = Frame(ventana, height=70, width=700, bg = 'white')
# frame.grid(column = 0, row = 1, columnspan=2, pady=2, sticky = E+W)
# frame.columnconfigure(0, minsize=100, weight=5)



def color1(event):
    current = event.widget.find_withtag('current')
    item = current [0]
    canvas.itemconfigure(item, fill=color, outline=color)

def color2(event):
    current = event.widget.find_withtag('current')
    item= current [0]
    canvas.itemconfigure(item, fill="Ghost White", outline="Gainsboro")

def nuevo():
    cuadricula()

def mostrar_color(nuevo_color):
    global color
    color = nuevo_color
    
color="Blue Violet"
def paleta():   
    

    canvas_colores = Canvas(ventana, bg='grey', width=700, height=70)
    canvas_colores.grid(column=0, row=1, sticky='ew', padx=1, pady=1)

    id_rojo = canvas_colores.create_rectangle((10,10,730,30), fill = 'red')
    canvas_colores.tag_bind(id_rojo, '<Button-1>', lambda x: mostrar_color('red'))

    id_verde = canvas_colores.create_rectangle((40,10,60,30), fill = 'green')
    canvas_colores.tag_bind(id_verde, '<Button-1>', lambda x: mostrar_color('green'))

    id_amarillo = canvas_colores.create_rectangle((70,10,90,30), fill = 'yellow')
    canvas_colores.tag_bind(id_amarillo, '<Button-1>', lambda x: mostrar_color('yellow'))

    id_magenta = canvas_colores.create_rectangle((100,10,120,30), fill = 'magenta')
    canvas_colores.tag_bind(id_magenta, '<Button-1>', lambda x: mostrar_color('magenta'))

    id_azul = canvas_colores.create_rectangle((130,10,150,30), fill = 'blue')
    canvas_colores.tag_bind(id_azul, '<Button-1>', lambda x: mostrar_color('blue'))

    id_naranja = canvas_colores.create_rectangle((160,10,180,30), fill = 'orange')
    canvas_colores.tag_bind(id_naranja, '<Button-1>', lambda x: mostrar_color('orange'))

    id_morado = canvas_colores.create_rectangle((190,10,210,30), fill = 'purple')
    canvas_colores.tag_bind(id_morado, '<Button-1>', lambda x: mostrar_color('purple'))

    id_negro = canvas_colores.create_rectangle((220,10,240,30), fill = 'black')
    canvas_colores.tag_bind(id_negro, '<Button-1>', lambda x: mostrar_color('black'))

    # c = colorchooser.askcolor()
    # color = c[1]
   


def guardar():
    canvas.postscript (file="Pixel_art.eps")
    

boton2 = Button(ventana, text="Save", height=2, cursor="hand2", command=guardar)
boton2.grid(column=0, row=2, sticky=E+W)
boton3 = Button (ventana, text="New", height=2, cursor="hand2", command=nuevo)
boton3.grid(column=1, row=2, sticky=E+W)

def cuadricula():
    for y in range(2,700,15):
        for x in range (2,700,15):
            cua=canvas.create_rectangle(x, y, x+15, y+15, fill="Ghost White", width=1, outline="Gainsboro") 
            canvas.tag_bind(cua, '<Button-1>', color1) 
            canvas.tag_bind(cua, '<Button-3>', color2)

cuadricula()

ventana.mainloop()