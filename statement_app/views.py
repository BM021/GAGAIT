from django.shortcuts import render, redirect
from . import models

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

from .models import Statements


def get_exact_statement(request, pk):
    exact_statement = models.Statements.objects.get(client_inn=pk)

    return render(request, 'statement_app/exact_statement.html', {'exact_statement': exact_statement})


def search_exact_statement(request):
    if request.method == 'POST':
        get_statement = request.POST.get('search-statement')

        try:
            models.Statements.objects.filter(client_inn=get_statement)

            return redirect(f"/exact_statement/{get_statement}")

        except:
            return redirect('main_page')


class CustomLoginView(LoginView):
    template_name = 'statement_app/registration/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('main_page')


class MainPage(LoginRequiredMixin, ListView):
    model = Statements
    context_object_name = 'all_statements'


class StatementDetail(LoginRequiredMixin, DetailView):
    model = Statements
    context_object_name = 'exact_statement'
    template_name = 'statement_app/exact_statement.html'


def create_statement(request):
    print(request)
    if request.method == 'POST':
        print(request)
        models.Statements.objects.create(user_added_statement=request.user,
                                         client_inn=request.POST.get('inn'),
                                         client_company_name=request.POST.get('company_name'),
                                         client_device_number=request.POST.get('device_number'),
                                         client_modul_number=request.POST.get('modul_number'),
                                         client_number=request.POST.get('client_number'),
                                         client_address=request.POST.get('client_address'),
                                         client_single_window_statement=request.POST.get('client_single_window_statement'),
                                         client_statement=request.POST.get('client_statement'),
                                         description=request.POST.get('description'))

    else:
        print('Error')

    return render(request, 'statement_app/statements_form.html')


class UpdateStatement(LoginRequiredMixin, UpdateView):
    model = Statements
    fields = '__all__'
    success_url = reverse_lazy('main_page')


class DeleteStatement(LoginRequiredMixin, DeleteView):
    model = Statements
    context_object_name = 'exact_statement'
    success_url = reverse_lazy('main_page')
