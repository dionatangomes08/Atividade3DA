from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from .models import Funcionario

# Create your views here.
class FuncionarioCreateView(CreateView):
    model = Funcionario
    fields = "__all__"
    template_name = 'form_funcionario.html'
    success_url = "lista_funcionarios" 

class FuncionarioListView(ListView):
    model = Funcionario
    template_name = "lista_funcionarios.html"

class FuncionarioUpdateView(UpdateView):
    model = Funcionario
    fields = ("nome", "data_nascimento", "email", "remuneração")
    template_name = "form_funcionario.html"
    success_url = reverse_lazy("lista_funcionarios") 

class FuncionarioDetailView(DetailView):
    model = Funcionario
    template_name = "lista_funcionario.html"
    context_object_name = "fun" 

class FuncionarioDeleteView(DeleteView):
    model = Funcionario
    template_name = "remover_funcionario.html"
    success_url = reverse_lazy("lista_funcionarios")
    context_object_name = "fun" 

def pagina_inicial(request):
    return render(request, 'pagina_inicial.html')
