from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages

from .models import People
from .form import PeopleForm

def optout(request, token, confirm = None):
    person = get_object_or_404(People, uuid=token)

    if confirm == '1':
        person.optin = False
        person.save()

    elif confirm == '2':
        person.optin = True
        person.save()

    return render(request, 'people/optout.html', {
        'email': person.email,
        'name': person.name,
        'token': token,
        'confirm': confirm
    })

def optin(request):
    if request.method == 'POST':
        form = PeopleForm(request.POST)
        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'E-mail cadastrado com sucesso')
            else:
                messages.error(request, 'Há campos inválidos. Corrija e tente novamente')

            return redirect('/optin')
        except Exception as e:
            messages.error(request, 'Ocorreu um erro ao cadastraro o e-mail. Tente novamente')
            print(e)
    else:
        form = PeopleForm()

    return render(request, 'people/optin.html', { 'form': form })
