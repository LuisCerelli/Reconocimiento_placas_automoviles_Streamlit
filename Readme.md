# Reconocimiento de Placas Vehiculares y Procesamiento de Imágenes

Este proyecto utiliza procesamiento de imágenes y técnicas de reconocimiento óptico de caracteres (OCR) para detectar bordes y reconocer el texto presente en imágenes de vehículos, específicamente para identificar las placas vehiculares. El flujo incluye varios pasos que permiten una correcta extracción de la información, comenzando con la eliminación del fondo de la imagen y culminando con la extracción de texto mediante técnicas avanzadas de OCR.

## Descripción del Funcionamiento

El código está desarrollado en **Python** y utiliza **Streamlit** para la creación de una interfaz de usuario interactiva, donde el usuario puede cargar imágenes. A partir de una imagen cargada (por ejemplo, una fotografía de un vehículo), se llevan a cabo varias etapas de procesamiento:

1. **Carga de la Imagen**: El usuario sube una imagen en formato `jpg` o `png` a través de la interfaz de Streamlit.
   
2. **Eliminación de Fondo**: Utilizando la librería `rembg`, se elimina el fondo de la imagen, dejando únicamente el objeto principal (el vehículo y su matrícula, por ejemplo).

3. **Preprocesamiento de la Imagen**:
   - **Conversión a escala de grises** para simplificar el procesamiento.
   - **Suavizado** (Gaussian Blur) para reducir el ruido.
   - **Ajuste de contraste** para mejorar la visibilidad de los detalles.
   - **Operaciones morfológicas** para mejorar los bordes y contornos.

4. **Detección de Bordes**: Se aplican técnicas de detección de bordes, específicamente el algoritmo de Canny, que resalta los bordes más importantes de la imagen. Esto ayuda a identificar estructuras relevantes como las letras y números de las placas.

5. **Reconocimiento de Texto (OCR)**: Finalmente, se utiliza la librería `EasyOCR` para extraer el texto de la imagen preprocesada, lo que permite identificar los caracteres presentes en las placas vehiculares. El OCR soporta múltiples idiomas, incluyendo inglés, español y francés.

6. **Salida de Resultados**: El texto extraído mediante OCR se muestra en la interfaz de Streamlit para que el usuario pueda visualizar los resultados.

## Ejemplo de Uso

Un usuario que desee identificar la matrícula de un vehículo a partir de una imagen puede seguir estos pasos:
1. Subir la imagen del vehículo en la interfaz.
2. El sistema eliminará el fondo automáticamente y procesará la imagen para mejorar los bordes y contornos.
3. Los caracteres presentes en la matrícula serán extraídos y presentados al usuario.

Este proceso es útil no solo para la identificación de placas, sino también para cualquier tarea que requiera extraer texto de imágenes complejas, como documentos escaneados o señales.

## Utilidad en Ingeniería de Datos y Ciencia de Datos

**Este código tiene múltiples aplicaciones tanto en ingeniería de datos como en ciencia de datos**:

- **En Ingeniería de Datos**, el flujo de procesamiento de imágenes puede considerarse un pipeline de ETL (Extracción, Transformación y Carga), donde las imágenes se cargan como entradas, se transforman mediante operaciones de preprocesamiento, y luego se extraen datos relevantes (el texto) que pueden ser almacenados o analizados. Este tipo de procesamiento es esencial en sistemas que manejan grandes volúmenes de datos no estructurados, como imágenes o videos, y requieren transformar estos datos en información útil.

- **En Ciencia de Datos**, este proyecto se puede integrar dentro de modelos de **Machine Learning** y **Deep Learning**. El reconocimiento de texto a partir de imágenes es fundamental en tareas como la clasificación de vehículos, reconocimiento automático de matrículas (ANPR), y análisis de imágenes en general. Además, los pasos de preprocesamiento son esenciales para mejorar la calidad de los datos antes de aplicar modelos predictivos o clasificadores.

**Por lo tanto, este proyecto no solo ofrece una solución efectiva para el reconocimiento de texto en imágenes, sino que también se alinea con los principios de ingeniería de datos, al construir un pipeline que toma datos no estructurados, los transforma y extrae información valiosa, y con los principios de ciencia de datos, al ser aplicable en proyectos de análisis de datos visuales y predicciones basadas en imágenes.**

## Consideraciones

- Es importante que las imágenes cargadas tengan buena calidad y resolución para maximizar la precisión del OCR.
- La elección de idiomas para el OCR (`EasyOCR`) puede ajustarse según el contexto de uso. En el código, están habilitados inglés, francés y español.
- Librerías adicionales como `rembg` requieren instalación previa, y algunos sistemas pueden requerir dependencias específicas para el procesamiento de imágenes.


