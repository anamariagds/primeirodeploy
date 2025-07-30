from django.conf import settings
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, To, Content

def enviar_email_sendgrid(nome, email_remetente, assunto, mensagem):
        conteudo = f"Mensagem de {nome} <{email_remetente}>:\n\n{mensagem}"
        
        email = Mail(
            from_email=Email(settings.DEFAULT_FROM_EMAIL, nome),
            to_emails=To(settings.DEFAULT_FROM_EMAIL),
            subject=assunto,
            plain_text_content=Content("text/plain", conteudo)
        )

        email.reply_to = email_remetente

        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        response = sg.send(email)

        return response
