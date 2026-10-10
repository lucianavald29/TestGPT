
import streamlit as st

# CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(
    page_title="Crochet Boutique | Bolsos Artesanales",
    page_icon="👜",
    layout="wide"
)

# ESTILOS CSS
st.markdown("""
<style>
.stApp {
    background-color: #fff8f2;
}
h1, h2, h3 {
    color: #8b5e3c;
}
p {
    color: #59483e;
}
div.stButton > button {
    background-color: #b77952;
    color: white;
    border-radius: 12px;
    border: none;
    padding: 10px 20px;
}
div.stButton > button:hover {
    background-color: #8b5e3c;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ENCABEZADO
st.title("👜 Crochet Boutique")
st.subheader("Bolsos artesanales tejidos con amor")
st.write(
    "Descubre bolsos únicos hechos a mano con dedicación, "
    "creatividad y estilo. ¡Lleva contigo una pieza artesanal!"
)

st.divider()

# MENÚ DE NAVEGACIÓN
menu = st.radio(
    "Navegación",
    ["Inicio", "Catálogo", "Sobre nosotros", "Contacto"],
    horizontal=True
)

# PRODUCTOS
productos = [
    {
        "nombre": "Bolso Boho Chic",
        "precio": 65,
        "descripcion": "Bolso tejido a crochet con estilo bohemio.",
        "imagen": "https://placehold.co/400x300/F0D9C5/795548?text=Bolso+Boho"
    },
    {
        "nombre": "Bolso Elegante",
        "precio": 80,
        "descripcion": "Diseño sofisticado para ocasiones especiales.",
        "imagen": "https://placehold.co/400x300/E8D5C4/795548?text=Bolso+Elegante"
    },
    {
        "nombre": "Bolso Casual",
        "precio": 50,
        "descripcion": "Cómodo, práctico y perfecto para todos los días.",
        "imagen": "https://placehold.co/400x300/F5E6D3/795548?text=Bolso+Casual"
    },
    {
        "nombre": "Bolso Colorido",
        "precio": 70,
        "descripcion": "Un diseño alegre que combina con tu personalidad.",
        "imagen": "https://placehold.co/400x300/EAD7E5/795548?text=Bolso+Colorido"
    }
]

# INICIO
if menu == "Inicio":
    st.image(
        "https://placehold.co/1200x400/EAD7C5/795548?text=Bolsos+Artesanales+a+Crochet",
        use_container_width=True
    )
    st.header("✨ Artesanía que enamora")
    st.write(
        "Nuestros bolsos están tejidos a mano, cuidando cada detalle. "
        "Encuentra el complemento perfecto para tu estilo."
    )

    col1, col2, col3 = st.columns(3)
    col1.metric("Diseños", "Únicos")
    col2.metric("Elaboración", "A mano")
    col3.metric("Estilo", "Artesanal")

    if st.button("Ver catálogo"):
        st.session_state["ir_catalogo"] = True
        st.rerun()

# CATÁLOGO
elif menu == "Catálogo" or st.session_state.get("ir_catalogo", False):
    st.session_state["ir_catalogo"] = False
    st.header("🛍️ Nuestro catálogo")
    st.write("Precios expresados en soles peruanos (S/).")

    busqueda = st.text_input("🔎 Buscar un bolso")
    presupuesto = st.slider(
        "Precio máximo (S/)",
        min_value=30,
        max_value=150,
        value=150
    )

    carrito = st.session_state.setdefault("carrito", [])

    columnas = st.columns(2)

    for i, producto in enumerate(productos):
        if (
            busqueda.lower() in producto["nombre"].lower()
            and producto["precio"] <= presupuesto
        ):
            with columnas[i % 2]:
                st.image(producto["imagen"], use_container_width=True)
                st.subheader(producto["nombre"])
                st.write(producto["descripcion"])
                st.markdown(f"### S/ {producto['precio']:.2f}")

                if st.button(
                    "🛒 Agregar al carrito",
                    key=f"agregar_{i}"
                ):
                    carrito.append(producto["nombre"])
                    st.success("¡Producto agregado al carrito!")

    st.divider()
    st.subheader("🛒 Tu carrito")
    if carrito:
        for nombre in carrito:
            st.write(f"• {nombre}")
        if st.button("Vaciar carrito"):
            st.session_state["carrito"] = []
            st.rerun()
    else:
        st.info("Tu carrito está vacío.")

# SOBRE NOSOTROS
elif menu == "Sobre nosotros":
    st.header("💖 Nuestra historia")
    st.write(
        "Somos un emprendimiento dedicado a la creación de bolsos "
        "a crochet. Cada pieza está elaborada artesanalmente, "
        "con paciencia, pasión y mucho amor por los detalles."
    )
    st.write(
        "Queremos ofrecer accesorios originales, duraderos y "
        "hechos a mano para acompañarte en cada momento."
    )

# CONTACTO
elif menu == "Contacto":
    st.header("📩 Contáctanos")
    st.write("¿Te gustó alguno de nuestros bolsos? Escríbenos.")

    nombre = st.text_input("Tu nombre")
    correo = st.text_input("Tu correo electrónico")
    mensaje = st.text_area("¿Qué bolso te interesa?")

    if st.button("Enviar consulta"):
        if nombre.strip() and correo.strip() and mensaje.strip():
            st.success(
                "¡Gracias por escribirnos! Tu consulta está lista. "
                "Para recibirla, conecta un servicio de envío de mensajes."
            )
        else:
            st.warning("Completa todos los campos antes de continuar.")

st.divider()
st.caption("© 2026 Crochet Boutique | Hecho a mano con amor 🧶")
