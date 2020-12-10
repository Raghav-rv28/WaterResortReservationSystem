"""mod3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from pages.views import home_view, contact_view, services_view, hotel_view, blog_view
from hotels import views

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),

    path('contact/', contact_view, name='contact'),
    path('services/', services_view, name='services'),
    path('blog/', blog_view, name='blog'),
    path('hotel/', hotel_view, name='hotel'),

    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.register, name='register'),

    path('booking/', include('hotels.urls')),
    path("book/<obj_id>", views.book, name='book'),
    path("search", views.search, name='search'),
    path("confirm", views.confirm, name='confirm'),
    path("payment", views.payment, name='payment'),
    path("success", views.success, name='success'),
    path("cancel", views.cancel, name='cancel'),

]

urlpatterns = urlpatterns + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
