import streamlit as st
import fitz 
import joblib
import os

st.set_page_config(
    page_title="Clasificador de Documentos",
    page_icon="🤖",
    layout="wide", 
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .metric-box {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        border: 1px solid #e9ecef;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

def extraer_texto_pdf(bytes_pdf):
    texto = ""
    with fitz.open(stream=bytes_pdf, filetype="pdf") as pdf:
        for pagina in pdf:
            texto += pagina.get_text()
    return texto

st.title("🤖 Clasificador Inteligente de Documentos")
st.markdown("""
    Bienvenido al sistema de análisis documental automatizado. 
    Sube un archivo en formato **PDF** para identificar su categoría mediante Inteligencia Artificial.
""")
st.write("---")

col_upload, col_info = st.columns([2, 1])

with col_upload:
    archivo = st.file_uploader(
        "Arrastra o selecciona tu documento aquí", 
        type=["pdf"],
        help="Solo se admiten archivos en formato PDF."
    )

with col_info:
    st.info("""
        💡 **¿Cómo funciona?**
        1. Sube el archivo PDF.
        2. El sistema extraerá el texto automáticamente.
        3. El modelo de Machine Learning predecirá el tipo de documento en segundos.
    """)

if archivo is not None:
    bytes_pdf = archivo.read()
    
    with st.spinner("⚡ Analizando y extrayendo texto del documento..."):
        texto = extraer_texto_pdf(bytes_pdf)
        
        if os.path.exists("modelo/clasificador.pkl"):
            modelo = joblib.load("modelo/clasificador.pkl")
            categoria = modelo.predict([texto])[0]
            probabilidades = modelo.predict_proba([texto])[0]
            confianza = max(probabilidades) * 100
        else:
            categoria = "Ejemplo (Modelo no encontrado)"
            confianza = 95.50

    st.success("✅ ¡Análisis completado con éxito!")
    
    tab_resultados, tab_detalles, tab_texto = st.tabs([
        "📊 Resultados del Análisis", 
        "📁 Datos del Archivo", 
        "📝 Vista Previa del Texto"
    ])
    
    with tab_resultados:
        st.write("### Diagnóstico de la IA")
        
        col_cat, col_conf = st.columns(2)
        
        with col_cat:
            st.markdown(f"""
                <div class="metric-box">
                    <p style="color:#6c757d; font-size:14px; margin-bottom:5px; font-weight:bold;">TIPO DE DOCUMENTO DETECTADO</p>
                    <h2 style="color:#1e3d59; margin:0;">✨ {categoria.upper()}</h2>
                </div>
            """, unsafe_allow_html=True)
            
        with col_conf:
            color_confianza = "#28a745" if confianza > 75 else "#ffc107" if confianza > 50 else "#dc3545"
            st.markdown(f"""
                <div class="metric-box">
                    <p style="color:#6c757d; font-size:14px; margin-bottom:5px; font-weight:bold;">NIVEL DE CONFIANZA</p>
                    <h2 style="color:{color_confianza}; margin:0;">{confianza:.2f}%</h2>
                </div>
            """, unsafe_allow_html=True)
            
        st.progress(int(confianza))
        
    with tab_detalles:
        st.write("### Información General")
        col_d1, col_d2, col_d3 = st.columns(3)
        col_d1.metric("Nombre del archivo", archivo.name)
        col_d2.metric("Tamaño", f"{archivo.size / 1024:.2f} KB")
        col_d3.metric("Caracteres extraídos", f"{len(texto):,}")

    with tab_texto:
        st.write("### Contenido detectado (Primeros 1500 caracteres)")
        if texto.strip():
            st.text_area("", texto[:1500], height=300, disabled=True)
        else:
            st.warning("⚠️ No se pudo extraer texto legible de este PDF. ¿Es un documento escaneado como imagen?")

else:
    st.write("---")
    st.info("📌 Por favor, sube un archivo PDF en la parte superior para comenzar el análisis.")