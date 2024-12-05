from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from .forms import UserLoginForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib import messages
# Create your views here.

class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserLoginView(LoginView):
    template_name = 'rework/login.html'
    redirect_authenticated_user = True
    authentication_form = UserLoginForm
    
    def get_success_url(self):
        return reverse_lazy('') 
    
    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))