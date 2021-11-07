from tkinter import Canvas, Tk, Frame, Button, Widget, messagebox, filedialog, Scale, HORIZONTAL, ALL
import PIL.ImageGrab as ImageGrab

linea_x = 0
linea_y = 0
color = 'black'

def linea_xy(event):
    global linea_x
    global linea_y

    linea_x = event.x
    linea_y = event.y

def linea(event):
    global linea_x, linea_y
    canvas.create_line((linea_x, linea_y, event.x, event.y), fill = color, width = espesor_pincel.get())
    linea_x = event.x
    linea_y = event.y

def mostrar_color(nuevo_color):
    global color
    color = nuevo_color

def borrar():
    global color
    color = 'White'

def limpiar():
    canvas.delete(ALL)

def salir():
    ventana.destroy()
    ventana.quit()



ventana = Tk()
ventana.state =('zoomed')
ventana.config(bg='black')
ventana.title('Dibujar')
ventana.iconbitmap('icono_dibujo.ico')

ventana.rowconfigure(0,weight=1)
ventana.columnconfigure(0,weight=1)

# frame principal comandos y canvas de dibujo

frame = Frame(ventana, height=660, bg = 'white')
frame.grid(column = 0, row = 0, sticky = 'ew')

frame.columnconfigure(0, minsize=200, weight=1)

# canvas de dibujo
canvas = Canvas(ventana, height=660, bg= 'white')
canvas.grid(row=1, column=0, sticky='nsew')

canvas.rowconfigure(0,weight=1)
canvas.columnconfigure(0, weight=1, minsize=100)

canvas.bind('<Button-1>', linea_xy)
canvas.bind('<B1-Motion', linea)

# Canvas para colores

canvas_colores = Canvas(frame, bg='black', width=5, height=40)
canvas_colores.grid(column=0, row=0, sticky='ew', padx=1, pady=1)

id = canvas_colores.create_rectangle((10,10,30,30), fill = 'red')
canvas_colores.tag_bind(id, '<Button-1>', lambda x: mostrar_color('red'))




