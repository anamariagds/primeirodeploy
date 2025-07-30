import requests
import json
from django.conf import settings

def enviar_email_sendgrid(nome, email_remetente, assunto, mensagem):
    url = "https://api.sendgrid.com/v3/mail/send"

    headers = {
        "Authorization": f"Bearer {settings.SENDGRID_API_KEY}",
        "Content-Type": "application/json"
    }

    body = {
        "personalizations": [
            {
                "to": [{"email": settings.DEFAULT_FROM_EMAIL}],
                "subject": assunto
            }
        ],
        "from": {"email": settings.DEFAULT_FROM_EMAIL, "name": nome},
        "reply_to": {"email": email_remetente},
        "content": [
            {
                "type": "text/plain",
                "value": f"Mensagem de {nome} <{email_remetente}>:\n\n{mensagem}"
            }
        ]
    }

    response = requests.post(url, headers=headers, data=json.dumps(body))
    return response.status_code == 202
