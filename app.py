# app.py
import streamlit as st
from assistant_logic import get_customer, generate_summary, generate_business_review_agenda, suggest_next_steps
# app.py (agrega al inicio)
if "step" not in st.session_state:
    st.session_state.step = "start"
if "selected_client" not in st.session_state:
    st.session_state.selected_client = None

st.set_page_config(page_title="AI Success Companion", page_icon="🤖")
st.title("🤖 Asistente Virtual de Éxito del Cliente")

# Input: selector de cliente
st.sidebar.title("Selecciona un cliente")
client_keys = {
    "ACME Corp": "acme_corp",
    "Beta Inc": "beta_inc",
    "Nova LLC": "nova_llc"
}
selected_name = st.sidebar.selectbox("Cliente", list(client_keys.keys()))
client_key = client_keys[selected_name]
customer = get_customer(client_key)

if customer:
    st.subheader("📌 Resumen de la cuenta")
    st.text(generate_summary(customer))

    st.subheader("📝 Agenda de Business Review")
    st.text(generate_business_review_agenda(customer))

    st.subheader("🚀 Recomendación de próximos pasos")
    st.success(suggest_next_steps(customer["maturity"]))
else:
    st.error("Cliente no encontrado.")

import streamlit as st
from assistant_logic import process_user_message

st.subheader("💬 Chat con tu AI Success Companion")

if "history" not in st.session_state:
    st.session_state.history = []

# Input de usuario
user_input = st.chat_input("Escribe aquí tu pregunta...")
if user_input:
    response = process_user_message(user_input)
    st.session_state.history.append(("usuario", user_input))
    st.session_state.history.append(("bot", response))

# Mostrar el historial
for sender, msg in st.session_state.history:
    if sender == "usuario":
        st.chat_message("user").markdown(msg)
    else:
        st.chat_message("assistant").markdown(msg)

