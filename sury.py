import streamlit as st
import time

# Configuración de página
st.set_page_config(page_title="Para Sury", page_icon="🌷", layout="centered")

# Estilos CSS
st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    
    .funda-ramo {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-wrap: wrap;
        max-width: 500px;
        margin: 0 auto;
    }
    
    .tulipan-svg {
        width: 120px;
        height: 160px;
        margin: -20px; /* Para que se amontonen como un ramo */
        opacity: 0;
        animation: aparecer 1.5s ease-out forwards;
    }

    @keyframes aparecer {
        0% { transform: translateY(30px) scale(0); opacity: 0; }
        100% { transform: translateY(0) scale(1); opacity: 1; }
    }

    .texto-sury {
        color: #FFB6C1;
        font-family: 'Dancing Script', cursive;
        font-size: 3.5rem;
        text-align: center;
        margin-top: 30px;
        opacity: 0;
        animation: fadeIn 3s ease-in forwards;
        animation-delay: 5s;
    }

    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)

# El "dibujo" del tulipán en código SVG (líneas y curvas)
def dibujo_tulipan(color_flor, delay):
    svg = f"""
    <svg class="tulipan-svg" style="animation-delay: {delay}s;" viewBox="0 0 100 150">
        <path d="M50 150 Q55 100 50 60" stroke="#2D5A27" stroke-width="4" fill="none" />
        <path d="M50 120 Q30 110 20 80 Q40 90 50 105" fill="#3B7A32" />
        <path d="M50 60 Q30 60 25 35 Q40 15 50 40 Q60 15 75 35 Q70 60 50 60" fill="{color_flor}" />
        <path d="M50 60 Q40 55 35 30 Q50 10 65 30 Q60 55 50 60" fill="{color_flor}" opacity="0.8" />
    </svg>
    """
    return svg

# Colores para el ramo
colores = ["#FF69B4", "#FF1493", "#FFC0CB", "#FF007F", "#DA70D6", "#BA55D3", "#FF69B4", "#FFB6C1"]

st.write("<div class='funda-ramo'>", unsafe_allow_html=True)

# Contenedor para ir mostrando los tulipanes
placeholder = st.empty()
html_acumulado = "<div class='funda-ramo'>"

for i, color in enumerate(colores):
    html_acumulado += dibujo_tulipan(color, i * 0.5)
    placeholder.markdown(html_acumulado + "</div>", unsafe_allow_html=True)
    time.sleep(0.5)

# Mensaje final
st.markdown("<div class='texto-sury'>Te quiero mucho mi Sury Hermosa</div>", unsafe_allow_html=True)

# Globos finales
if i == len(colores) - 1:
    st.balloons()