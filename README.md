# Sistema Inteligente de Clasificación Documental

## Descripción

Este proyecto consiste en el desarrollo de un sistema inteligente de clasificación documental utilizando Python y técnicas de Machine Learning. Su objetivo es automatizar la identificación y categorización de documentos administrativos, reduciendo el tiempo de procesamiento y minimizando los errores asociados a la clasificación manual.

El sistema analiza el contenido textual de los documentos, identifica patrones lingüísticos mediante Procesamiento de Lenguaje Natural (PLN) y asigna automáticamente una categoría previamente definida.

---

## Objetivos

* Automatizar la clasificación de documentos administrativos.
* Reducir los tiempos de procesamiento documental.
* Minimizar errores humanos en la categorización de archivos.
* Facilitar la organización y recuperación de información.
* Servir como base para futuros sistemas de gestión documental inteligente.

---

## Tecnologías Utilizadas

* Python 3.12
* Scikit-Learn
* Pandas
* PyMuPDF
* Joblib
* Machine Learning Supervisado
* TF-IDF (Term Frequency - Inverse Document Frequency)

---

## Funcionamiento General

El sistema opera en cuatro etapas principales:

### 1. Carga de documentos

Los documentos se organizan en carpetas según su categoría:

```text
documentos/
│
├── facturas/
├── curriculums/
└── reportes/
```

Cada carpeta contiene ejemplos de documentos pertenecientes a una categoría específica.

### 2. Extracción de texto

El sistema utiliza la librería PyMuPDF para extraer el contenido textual de los archivos PDF.

### 3. Entrenamiento del modelo

Los textos extraídos son transformados mediante TF-IDF para convertir las palabras en vectores numéricos.

Posteriormente se entrena un clasificador probabilístico que aprende los patrones característicos de cada tipo documental.

### 4. Clasificación automática

Cuando se recibe un nuevo documento:

1. Se extrae su contenido textual.
2. Se aplica el mismo proceso de vectorización.
3. El modelo predice la categoría más probable.
4. Se calcula el porcentaje de confianza de la predicción.

---

## Estructura del Proyecto

```text
clasificador_documentos/
│
├── documentos/
│   ├── facturas/
│   ├── curriculums/
│   └── reportes/
│
├── modelo/
│   └── clasificador.pkl
│
├── entrenar.py
├── clasificar.py
├── requirements.txt
└── README.md
```

---

## Instalación

### Crear entorno virtual

```bash
python -m venv venv
```

### Activar entorno virtual

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

por si da error al momento de iniciar el entorno virtual

paso 1
```bash
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
```
paso 2
```bash
PS C:\Users\PC\Documents\Proyecto diplomado\proyecto-Karley-master> .\venv\Scripts\Activate.ps1
```


### Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Entrenamiento del Modelo

Ejecutar:

```bash
python entrenar.py
```

El sistema analizará todos los documentos de entrenamiento y generará el archivo:

```text
modelo/clasificador.pkl
```

---

## Clasificación de Nuevos Documentos

Colocar el archivo PDF a evaluar en la raíz del proyecto y ejecutar:

```bash
python clasificar.py
```

Salida esperada:

```text
Categoría detectada: factura
Confianza: 92.45%
```

---

## Mejoras Futuras

* Integración con OCR para imágenes escaneadas.
* Soporte para documentos Word y Excel.
* Integración con bases de datos PostgreSQL.
* Integración con Supabase.
* API REST mediante FastAPI.
* Interfaz web con React.
* Clasificación mediante modelos de Inteligencia Artificial Generativa.
* Almacenamiento de metadatos y auditoría documental.

---

## Autor

Karley 

Proyecto académico desarrollado para la Escuela de Ingeniería de Sistemas, orientado a la aplicación de Machine Learning en procesos administrativos y gestión documental inteligente.
