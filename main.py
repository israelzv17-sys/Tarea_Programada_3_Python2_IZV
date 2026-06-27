import os
from PIL import Image
from PIL import ImageDraw
from xlsxwriter import Workbook

#Para calcular las nuevas dimensiones manteniendo la relación de las imagenes
def calcular_resize(ancho_original, alto_original, ancho_deseado=None, alto_deseado=None):
    """Calcular las nuevas dimensiones de una imagen manteniendo su proporción.

    Esta función permite redimensionar una imagen especificando ya sea el
    ancho deseado o el alto deseado. Si se proporciona uno de los dos, el
    valor restante se calcula automáticamente para conservar la relación de
    aspecto original.

    :param ancho_original: Ancho original de la imagen en píxeles.
    :type ancho_original: int
    :param alto_original: Alto original de la imagen en píxeles.
    :type alto_original: int
    :param ancho_deseado: Ancho deseado para la nueva imagen, si aplica.
    :type ancho_deseado: int | None
    :param alto_deseado: Alto deseado para la nueva imagen, si aplica.
    :type alto_deseado: int | None
    :return: Una tupla con las nuevas dimensiones ``(ancho, alto)`` o ``None``
        si no se especificó ningún valor de redimensionamiento.
    :rtype: tuple | None
    """

    if ancho_deseado == None and alto_deseado == None:
        return None
    
    if ancho_deseado != None:

        relacion = alto_original / ancho_original
        alto_deseado = ancho_deseado * relacion
        alto_deseado = int(alto_deseado)            

    elif alto_deseado != None:
        
        relacion = ancho_original / alto_original
        ancho_deseado = alto_deseado * relacion
        ancho_deseado = int(ancho_deseado)

    return (ancho_deseado, alto_deseado)

if __name__ == '__main__':

    nombres_imagenes=os.listdir("Imagenes Tarea 2") #Para obtener los nombres de la carpeta que almacena las imagenes
    lista=[]
    #Recorre la lista con los nombres de las imagenes
    for nombre in nombres_imagenes: 
        if nombre.endswith(".jpg") or nombre.endswith(".png"): #Para procesar solo imagenes JPG y PNG
            ruta=f"Imagenes Tarea 2/{nombre}"
            imagen=Image.open(ruta)

            tupla=()
            if imagen.size[1]>800 and imagen.size[1]>=imagen.size[0]:
                tupla=(nombre,imagen.format,imagen.size[0],imagen.size[1],"Procesada") #Toma los datos para el reporte
                
                nuevas_dimensiones=calcular_resize(imagen.size[0], imagen.size[1],None,800) #Para redimensionar la imagen
                imagen = imagen.resize(nuevas_dimensiones)
                
                imagen= imagen.convert("L") #Aplica escala grises
            
                draw = ImageDraw.Draw(imagen) #Aplica una marca de agua de texto
                texto = "Firma empresa"
                posicion = (10, 10)
                draw.text(posicion, texto)
                
                imagen.save(f"Imagenes procesadas/{nombre}") #Guarda la imagen en la carpeta definida

            elif imagen.size[0]>800 and imagen.size[0]>=imagen.size[1]:
                tupla=(nombre,imagen.format,imagen.size[0],imagen.size[1],"Procesada") 
            
                nuevas_dimensiones=calcular_resize(imagen.size[0], imagen.size[1], 800)
                imagen = imagen.resize(nuevas_dimensiones)
                
                imagen= imagen.convert("L") 
                
                draw = ImageDraw.Draw(imagen) 
                texto = "Firma empresa"
                posicion = (10, 10)
                draw.text(posicion, texto)
                
                imagen.save(f"Imagenes procesadas/{nombre}")      

            elif imagen.size[0]<=800 and imagen.size[1]<=800:
                tupla=(nombre,imagen.format,imagen.size[0],imagen.size[1],"Procesada")
            
                imagen= imagen.convert("L") 
                
                draw = ImageDraw.Draw(imagen)
                texto = "Firma empresa"
                posicion = (10, 10)
                draw.text(posicion, texto)
                
                imagen.save(f"Imagenes procesadas/{nombre}")
            lista.append(tupla) #Agrega los datos a la lista para luego usarlos en el reporte
        
        else:
            print(f"El archivo {nombre} no es una imagen del formato .jpg o .png")
        
    
    #Generación del reporte para Excel

    reporte = Workbook("reporte_imagenes.xlsx") #Crear el archivo Excel y encabezados de las columnas
    hoja1= reporte.add_worksheet("Resumen")
    hoja1.write(0,0, "Nombre del archivo original")
    hoja1.write(0,1, "Formato de la imagen")
    hoja1.write(0,2, "Ancho original")
    hoja1.write(0,3, "Alto original")
    hoja1.write(0,4, "Estado")

    indice_fila=1

    for dato in lista: #Para recorrer la lista con datos y escribirlos en el Excel
        hoja1.write(indice_fila, 0, dato[0])
        hoja1.write(indice_fila, 1, dato[1])    
        hoja1.write(indice_fila, 2, dato[2])
        hoja1.write(indice_fila, 3, dato[3])
        hoja1.write(indice_fila, 4, dato[4])

        indice_fila += 1


    reporte.close()