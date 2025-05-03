# assistant_logic.py
from database import customers_data

def get_customer(name_key):
    return customers_data.get(name_key.lower())

def generate_summary(customer):
    return (
        f"📊 Cliente: {customer['name']}\n"
        f"🩺 Salud de la cuenta: {customer['health']}\n"
        f"📈 Madurez: {customer['maturity']}\n"
        f"📅 Última revisión: {customer['last_review']}\n"
        f"💬 Feedback: {customer['feedback']}"
    )

def generate_business_review_agenda(customer):
    usage = customer['usage_metrics']
    return (
        f"📋 Agenda para Business Review:\n"
        f"1. Estado de la cuenta: {customer['health']}\n"
        f"2. Uso semanal: {usage['logins_per_week']} logins, módulos usados: {', '.join(usage['modules_used'])}\n"
        f"3. Feedback del cliente\n"
        f"4. Plan según madurez: {customer['maturity']}\n"
        "5. Próximos pasos y Q&A"
    )

def suggest_next_steps(maturity):
    suggestions = {
        "Onboarding": "Realizar llamada de bienvenida y entregar guía de uso.",
        "Adopción": "Revisar funcionalidades clave y metas.",
        "Expansión": "Presentar funciones premium o casos de éxito.",
        "Riesgo": "Identificar problemas urgentes y agendar llamada.",
        "Churn": "Intentar rescate con oferta o revisión ejecutiva."
    }
    return suggestions.get(maturity, "Sin sugerencias disponibles.")

# assistant_logic.py (añadir al final)
from difflib import get_close_matches

def get_best_match(user_input):
    possible_clients = ["acme corp", "beta inc", "nova llc"]
    match = get_close_matches(user_input.lower(), possible_clients, n=1, cutoff=0.5)
    return match[0].replace(" ", "_") if match else None

def process_user_message(message):
    message_lower = message.lower()
    client_key = get_best_match(message)

    if not client_key:
        return "🤖 No encontré a ese cliente. Intenta con: ACME Corp, Beta Inc, o Nova LLC."

    customer = get_customer(client_key)

    if "estado" in message_lower or "cómo está" in message_lower:
        return generate_summary(customer)
    elif "agenda" in message_lower:
        return generate_business_review_agenda(customer)
    elif "siguiente" in message_lower or "próximo" in message_lower:
        return suggest_next_steps(customer["maturity"])
    else:
        return "🤖 Puedes preguntarme por el estado de la cuenta, agenda para business review o próximos pasos."
