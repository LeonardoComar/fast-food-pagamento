import mercadopago

mp = mercadopago.SDK("TEST-1234567890123456-123456-1234567890abcd1234567890abcd-123456")

def create_payment(preference_data):
    try:
        response = mp.preference().create(preference_data)
        return response
    except Exception as e:
        print(f"Erro ao criar pagamento: {e}")
        raise
