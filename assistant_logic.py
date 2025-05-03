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
