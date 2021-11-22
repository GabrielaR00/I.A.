import speech_recognition as sr

from tkinter import *
from tkinter import colorchooser

from tkinter import Canvas, Tk, ttk, Frame, Button, Widget, filedialog, Scale, HORIZONTAL, ALL
import PIL.ImageGrab as ImageGrab
import tkinter as tk
from tkinter.messagebox import *

from os import path

reco= sr.Recognizer()

ventana = Tk()
ventana.title("Firulais 1.0")
ventana.configure(bd=10)
ventana.iconbitmap(r"E:\\Documentos\\Gabs\\UMNG\\OCTAVO\\INTELIGENCIA ARTIFICIAL\\Firulais\\Python\\logo.ico")

centro_x = 362
centro_y = 362

# frame principal comandos y canvas de dibujo

frameizquierda=Frame(ventana, height=750, width=300, bg = 'Gainsboro')
frameizquierda.grid(column = 0, row = 0, sticky = 'n')


framederecha=Frame(ventana, height=750, width=750, bg = 'Gainsboro')
framederecha.grid(column = 1, row = 0, sticky = 'n')


#canvas 

canvas = Canvas (framederecha, width=750, height=750, bg="Gainsboro")
canvas.grid(column=0, row=0, columnspan=2)

#canvas iz
instruc= 'Instruc.png'
print(path.abspath(instruc))
render = tk.PhotoImage(file="E:\\Documentos\\Gabs\\UMNG\\OCTAVO\\INTELIGENCIA ARTIFICIAL\\Firulais\\Python\\Instruc.png")
canvas.create_image(0,0,anchor="nw", image=render)
img = Label(frameizquierda, image=render)
img.place(x=0, y=0)


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

        mostrar_color('dark orange')      
    
    elif pal==10:

        mostrar_color('red')      

    elif pal==11: 

        mostrar_color('deep pink')      

    elif pal==12:

        mostrar_color('purple')          
      



def exit():
    ventana.destroy()
    ventana.quit()

def borrar():    
    item  = canvas.create_rectangle(centro_x, centro_y, centro_x+15, centro_y+15) 
    canvas.itemconfigure(item, fill='Ghost White', outline='Gainsboro')

def guardar():
    try:
        filename = filedialog.asksaveasfilename(defaultextension='.png')

        x = ventana.winfo_rootx() + 310
        y = ventana.winfo_rooty() + 10

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
        print('Hola soy Firulais, tu asistente de voz')
        audio=reco.listen(source)

        try: 
            texto = reco.recognize_google(audio)
            texto = texto.lower()
            print ('Has dicho: {}'.format(texto))

            mensaje()

            if "color" in texto or "paint" in texto or "full" in texto or "pack" in texto:
                color1()
            if "left" in texto:
                izquierda() 
            if "right" in texto:
                derecha() 
            if "down" in texto:  
                abajo() 
            if "above" in texto or "up" in texto:
                arriba() 
            if "delete" in texto:
                borrar() 
            if "clean" in texto:
                nuevo() 
            if "save" in texto or "keep" in texto:
                guardar()
            if "exit" in texto:
                exit()
                
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
            DURATION = 2000
            top = Toplevel()
            top.title('Firulais')
            WELCOME_MSG = 'No he entendido'
            Message(top, text = WELCOME_MSG, padx=10, pady=10).pack()
            top.after(DURATION, top.destroy)
            

    ventana.after(3000,reconocimiento)

    
            

def cuadricula():
    for y in range(2,750,15):
        for x in range (2,750,15):
            cua=canvas.create_rectangle(x, y, x+15, y+15, fill="Ghost White", width=1, outline="Gainsboro") 
            canvas.tag_bind(cua, '<Button-3>', color2)

cuadricula()
pintar_pixel()            


ventana.after(3000,reconocimiento)

ventana.mainloop()





