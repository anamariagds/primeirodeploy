from django.shortcuts import render, redirect
#from .dados import habilidades, projetos
from .models import Habilidade, Projeto
from .forms import ContatoForm
#from django.core.mail import EmailMessage
from .utils.email_lib import enviar_email_sendgrid

from django.conf import settings
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']


            sucesso = enviar_email_sendgrid(nome, email, assunto, mensagem)

            if sucesso:
                messages.success(request, "Email enviado com sucesso!")
            else:
                messages.error(request, "Ocorreu um erro ao enviar o email. Tente novamente mais tarde.")
                
            return redirect('home')
    else:
        form = ContatoForm()
        
    habilidades = Habilidade.objects.all()

    #         corpo_email = f"Mensagem de {nome} <{email}>:\n\n{mensagem}"

    #         email_obj = EmailMessage(
    #             subject= assunto,
    #             body= corpo_email,
    #             from_email= settings.DEFAULT_FROM_EMAIL,
    #             to=[settings.DEFAULT_FROM_EMAIL],
    #             reply_to=[email]
    #         )
    #         email_obj.send()
    #         messages.success(request, "Email enviado com sucesso!")
    #         return redirect('home')
    # else:
    #      form = ContatoForm()
    # habilidades = Habilidade.objects.all()
    return render(request, 'home.html', {'habilidades': habilidades, 'form': form})

def lista_projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'projetos.html', {'projetos': projetos})

def detalhes_projeto(request, id_projeto):
    projeto = Projeto.objects.get(id=id_projeto)
    return render(request, 'detalhes_projeto.html', {'projeto': projeto})