from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import RegisterForm

# Create your views here.
def index(request):
    return render(request, 'index.html')


class RegisterFormView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
