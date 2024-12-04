from fastapi import APIRouter, HTTPException
from app.utils.mercado_pago import create_payment

router = APIRouter()

@router.post("/pagamento/qrcode")
async def gerar_qrcode_pagamento(valor: float, descricao: str):
    """
    Gera um QR Code para pagamento via Mercado Pago.
    """
    try:
        # Dados da preferência de pagamento
        preference_data = {
            "items": [
                {
                    "title": descricao,
                    "quantity": 1,
                    "unit_price": valor
                }
            ],
            "back_urls": {
                "success": "http://seusite.com/sucesso",
                "failure": "http://seusite.com/falha",
                "pending": "http://seusite.com/pendente"
            },
            "auto_return": "approved"
        }

        # Cria a preferência de pagamento
        response = create_payment(preference_data)
        if response["status"] == 201:
            qr_code_url = response["response"]["sandbox_init_point"]  # URL do QR Code (modo sandbox)
            return {"status": "sucesso", "qr_code_url": qr_code_url}
        else:
            raise HTTPException(status_code=400, detail="Erro ao criar pagamento no Mercado Pago")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno: {e}")
