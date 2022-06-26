from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib import auth, messages
from receitas.models import Receita


def cadastro(request):
    """ Cadastra um novo usuário no sistema """

    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        
        
        if campo_vazio(nome):
            messages.error(request, 'O campo "Nome completo" não pode ficar em branco!')
            return redirect('cadastro')
        
        if campo_vazio(email):
            messages.error(request, 'O campo "Email" não pode ficar em branco!')
            return redirect('cadastro')
        
        if senhas_diferentes(senha, senha2):
            messages.error(request, 'As senhas não são iguais!')
            return redirect('cadastro')
                
        if email_ja_cadastrado(email) or nome_ja_cadastrado(nome):
            messages.error(request, 'Usuário já cadastrado')
            return redirect('cadastro')
        
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        
        messages.success(request, "Usuário cadastrado!")
         
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')

def login(request):
    """ Realiza o login de um usuário no sistema """
    if request.method == 'POST':

        email = request.POST['email']
        senha = request.POST['senha']
        
        email = email.strip()
        senha = senha.strip()
        
        if campo_vazio(email) or campo_vazio(senha):
            messages.error(request, "Os campos 'Email' e 'Senha' não podem ficar em branco")
            return redirect('login')
        
        if email_ja_cadastrado(email):
            
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()

            user = auth.authenticate(request, username=nome, password=senha)
            
            if user is not None:
                auth.login(request, user)
                
                return redirect('dashboard')
            
        
        messages.error(request, "Usuário ou Senha inválida")
        
    return render(request, 'usuarios/login.html')

def logout(request):
    """ Realiza o logout do usuário no sistema """
    auth.logout(request)
    return redirect('index')

def dashboard(request):
    """ Exibe o dashboard do usuário, com todas suas receitas"""
    if request.user.is_authenticated:
        
        id = request.user.id
        
        receitas = Receita.objects.order_by('-data_receita').filter(pessoa=id)
        
        dados = {
            'receitas' : receitas
        }
        
        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('index')
 
def campo_vazio(campo):
    """ Retirna se o campo informado está vazio """
    return not campo.strip()

def senhas_diferentes(senha, senha2):
    """ Retorna caso as senhas sejam diferentes """
    return senha.strip() != senha2.strip()

def email_ja_cadastrado(email):
    """ Retorna se o email já está cadastrado no sistema """
    return User.objects.filter(email=email).exists()

def nome_ja_cadastrado(nome):
    """ Retorna se o nome já está cadastrado no sistema """
    return User.objects.filter(username=nome).exists()
