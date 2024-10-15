import streamlit as st
import numpy as np
import cv2
import rembg
from PIL import Image
import easyocr

# Carga de la imagen
archivo_cargado = st.file_uploader("Elige un archivo con la imagen de un vehículo", type=['jpg', 'png'])

# Procesamiento de la imagen si se ha cargado
if archivo_cargado is not None:
    # Convertir la imagen cargada a un formato que OpenCV pueda procesar
    img = cv2.imdecode(np.frombuffer(archivo_cargado.getvalue(), np.uint8), 1)

    # Elimina el fondo usando rembg
    output_array = rembg.remove(img)
    output_image = Image.fromarray(output_array)

    # Mostrar la imagen con el fondo eliminado
    st.image(output_image, caption="Imagen con fondo eliminado")

    # Convertir la imagen sin fondo a formato OpenCV para procesamiento adicional
    img_sin_fondo = np.array(output_image)

    # Conversión a escala de grises (útil para procesamiento de imágenes)
    img_gris = cv2.cvtColor(img_sin_fondo, cv2.COLOR_BGR2GRAY)

    ### ---- PREPROCESAMIENTO DE IMAGEN ---- ###
    
    # Aplicar suavizado (GaussianBlur) para reducir el ruido
    img_suavizada = cv2.GaussianBlur(img_gris, (5, 5), 0)

    # Ajuste del contraste de la imagen
    img_contraste = cv2.convertScaleAbs(img_suavizada, alpha=1.5, beta=0)

    # Aplicar técnicas de morfología para mejorar los contornos
    kernel = np.ones((3, 3), np.uint8)
    img_morph = cv2.morphologyEx(img_contraste, cv2.MORPH_CLOSE, kernel)

    # Mostrar la imagen tras el preprocesamiento
    st.image(img_morph, caption="Imagen tras el preprocesamiento")

    ### ---- DETECCIÓN DE BORDES ---- ###
    
    # Detección de bordes utilizando el algoritmo de Canny
    bordes = cv2.Canny(img_morph, 100, 200)

    # Mostrar la imagen con los bordes detectados
    st.image(bordes, caption="Bordes detectados", channels="GRAY")

    ### ---- RECONOCIMIENTO OCR ---- ###
    
    # OCR: reconocimiento óptico de caracteres usando easyOCR
    reader = easyocr.Reader(['en','fr','es'])  # Puedes añadir otros idiomas si lo necesitas
    ocr_result = reader.readtext(img_morph)

    # Mostrar el texto reconocido por OCR
    st.write("Texto reconocido por OCR:")
    for resultado in ocr_result:
        st.write(f"Texto: {resultado[1]}")
