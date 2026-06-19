import streamlit as st
import fitz
import joblib
import os

st.set_page_config(
    page_title="Clasificador de Documentos",
    page_icon="📄",
    layout="centered"
)

def extraer_texto_pdf(ruta_pdf):
    texto = ""
    with fitz.open(ruta_pdf) as pdf:
        for pagina in pdf:
            texto += pagina.get_text()
    return texto

st.title("📄 Clasificador Inteligente de Documentos")
st.write("Carga un documento PDF para identificar su tipo y nivel de confianza.")

archivo = st.file_uploader("Subir documento PDF", type=["pdf"])

if archivo is not None:
    ruta_temporal = os.path.join("documentos", archivo.name)

    with open(ruta_temporal, "wb") as f:
        f.write(archivo.getbuffer())

    st.success("Documento cargado correctamente")

    texto = extraer_texto_pdf(ruta_temporal)

    st.subheader("Vista previa del texto extraído")
    st.text_area("Contenido detectado", texto[:1500], height=250)

    modelo = joblib.load("modelo/clasificador.pkl")

    categoria = modelo.predict([texto])[0]
    probabilidades = modelo.predict_proba([texto])[0]
    confianza = max(probabilidades) * 100

    st.subheader("Resultado del análisis")

    st.metric("Tipo de documento", categoria)
    st.metric("Confianza", f"{confianza:.2f}%")

    st.progress(int(confianza))

    st.subheader("Datos del documento")
    st.write(f"**Nombre del archivo:** {archivo.name}")
    st.write(f"**Cantidad de caracteres extraídos:** {len(texto)}")