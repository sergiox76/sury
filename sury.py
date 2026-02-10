import streamlit as st
import time

st.set_page_config(page_title="Para Sury", page_icon="🌷", layout="centered")

# Estilos CSS para construir el tulipán desde cero
st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    
    .container {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-wrap: wrap;
        padding-top: 50px;
    }

    /* Estructura del Tulipán */
    .tulip {
        position: relative;
        width: 80px;
        height: 180px;
        margin: 10px;
        animation: flowerGrow 1.5s ease-out forwards;
        opacity: 0;
    }

    @keyframes flowerGrow {
        0% { transform: translateY(50px) scale(0); opacity: 0; }
        100% { transform: translateY(0) scale(1); opacity: 1; }
    }

    /* Los Pétalos */
    .petals {
        position: relative;
        width: 50px;
        height: 60px;
        margin: 0 auto;
    }

    .petal {
        position: absolute;
        width: 35px;
        height: 55px;
        border-radius: 50% 50% 50% 50% / 80% 80% 20% 20%;
    }

    .petal.main {
        background: #ff4d6d;
        left: 8px;
        z-index: 2;
    }

    .petal.left {
        background: #ff758f;
        left: -5px;
        transform: rotate(-25deg);
        z-index: 1;
    }

    .petal.right {
        background: #ff758f;
        left: 20px;
        transform: rotate(25deg);
        z-index: 1;
    }

    /* El Tallo */
    .stem {
        width: 4px;
        height: 100px;
        background: #2d6a4f;
        margin: 0 auto;
        border-radius: 2px;
    }

    /* La Hoja */
    .leaf {
        width: 30px;
        height: 15px;
        background: #40916c;
        border-radius: 0 15px 0 15px;
        position: absolute;
        top: 100px;
        left: 40px;
        transform: rotate(-20deg);
    }

    .mensaje {
        color: #ffb3c1;
        font-family: 'Comic Sans MS', cursive;
        font-size: 35px;
        text-align: center;
        margin-top: 40px;
        width: 100%;
        opacity: 0;
        animation: fadeIn 2s ease-in forwards;
    }

    @keyframes fadeIn {
        to { opacity: 1; }
    }
    </style>
    """, unsafe_allow_html=True)

# Función para generar el HTML de un tulipán
def crear_tulipan(delay):
    return f"""
    <div class="tulip" style="animation-delay: {delay}s;">
        <div class="petals">
            <div class="petal left"></div>
            <div class="petal main"></div>
            <div class="petal right"></div>
        </div>
        <div class="stem"></div>
        <div class="leaf"></div>
    </div>
    """

# Título oculto para SEO de la página
st.write("") 

# Espacio para el ramo
ramo_placeholder = st.empty()
html_ramo = "<div class='container'>"

# Generar 9 tulipanes para el ramo
for i in range(9):
    html_ramo += crear_tulipan(i * 0.4)
    ramo_placeholder.markdown(html_ramo + "</div>", unsafe_allow_html=True)
    time.sleep(0.4)

# Mensaje final
st.markdown("<div class='mensaje' style='animation-delay: 4s;'>Te quiero mucho mi Sury Hermosa</div>", unsafe_allow_html=True)

st.balloons()
