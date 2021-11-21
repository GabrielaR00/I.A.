from tkinter import messagebox
import webbrowser
import speech_recognition as sr

from tkinter import *
from tkinter import colorchooser

from tkinter import Canvas, Tk, ttk, Frame, Button, Widget, filedialog, Scale, HORIZONTAL, ALL
import PIL.ImageGrab as ImageGrab
from tkinter.messagebox import *

reco= sr.Recognizer()

ventana = Tk()
ventana.title("Pixel Art 1.0")
ventana.configure(bd=10)

centro_x = 362
centro_y = 362

# frame principal comandos y canvas de dibujo

frameizquierda=Frame(ventana, height=500, width=200, bg = 'Gainsboro')
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

def pintar_pixel():
    global pixel
    pixel  = canvas.create_rectangle(centro_x, centro_y, centro_x+15, centro_y+15,fill='', outline='blue')  

def izquierda():
    global centro_x
    canvas.delete(pixel)
    centro_x-=15
    pintar_pixel()


def derecha():
    global centro_x
    canvas.delete(pixel)
    centro_x+=15
    pintar_pixel()

def arriba():
    global centro_y
    canvas.delete(pixel)
    centro_y-=15
    pintar_pixel()

def abajo():
    global centro_y
    canvas.delete(pixel)
    centro_y+=15
    pintar_pixel()

def color1():
    global centro_x, centro_y, item
    item  = canvas.create_rectangle(centro_x, centro_y, centro_x+15, centro_y+15) 
    canvas.itemconfigure(item, fill=color, outline=outline)
    

def color2():
    global centro_x, centro_y
    item  = canvas.create_rectangle(centro_x, centro_y, centro_x+15, centro_y+15, fill="Ghost White", width=1, outline="Gainsboro") 
    canvas.itemconfigure(item, fill="Ghost White", outline="Gainsboro")

def nuevo():
    cuadricula()

def mostrar_color(nuevo_color):
    global color, outline
    color = nuevo_color
    outline = nuevo_color
    
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

    id_verde = canvas_colores.create_rectangle((210,10,240,40), fill = 'green', outline="")
    canvas_colores.tag_bind(id_verde, '<Button-1>', lambda x: mostrar_color('green'))   

    id_amarillo = canvas_colores.create_rectangle((250,10,280,40), fill = 'yellow', outline="")
    canvas_colores.tag_bind(id_amarillo, '<Button-1>', lambda x: mostrar_color('yellow'))

    id_cafe = canvas_colores.create_rectangle((290,10,320,40), fill = 'brown', outline="")
    canvas_colores.tag_bind(id_cafe, '<Button-1>', lambda x: mostrar_color('brown'))    

    id_naranja = canvas_colores.create_rectangle((330,10,360,40), fill = 'orange', outline="")
    canvas_colores.tag_bind(id_naranja, '<Button-1>', lambda x: mostrar_color('orange'))
    
    id_rojo = canvas_colores.create_rectangle((370,10,400,40), fill = 'red', outline="")
    canvas_colores.tag_bind(id_rojo, '<Button-1>', lambda x: mostrar_color('red'))       

    id_magenta = canvas_colores.create_rectangle((410,10,440,40), fill = 'magenta', outline="")
    canvas_colores.tag_bind(id_magenta, '<Button-1>', lambda x: mostrar_color('magenta'))

    id_morado = canvas_colores.create_rectangle((450,10,480,40), fill = 'purple', outline="")
    canvas_colores.tag_bind(id_morado, '<Button-1>', lambda x: mostrar_color('purple'))   

color="Black"
outline = "Black"

def colorselec(pal):  
    global fill
    global outline     

   
    if pal==1:

        mostrar_color('white') 
             

    elif pal==2:

        mostrar_color('black')        
    
    elif pal==3:
        
        mostrar_color('grey')       

    elif pal==4:

        mostrar_color('blue')        

    elif pal==5:

        mostrar_color('cyan')        

    elif pal==6:

        mostrar_color('green')        

    elif pal==7:

        mostrar_color('yellow')        

    elif pal==8:

        mostrar_color('brown')          
    
    elif pal==9:

        mostrar_color('orange')      
    
    elif pal==10:

        mostrar_color('red')      

    elif pal==11: 

        mostrar_color('magenta')      

    elif pal==12:

        mostrar_color('purple')          
      

