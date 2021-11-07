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

def guardar_dibujo():
    
    try:
        filename = filedialog.asksaveasfilename(defaultextension='.png')

        x = ventana.winfo_rootx() + canvas.winfo_x()
        y = ventana.winfo_rooty() + canvas.winfo_y()

        x1 = x + canvas.winfo_width()
        y1 = y + canvas.winfo_height()

        ImageGrab.grab().crop((x, y, x1, y1)).save(filename)
        messagebox.showinfo('Guardar Dibujo','Imagen guardada en: ' + str(filename))
    except:
        messagebox.showerror('Guardar Dibujo', 'Imagen no guardada\n Error')



ventana = Tk()
ventana.state =('zoomed')
ventana.config(bg='black')
ventana.title('Dibujar')
#ventana.iconbitmap('icono_dibujo.ico')

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
canvas.bind('<B1-Motion>', linea)

# Canvas para colores

canvas_colores = Canvas(frame, bg='black', width=5, height=40)
canvas_colores.grid(column=0, row=0, sticky='ew', padx=1, pady=1)

id_rojo = canvas_colores.create_rectangle((10,10,30,30), fill = 'red')
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

# espesor pincel

espesor_pincel = Scale(frame, orient= HORIZONTAL, from_= 0 , to=50, length=200, relief= 'groove', bg='gold', width=17, sliderlength=20, highlightbackground='white', activebackground='red')
espesor_pincel.set(1)
espesor_pincel.grid(column=1, row=0, sticky='ew', pady=1, padx=2)

bt_guardar = Button(frame, text = 'Guardar', bg='green2', command = guardar_dibujo, width=10, height=2, activebackground='white', font=('Comic sens MS', 10, 'bold'))
bt_guardar.grid(column=2, row=0, sticky= 'ew', pady=1, padx=4)

bt_borrar = Button(frame, text = 'Borrar', bg='cyan2', command = borrar, width=10, height=2, activebackground='white', font=('Comic sens MS', 10, 'bold'))
bt_borrar.grid(column=3, row=0, sticky= 'ew', pady=1, padx=4)

bt_limpiar = Button(frame, text = 'Limpiar', bg='violet red', command = limpiar, width=10, height=2, activebackground='white', font=('Comic sens MS', 10, 'bold'))
bt_limpiar.grid(column=4, row=0, sticky= 'ew', pady=1, padx=4)

bt_salir = Button(frame, text = 'Salir', bg='firebrick1', command = salir, width=10, height=2, activebackground='white', font=('Comic sens MS', 10, 'bold'))
bt_salir.grid(column=5, row=0, sticky= 'ew', pady=1, padx=4)



ventana.mainloop()




