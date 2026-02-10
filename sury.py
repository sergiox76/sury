import streamlit as st
import time

st.set_page_config(
    page_title="Para ti 🌷",
    page_icon="🌷",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background-color: #000000;
}

/* Contenedor del ramo */
.bouquet {
    display: flex;
    justify-content: center;
    align-items: flex-end;
    gap: 25px;
    margin-top: 80px;
}

/* Flor */
.flower {
    display: flex;
    flex-direction: column;
    align-items: center;
    font-size: 48px;
    opacity: 0;
    animation: rise 2s forwards;
}

/* Retrasos para animación */
.f1 { animation-delay: 0s; }
.f2 { animation-delay: 0.4s; }
.f3 { animation-delay: 0.8s; }
.f4 { animation-delay: 1.2s; }
.f5 { animation-delay: 1.6s; }

/* Tallos */
.stem {
    width: 4px;
    background-color: #2ecc71;
    margin-top: -10px;
}

/* Animación de subida */
@keyframes rise {
    from {
        transform: translateY(60px);
        opacity: 0;
    }
    to {
        transform: translateY(0);
        opacity: 1;
    }
}

/* Lazo */
.ribbon {
    text-align: center;
    font-size: 42px;
    margin-top: -10px;
    opacity: 0;
    animation: appear 1.5s forwards;
    animation-delay: 2.4s;
}

/* Mensaje */
.message {
    color: #ff69b4;
    font-family: 'Comic Sans MS', cursive;
    font-size: 36px;
    text-align: center;
    margin-top: 40px;
    min-height: 50px;
}

@keyframes appear {
    to { opacity: 1; }
}
</style>
""", unsafe_allow_html=True)

# Ramo animado
st.markdown("""
<div class="bouquet">
    <div class="flower f1">
        🌷
        <div class="stem" style="height:140px"></div>
    </div>
    <div class="flower f2">
        🌷
        <div class="stem" style="height:130px"></div>
    </div>
    <div class="flower f3">
        🌷
        <div class="stem" style="height:120px"></div>
    </div>
    <div class="flower f4">
        🌷
        <div class="stem" style="height:130px"></div>
    </div>
    <div class="flower f5">
        🌷
        <div class="stem" style="height:140px"></div>
    </div>
</div>

<div class="ribbon">🎀</div>
""", unsafe_allow_html=True)

# Mensaje letra por letra
mensaje = "te quieo mucho sury 💖"
texto = st.empty()

for i in range(len(mensaje) + 1):
    texto.markdown(
        f"<div class='message'>{mensaje[:i]}</div>",
        unsafe_allow_html=True
    )
    time.sleep(0.08)

st.balloons()
