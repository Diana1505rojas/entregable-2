import os
import pydicom
import matplotlib.pyplot as plt

# Directorio de imágenes DICOM
directorio_dicom = r"C:\Users\Sofia Rojas\Desktop\entregable2\imagenes"

# Lista para almacenar los datos de las imágenes DICOM
imagenes_dicom = []

# Iterar sobre los nombres de archivo de las imágenes en orden de 1 a 20
for i in range(1, 21):
    # Formatear el número de imagen con ceros a la izquierda
    numero_imagen = f"{i:06d}"
    
    # Nombre de archivo de la imagen actual
    nombre_archivo = f"image-{numero_imagen}.dcm"  
    
    # Ruta completa de la imagen
    ruta_imagen = os.path.join(directorio_dicom, nombre_archivo)
    
    # Verificar si el archivo existe
    if os.path.isfile(ruta_imagen):
        # Cargar la imagen DICOM y agregarla a la lista
        ds = pydicom.dcmread(ruta_imagen)
        imagenes_dicom.append(ds)
    else:
        print(f"Advertencia: La imagen {nombre_archivo} no fue encontrada.")

# Función para visualizar imágenes DICOM en secuencia continua
def visualizar_imagenes_secuencia(imagenes_dicom):
    fig, ax = plt.subplots(1, figsize=(8, 6))
    plt.ion()  # Modo interactivo para actualizar las ventanas
    
    for imagen in imagenes_dicom:
        # Mostrar imagen
        ax.imshow(imagen.pixel_array, cmap=plt.cm.bone)
        ax.set_title(f"Imagen DICOM - {os.path.basename(imagen.filename)}")
        ax.axis('off')
        
        # Actualizar la ventana
        plt.draw()
        plt.pause(0.5)  # Esperar un tiempo antes de mostrar la siguiente imagen
        ax.clear()      # Limpiar la ventana para la próxima imagen

# Visualizar imágenes DICOM en secuencia continua
visualizar_imagenes_secuencia(imagenes_dicom)
