# app.py
import streamlit as st
from assistant_logic import get_customer, generate_summary, generate_business_review_agenda, suggest_next_steps

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