paleta()

def borrar():    
    item  = canvas.create_rectangle(centro_x, centro_y, centro_x+15, centro_y+15) 
    canvas.itemconfigure(item, fill='Ghost White', outline='Gainsboro')

def guardar():
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

def mensaje():
    DURATION = 2000
    top = Toplevel()
    top.title('Firulais')
    WELCOME_MSG = 'Has dicho: {}'.format(texto)
    Message(top, text = WELCOME_MSG, padx=20, pady=20).pack()
    top.after(DURATION, top.destroy)


def reconocimiento():
    global texto
    with sr.Microphone() as source: 
        print('Hola, soy tu asistente de voz')
        audio=reco.listen(source)

        try: 
            texto = reco.recognize_google(audio)
            texto = texto.lower()
            print ('Has dicho: {}'.format(texto))

            #canva_label = Canvas(frameizquierda)

            #scrollbar = Scrollbar(frameizquierda, orient="vertical", command=canva_label.yview)
            #scrollbar_frame = Scrollbar(canva_label)

            #canva_label((0,0), window = scrollbar_frame, anchor="nw")


            #canva_label.configure(yscrollcommand=scrollbar.set)
            #l_1 = Label(frameizquierda, text = 'Has dicho: {}'.format(texto))
            #l_1.pack()

            #messagebox.showinfo(title='Firulaiis', message='Has dicho: {}'.format(texto), padx=20,pady=20)

            mensaje()

            if "color" in texto:
                color1()
            if "fill" in texto:
                color1()
            if "borrar" in texto:
                borrar() 
            if "left" in texto:
                izquierda() 
            if "right" in texto:
                derecha() 
            if "down" in texto:  
                abajo() 
            if "above" in texto:
                arriba() 
            if "delete" in texto:
                borrar() 
            if "clean" in texto:
                nuevo() 
            if "save" in texto:
                guardar()
                
            #colores
            if 'White' in texto or 'white' in texto:
                 colorselec(1) 

            if "Black" in texto or "black" in texto:
                colorselec(2) 
            
            if "Gray" in texto or "gray" in texto:
                colorselec(3) 

            if "Blue"  in texto or "blue" in texto:
                colorselec(4)

            if "Aqua" in texto or "aqua" in texto:
                colorselec(5)
                
            if "Dark green" in texto or "dark green" in texto:
                colorselec()

            if "Green" in texto or "green" in texto:
                colorselec(6)

            if "Yellow" in texto or "yellow" in texto:
                colorselec(7)

            if "Brown" in texto or "brown" in texto:
                colorselec(8)            

            if 'Orange' in texto or 'orange' in texto:
                colorselec(9) 

            if "Ginger" in texto or "ginger" in texto:
                colorselec(10)

            if "Pink" in texto or "pink" in texto:
                colorselec(11)

            if "Purple" in texto or "purple" in texto:
                colorselec(12)

        except:
            print('No he entendido')

    ventana.after(3000,reconocimiento)

    
            

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

    boton5 = Button (framebotones, text="Arriba", height=2, cursor="hand2", command=arriba)
    boton5.pack(side="right", fill="both", expand=True)
    boton6 = Button (framebotones, text="Abajo", height=2, cursor="hand2", command=abajo)
    boton6.pack(side="right", fill="both", expand=True)

    boton7 = Button (framebotones, text="Derecha", height=2, cursor="hand2", command=derecha)
    boton7.pack(side="right", fill="both", expand=True)

    boton8 = Button (framebotones, text="Izquierda", height=2, cursor="hand2", command=izquierda)
    boton8.pack(side="right", fill="both", expand=True)

    boton9 = Button (framebotones, text="Pintar", height=2, cursor="hand2", command=color1)
    boton9.pack(side="right", fill="both", expand=True)

    boton10 = Button (framebotones, text="hablar", height=2, cursor="hand2", command=reconocimiento)
    boton10.pack(side="right", fill="both", expand=True)


botones()


def cuadricula():
    for y in range(2,750,15):
        for x in range (2,750,15):
            cua=canvas.create_rectangle(x, y, x+15, y+15, fill="Ghost White", width=1, outline="Gainsboro") 
            canvas.tag_bind(cua, '<Button-3>', color2)

cuadricula()
pintar_pixel()            


ventana.after(3000,reconocimiento)

ventana.mainloop()





