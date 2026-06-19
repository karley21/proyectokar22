import os
import fitz
import joblib
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline


def extraer_texto_pdf(ruta_pdf):
    texto = ""

    with fitz.open(ruta_pdf) as pdf:
        for pagina in pdf:
            texto += pagina.get_text()

    return texto


def cargar_documentos(carpeta_base="documentos"):
    textos = []
    categorias = []

    for categoria in os.listdir(carpeta_base):
        ruta_categoria = os.path.join(carpeta_base, categoria)

        if not os.path.isdir(ruta_categoria):
            continue

        for archivo in os.listdir(ruta_categoria):
            if archivo.endswith(".pdf"):
                ruta_archivo = os.path.join(ruta_categoria, archivo)
                texto = extraer_texto_pdf(ruta_archivo)

                textos.append(texto)
                categorias.append(categoria)

    return textos, categorias


textos, categorias = cargar_documentos()

modelo = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clasificador", MultinomialNB())
])

modelo.fit(textos, categorias)

os.makedirs("modelo", exist_ok=True)
joblib.dump(modelo, "modelo/clasificador.pkl")

print("Modelo entrenado correctamente.")