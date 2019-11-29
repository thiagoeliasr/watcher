from django.shortcuts import get_object_or_404, render

from .models import People

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

