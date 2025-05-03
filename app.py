# app.py
import streamlit as st
from assistant_logic import (
    get_customer,
    generate_summary,
    generate_business_review_agenda,
    suggest_next_steps,
)

st.set_page_config(page_title="AI Success Companion", page_icon="🤖")
st.title("🤖 Asistente Virtual de Éxito del Cliente")

# Inicializar variables de sesión
if "step" not in st.session_state:
    st.session_state.step = "start"
if "selected_client" not in st.session_state:
    st.session_state.selected_client = None

st.subheader("🧠 Chat guiado")

# Paso 1: Selección de cliente
if st.session_state.step == "start":
    st.chat_message("assistant").markdown("¡Hola! ¿Sobre qué cliente deseas hablar?")
    col1, col2, col3 = st.columns(3)
    if col1.button("ACME Corp"):
        st.session_state.selected_client = "acme_corp"
        st.session_state.step = "ask_topic"
    if col2.button("Beta Inc"):
        st.session_state.selected_client = "beta_inc"
        st.session_state.step = "ask_topic"
    if col3.button("Nova LLC"):
        st.session_state.selected_client = "nova_llc"
        st.session_state.step = "ask_topic"

# Paso 2: Qué quieres saber
elif st.session_state.step == "ask_topic":
    customer = get_customer(st.session_state.selected_client)
    st.chat_message("assistant").markdown(f"¿Qué deseas saber de **{customer['name']}**?")
    col1, col2, col3 = st.columns(3)
    if col1.button("Estado de cuenta"):
        st.chat_message("assistant").markdown(generate_summary(customer))
    if col2.button("Agenda para Business Review"):
        st.chat_message("assistant").markdown(generate_business_review_agenda(customer))
    if col3.button("Siguientes pasos"):
        st.chat_message("assistant").markdown(suggest_next_steps(customer["maturity"]))

    st.markdown("🔁 ¿Quieres volver a empezar?")
    if st.button("Elegir otro cliente"):
        st.session_state.step = "start"
        st.session_state.selected_client = None


