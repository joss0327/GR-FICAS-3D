
import streamlit as st
import numpy as np
import plotly.graph_objects as go

# ==========================================
# CONFIGURACION DE LA PAGINA
# ==========================================

st.set_page_config(
    page_title="Visualizador Geometrico 3D",
    page_icon="📐",
    layout="wide"
)

st.markdown("""
<style>
    .main {
        background-color: #f0f4f8;
    }
    .titulo {
        background-color: #17365d;
        padding: 22px;
        border-radius: 12px;
        text-align: center;
        color: white;
    }
    .titulo h1 {
        color: white;
        margin-bottom: 5px;
    }
    .titulo p {
        color: #dce6f1;
        margin: 0;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# ENCABEZADO
# ==========================================

st.markdown("""
<div class="titulo">
    <h1>VISUALIZADOR GEOMETRICO 3D</h1>
    <p>ELIPSE | CIRCUNFERENCIA | ESFERA</p>
</div>
""", unsafe_allow_html=True)

st.write("")

st.info(
    "Modifica los parámetros numéricos para actualizar "
    "las representaciones tridimensionales."
)

# ==========================================
# FUNCIONES PARA LOS EJES
# ==========================================

def configurar_escena(figura, titulo, limite):

    figura.update_layout(
        title=dict(
            text=titulo,
            x=0.5,
            font=dict(size=18, color="#17365d")
        ),
        scene=dict(
            xaxis=dict(
                title="Eje X",
                range=[-limite, limite],
                showbackground=True,
                backgroundcolor="#f5f8fc"
            ),
            yaxis=dict(
                title="Eje Y",
                range=[-limite, limite],
                showbackground=True,
                backgroundcolor="#f5f8fc"
            ),
            zaxis=dict(
                title="Eje Z",
                range=[-limite, limite],
                showbackground=True,
                backgroundcolor="#f5f8fc"
            ),
            aspectmode="cube",
            camera=dict(
                eye=dict(x=1.5, y=1.5, z=1.2)
            )
        ),
        margin=dict(l=0, r=0, t=55, b=0),
        height=480,
        paper_bgcolor="white",
        showlegend=False
    )

    return figura


# ==========================================
# PANEL DE PARAMETROS
# ==========================================

st.subheader("⚙️ Parámetros de las figuras")

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown("### 🔵 Elipse")

    a = st.number_input(
        "Semieje mayor (a)",
        min_value=0.1,
        max_value=100.0,
        value=5.0,
        step=0.5,
        key="elipse_a"
    )

    b = st.number_input(
        "Semieje menor (b)",
        min_value=0.1,
        max_value=100.0,
        value=3.0,
        step=0.5,
        key="elipse_b"
    )

with col2:

    st.markdown("### 🟢 Circunferencia")

    r_c = st.number_input(
        "Radio (r)",
        min_value=0.1,
        max_value=100.0,
        value=4.0,
        step=0.5,
        key="radio_c"
    )

with col3:

    st.markdown("### 🔵 Esfera")

    r_e = st.number_input(
        "Radio (r)",
        min_value=0.1,
        max_value=100.0,
        value=4.0,
        step=0.5,
        key="radio_e"
    )

# ==========================================
# COORDENADAS
# ==========================================

t = np.linspace(0, 2 * np.pi, 300)

# ==========================================
# GRAFICA 1: ELIPSE
# ==========================================

x_elipse = a * np.cos(t)
y_elipse = b * np.sin(t)
z_elipse = np.zeros_like(t)

fig1 = go.Figure()

fig1.add_trace(
    go.Scatter3d(
        x=x_elipse,
        y=y_elipse,
        z=z_elipse,
        mode="lines",
        line=dict(
            color="#2563eb",
            width=8
        ),
        name="Elipse"
    )
)

fig1.add_trace(
    go.Scatter3d(
        x=[0],
        y=[0],
        z=[0],
        mode="markers",
        marker=dict(
            size=6,
            color="red"
        ),
        name="Centro"
    )
)

configurar_escena(
    fig1,
    "ELIPSE",
    max(a, b) * 1.3
)

# ==========================================
# GRAFICA 2: CIRCUNFERENCIA
# ==========================================

x_c = r_c * np.cos(t)
y_c = r_c * np.sin(t)
z_c = np.zeros_like(t)

fig2 = go.Figure()

fig2.add_trace(
    go.Scatter3d(
        x=x_c,
        y=y_c,
        z=z_c,
        mode="lines",
        line=dict(
            color="#16a34a",
            width=8
        ),
        name="Circunferencia"
    )
)

# Radio

fig2.add_trace(
    go.Scatter3d(
        x=[0, r_c],
        y=[0, 0],
        z=[0, 0],
        mode="lines+markers",
        line=dict(
            color="orange",
            width=6,
            dash="dash"
        ),
        marker=dict(size=4),
        name="Radio"
    )
)

configurar_escena(
    fig2,
    "CIRCUNFERENCIA",
    r_c * 1.3
)

# ==========================================
# GRAFICA 3: ESFERA
# ==========================================

u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 80)

x_esfera = r_e * np.outer(
    np.cos(u),
    np.sin(v)
)

y_esfera = r_e * np.outer(
    np.sin(u),
    np.sin(v)
)

z_esfera = r_e * np.outer(
    np.ones_like(u),
    np.cos(v)
)

fig3 = go.Figure()

fig3.add_trace(
    go.Surface(
        x=x_esfera,
        y=y_esfera,
        z=z_esfera,
        colorscale=[
            [0, "#17365d"],
            [0.5, "#3978b9"],
            [1, "#93c5fd"]
        ],
        opacity=0.85,
        showscale=False,
        name="Esfera"
    )
)

# Radio de la esfera

fig3.add_trace(
    go.Scatter3d(
        x=[0, r_e],
        y=[0, 0],
        z=[0, 0],
        mode="lines+markers",
        line=dict(
            color="orange",
            width=6,
            dash="dash"
        ),
        marker=dict(size=4),
        name="Radio"
    )
)

configurar_escena(
    fig3,
    "ESFERA",
    r_e * 1.3
)

# ==========================================
# MOSTRAR LAS TRES FIGURAS
# ==========================================

st.divider()

st.subheader("📊 Representaciones tridimensionales")

p1, p2 = st.columns(2)

with p1:

    st.plotly_chart(
        fig1,
        use_container_width=True,
        key="grafica_elipse"
    )

with p2:

    st.plotly_chart(
        fig2,
        use_container_width=True,
        key="grafica_circunferencia"
    )

st.plotly_chart(
    fig3,
    use_container_width=True,
    key="grafica_esfera"
)

# ==========================================
# INFORMACION MATEMATICA
# ==========================================

st.divider()

st.subheader("📐 Información matemática")

m1, m2, m3 = st.columns(3)

with m1:

    st.markdown("### Elipse")

    st.latex(
        r"\frac{x^2}{a^2}+\frac{y^2}{b^2}=1"
    )

    st.write(f"Semieje mayor: {a}")
    st.write(f"Semieje menor: {b}")
    st.write(f"Área: {np.pi*a*b:.2f} u²")

with m2:

    st.markdown("### Circunferencia")

    st.latex(
        r"x^2+y^2=r^2"
    )

    st.write(f"Radio: {r_c}")
    st.write(f"Diámetro: {2*r_c:.2f}")
    st.write(f"Longitud: {2*np.pi*r_c:.2f} u")

with m3:

    st.markdown("### Esfera")

    st.latex(
        r"x^2+y^2+z^2=r^2"
    )

    st.write(f"Radio: {r_e}")
    st.write(f"Área: {4*np.pi*r_e**2:.2f} u²")
    st.write(f"Volumen: {4/3*np.pi*r_e**3:.2f} u³")

# ==========================================
# PIE DE PAGINA
# ==========================================

st.divider()

st.caption(
    "Visualizador Geométrico 3D | Desarrollado en Python "
    "con Streamlit, NumPy y Plotly."
)