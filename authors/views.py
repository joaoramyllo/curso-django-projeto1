import re
from django.http import Http404
from django.shortcuts import render, redirect

from .forms import RegisterForm


def register_view(request): #basicamnete um mockup
    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)
    return render(request, 'authors/pages/register_view.html', {'form': form,})


def register_create(request): #vai ler os dados do post, validar, e criar o usuario e se nao estiver correto, retorna um erro
    if not request.POST:
        raise Http404()
    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterForm(POST)
    return redirect('authors:register')
