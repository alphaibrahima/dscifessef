from django.db.models import Count, Q
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
#fonction qui permet de ne pas permettre aux visiteur non authentifie à un page
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import User, Profile, Page, Clube
from .forms import (RegistrationForm,
    CompanyRegistrationForm, ClubeRegistrationForm, 
    UserForm, ProfileForm, PageForm, ClubeForm)
from django.contrib.auth import login
from ..posts.models import *




def Search(request):
    queryset = User.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(username__icontains=query)#|
            #Q(bio__icontains=query)
        ).distinct()
    context = {
        'queryset': queryset
    }
    return render(request, 'blog/search_resultat.html', context)


class HomeView(TemplateView):
    template_name = 'user/home.html'

class AdminHomeView(TemplateView):
    template_name = 'user/admin_reporting.html'

class RegistrationView(CreateView):
    model = User
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'user/register.html'


class CompanyRegistrationView(CreateView):
    model = User
    form_class = CompanyRegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'user/register.html'

class ClubeRegistrationView(CreateView):
    model = User
    form_class = ClubeRegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'user/register.html'

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'user/dashboard.html'
    login_url = reverse_lazy('home')

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'user/profile.html'


class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    user_form = UserForm
    profile_form = ProfileForm
    template_name = 'user/profile_update.html'

    def post(self, request):

        post_data = request.POST or None
        file_data = request.FILES or None

        user_form = UserForm(post_data, instance=request.user)
        profile_form = ProfileForm(post_data, file_data, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Votre profile a  bien été mise à jour !')
            return HttpResponseRedirect(reverse_lazy('profile'))

        context = self.get_context_data(
                                        user_form=user_form,
                                        profile_form=profile_form
                                    )

        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    
class PageView(LoginRequiredMixin, TemplateView):
    annonce = Annonce.objects.all()
    template_name = 'user/page.html'


class PageUpdateView(LoginRequiredMixin, TemplateView):
    user_form = UserForm
    page_form = PageForm
    template_name = 'user/pageUpdate.html'

    def post(self, request):

        post_data = request.POST or None
        file_data = request.FILES or None

        user_form = UserForm(post_data, instance=request.user)
        page_form = PageForm(post_data, file_data, instance=request.user.page)

        if user_form.is_valid() and page_form.is_valid():
            user_form.save()
            page_form.save()
            messages.success(request, 'Votre page a  bien été mise à jour !')
            return HttpResponseRedirect(reverse_lazy('page'))#doit changer pour rediriger vers la page 

        context = self.get_context_data(
                                        user_form=user_form,
                                        profile_form=page_form
                                    )

        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class ClubeView(LoginRequiredMixin, TemplateView):
    template_name = 'user/page.html'


class ClubeUpdateView(LoginRequiredMixin, TemplateView):
    user_form = UserForm
    clube_form = ClubeForm
    template_name = 'user/pageUpdate.html'

    def post(self, request):

        post_data = request.POST or None
        file_data = request.FILES or None

        user_form = UserForm(post_data, instance=request.user)
        page_form = PageForm(post_data, file_data, instance=request.user.clube)

        if user_form.is_valid() and clube_form.is_valid():
            user_form.save()
            clube_form.save()
            messages.success(request, 'Votre profile a  bien été mise à jour !')
            return HttpResponseRedirect(reverse_lazy('page'))#doit changer pour rediriger vers la page 

        context = self.get_context_data(
                                        user_form=user_form,
                                        profile_form=clube_form
                                    )

        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

