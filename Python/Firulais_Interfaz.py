from tkinter import *
from tkinter import colorchooser

from tkinter import Canvas, Tk, ttk, Frame, Button, Widget, messagebox, filedialog, Scale, HORIZONTAL, ALL
import PIL.ImageGrab as ImageGrab

ventana = Tk()
ventana.title("Pixel Art 1.0")
ventana.configure(bd=10)


# frame principal comandos y canvas de dibujo

frameizquierda=Frame(ventana, height=750, width=200, bg = 'Gainsboro')
frameizquierda.grid(column = 0, row = 0, sticky = 'n')

framederecha=Frame(ventana, height=750, width=750, bg = 'Gainsboro')
framederecha.grid(column = 1, row = 0, sticky = 'n')

frame = Frame(framederecha, height=70, width=700, bg = 'white')
frame.grid(column = 0, row = 1, columnspan= 2, pady=2, sticky = 'ew')
frame.columnconfigure(0, minsize=100, weight=5)

framebotones=Frame(framederecha, height=100, width=750, bg = 'Gainsboro')
framebotones.grid(column = 0, row = 2, columnspan=2, sticky ='ew')


#canvas 

canvas = Canvas (framederecha, width=750, height=750, bg="Gainsboro")
canvas.grid(column=0, row=0, columnspan=2)

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
    
color="Black"
def paleta():       

    canvas_colores = Canvas(frame, bg='gainsboro', width=700, height=70)
    canvas_colores.grid(column=0, row=0, sticky='ew', padx=2, pady=2)

    id_white = canvas_colores.create_rectangle((10,10,40,40), fill = 'white', outline="")
    canvas_colores.tag_bind(id_white, '<Button-1>', lambda x: mostrar_color('white'))

    id_negro = canvas_colores.create_rectangle((50,10,80,40), fill = 'black', outline="")
    canvas_colores.tag_bind(id_negro, '<Button-1>', lambda x: mostrar_color('black'))
    
    id_grey = canvas_colores.create_rectangle((90,10,120,40), fill = 'grey', outline="")
    canvas_colores.tag_bind(id_grey, '<Button-1>', lambda x: mostrar_color('grey'))

    id_azul = canvas_colores.create_rectangle((130,10,160,40), fill = 'blue', outline="")
    canvas_colores.tag_bind(id_azul, '<Button-1>', lambda x: mostrar_color('blue'))

    id_cyan = canvas_colores.create_rectangle((170,10,200,40), fill = 'cyan', outline="")
    canvas_colores.tag_bind(id_cyan, '<Button-1>', lambda x: mostrar_color('cyan'))

    id_verdeoscuro = canvas_colores.create_rectangle((210,10,240,40), fill = 'dark green', outline="")
    canvas_colores.tag_bind(id_verdeoscuro, '<Button-1>', lambda x: mostrar_color('dark green'))   

    id_verde = canvas_colores.create_rectangle((250,10,280,40), fill = 'green', outline="")
    canvas_colores.tag_bind(id_verde, '<Button-1>', lambda x: mostrar_color('green'))   

    id_amarillo = canvas_colores.create_rectangle((290,10,320,40), fill = 'yellow', outline="")
    canvas_colores.tag_bind(id_amarillo, '<Button-1>', lambda x: mostrar_color('yellow'))

    id_cafe = canvas_colores.create_rectangle((330,10,360,40), fill = 'brown', outline="")
    canvas_colores.tag_bind(id_cafe, '<Button-1>', lambda x: mostrar_color('brown'))    

    id_naranja = canvas_colores.create_rectangle((370,10,400,40), fill = 'orange', outline="")
    canvas_colores.tag_bind(id_naranja, '<Button-1>', lambda x: mostrar_color('orange'))
    
    id_rojo = canvas_colores.create_rectangle((410,10,440,40), fill = 'red', outline="")
    canvas_colores.tag_bind(id_rojo, '<Button-1>', lambda x: mostrar_color('red'))       

    id_magenta = canvas_colores.create_rectangle((450,10,480,40), fill = 'magenta', outline="")
    canvas_colores.tag_bind(id_magenta, '<Button-1>', lambda x: mostrar_color('magenta'))

    id_morado = canvas_colores.create_rectangle((490,10,520,40), fill = 'purple', outline="")
    canvas_colores.tag_bind(id_morado, '<Button-1>', lambda x: mostrar_color('purple'))   
      

paleta()


def borrar():
    global color
    color = 'White'

def guardar():
    try:
        filename = filedialog.asksaveasfilename(defaultextension='.png')

        x = ventana.winfo_rootx() + 210
        y = ventana.winfo_rooty() + 10

        print(x)
        print(y)
        print(canvas.winfo_x)
        print(canvas.winfo_y)


        x1 = x + canvas.winfo_width()
        y1 = y + canvas.winfo_height()

        ImageGrab.grab().crop((x, y, x1, y1)).save(filename)
        messagebox.showinfo('Guardar Dibujo','Imagen guardada en: ' + str(filename))
    except:
        messagebox.showerror('Guardar Dibujo', 'Imagen no guardada\n Error')
    
def botones():


    #framebotones.rowconfigure((0, 1), weight=1)
    boton2 = Button(framebotones, text="Guardar", height=2, cursor="hand2", command=guardar)
    #boton2.grid(column=0, row=0, sticky="EW")
    #framebotones.columnconfigure(0, weight=2)
    boton2.pack(side="right", fill="both", expand=True)
    boton3 = Button (framebotones, text="Limpiar", height=2, cursor="hand2", command=nuevo)
    #boton3.grid(column=1, row=0, sticky="EW")
    #framebotones.columnconfigure(1, weight=2)
    boton3.pack(side="right", fill="both", expand=True)
    boton4 = Button (framebotones, text="Borrador", height=2, cursor="hand2", command=borrar)
    #boton4.grid(column=2, row=0, sticky="EW")
    #framebotones.columnconfigure(2, weight=2)
    boton4.pack(side="right", fill="both", expand=True)



botones()


def cuadricula():
    for y in range(2,750,15):
        for x in range (2,750,15):
            cua=canvas.create_rectangle(x, y, x+15, y+15, fill="Ghost White", width=1, outline="Gainsboro") 
            canvas.tag_bind(cua, '<Button-1>', color1) 
            canvas.tag_bind(cua, '<Button-3>', color2)

cuadricula()

ventana.mainloop()