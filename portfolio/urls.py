from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", views.index, name="index"),
    path("index/", views.index, name="index"),
    path("home/", views.index, name="index"),  # Keep for backward compatibility
    path("hobbies/", views.hobbies, name="Hobbies"),
    path("portfolio/", views.portfolio, name="portfolio"),
    path("hobbies/<int:pk>", views.hobby_details, name="hobby_details"),
    path("portfolio/<int:pk>", views.portfolio_details, name="portfolio_details"),
    path('portfolio/add/', views.portfolio_add, name='portfolio_add'),
    path('portfolio/<int:pk>/edit/', views.portfolio_edit, name='portfolio_edit'),
    path('portfolio/<int:pk>/delete/', views.portfolio_delete, name='portfolio_delete'),
    path('contact/', views.contact_view, name='contact'),
    path('contact/success/', views.contact_success, name='contact_success'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)