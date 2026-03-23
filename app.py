import numpy as np
import matplotlib.pyplot as plt 
import streamlit as st


# Casos support
st.set_page_config(layout="wide")

#---------------Variables_iniciales--------------------
# angulo = float(input("angulo: "))
# velocidad_inicial = float(input("Velocidad inicial: "))
# altura_inicial = float(input("Altura inicial: "))
col1, col2, col3 = st.columns(3)

with col1:
    angulo = st.number_input("angulo (°)", min_value=-90.0, max_value=90.0, value=45.0)
with col2:
    velocidad_inicial = st.number_input("Velocidad inicial (m/s)", min_value=0.0, value=10.0)
with col3:
    altura_inicial = st.number_input("Altura inicial (m)", min_value=0.0, value=0.0)
angulo_rad = np.deg2rad(angulo)
g = 9.81
a = -(g/2)
b = velocidad_inicial * np.sin(angulo_rad)
c = altura_inicial

tiempo_transcurrido = (-b - np.sqrt(b**2 - 4*a*c)) / (2*a)
alcance_máximo = velocidad_inicial * np.cos(angulo_rad) * tiempo_transcurrido
# altura_máxima = altura_inicial + (velocidad_inicial * np.sin(angulo_rad) * (tiempo_transcurrido/2)) - ((1/2) * g * (tiempo_transcurrido/2)**2)

t_cima = (velocidad_inicial * np.sin(angulo_rad)) / g
altura_máxima = altura_inicial + velocidad_inicial * np.sin(angulo_rad) * t_cima - 0.5 * g * t_cima**2
# Formulas y Outputs
# Formulas y Outputs
# Formulas y Outputs
cola, colb, colc = st.columns(3)
with cola:
    st.markdown(f"<h3 style='text-align: center;'>t = {tiempo_transcurrido:.2f} s</h3>", unsafe_allow_html=True)
    with st.container(border=True):
        st.latex(r"t = \frac{-b - \sqrt{b^2 - 4ac}}{2a}")

with colb:
    st.markdown(f"<h3 style='text-align: center;'>Alcance máximo = {alcance_máximo:.2f} m</h3>", unsafe_allow_html=True)
    with st.container(border=True):
        st.latex(r"x_{max} = v_0 \cos(\theta) \cdot t")

with colc:
    st.markdown(f"<h3 style='text-align: center;'>Altura máxima = {altura_máxima:.2f} m</h3>", unsafe_allow_html=True)
    with st.container(border=True):
        st.latex(r"t_{cima} = \frac{v_0 \sin(\theta)}{g}")
        st.latex(r"y_{max} = h_0 + v_0 \sin(\theta) \cdot t_{cima} - \frac{1}{2} g \cdot t_{cima}^2")


#---------------Gráfica de la trayectoria--------------------
# Crear un vector de tiempos
t = np.linspace(0, tiempo_transcurrido, num=500)

# Posiciones en cada instante
if angulo == 90:
    x = np.zeros_like(t)
    y = velocidad_inicial*np.sin(angulo_rad) * t - 0.5*g*t**2
else:
    x = velocidad_inicial*np.cos(angulo_rad) * t
    y = altura_inicial + velocidad_inicial*np.sin(angulo_rad) * t - 0.5*g*t**2

plt.style.use("dark_background")
# Graficar
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(x, y, label="Trayectoria del proyectil")
ax.axhline(0, color="white", linewidth=0.8)
ax.set_title("Movimiento parabólico")
ax.set_xlabel("Distancia horizontal (m)")
ax.set_ylabel("Altura (m)")
ax.legend()
ax.grid(True)

st.title("Grafica de Movimiento parabólico:")
st.pyplot(fig)