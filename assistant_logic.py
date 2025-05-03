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
