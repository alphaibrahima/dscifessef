from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.views.generic import TemplateView
from apps.utilisateurs.views import (HomeView, RegistrationView, CompanyRegistrationView, 
    ClubeRegistrationView, DashboardView, ProfileUpdateView, ProfileView, PageView,
    PageUpdateView, Search, AdminHomeView)
from apps.posts.views import (PostView, AnnonceView,
    VolontariaView, PostCreation, DetailView, UpdateView, DeleteView, DetailAnnonceView,
    UpdateAnnonceView, DeleteAnnonceView, AnnonceCreation, VolontariaViewCreation,
    DetailVolontaireView, UpdateVolontaireView )
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('adminhome/', AdminHomeView.as_view(), name='adminhome'),
    path('', HomeView.as_view(), name='home'),
    path('register/', RegistrationView.as_view(), name="register"),
    path('register_company/', CompanyRegistrationView.as_view(), name="register_company"),
    path('register_clube/', ClubeRegistrationView.as_view(), name="register_clube"),
    path('login/', auth_views.LoginView.as_view(template_name = 'user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page = 'home'), name='logout'),
    path('profile-update/', ProfileUpdateView.as_view(), name='profile-update'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('page-update/', PageUpdateView.as_view(), name='page-update'),
    path('page/', PageView.as_view(), name='page'),
    path('change_password', auth_views.PasswordChangeView.as_view(template_name='user/change_password.html', success_url='/'), name='change-password'),
    #path pour la connexion avec les media sociaux 
    path('oauth/', include('social_django.urls', namespace='social')),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    #path pour la fonction reherche
    path('search/', Search, name='search'),


    #les path de lapplication posts
    path('posts/', PostView, name='posts'),
    path('create/', PostCreation, name='create'),
    path('posts/<int:id>/', DetailView, name = 'details' ),
    path('posts/<int:id>/update/', UpdateView, name = 'update' ),
    path('posts/<int:id>/delete/', DeleteView, name = 'delete' ),

    path('annonces/', AnnonceView, name='annonces'),
    path('Acreate/', AnnonceCreation, name='Acreate'),
    path('annonces/<int:id>/', DetailAnnonceView, name = 'details' ),
    path('annonces/<int:id>/update/', UpdateAnnonceView, name = 'update' ),
    path('annonces/<int:id>/delete/', DeleteAnnonceView, name = 'delete' ),

    path('volontaire/', VolontariaView, name='volontaire'),
    path('Vcreate/', VolontariaViewCreation, name='Vcreate'),
    path('volontaire/<int:id>/', DetailVolontaireView, name = 'details' ),
    path('volontaire/<int:id>/update/', UpdateVolontaireView, name = 'update' ),
    
]


from django.conf import settings
from django.conf.urls.static import static


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
