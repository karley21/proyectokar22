import fitz
import joblib


def extraer_texto_pdf(ruta_pdf):
    texto = ""

    with fitz.open(ruta_pdf) as pdf:
        for pagina in pdf:
            texto += pagina.get_text()

    return texto


modelo = joblib.load("modelo/clasificador.pkl")

ruta_documento = "prueba.pdf"

texto = extraer_texto_pdf(ruta_documento)
print(texto[:1000])

categoria = modelo.predict([texto])[0]
probabilidades = modelo.predict_proba([texto])[0]
confianza = max(probabilidades) * 100

print(f"Categoría detectada: {categoria}")
print(f"Confianza: {confianza:.2f}%")