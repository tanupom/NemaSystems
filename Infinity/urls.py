"""Infinity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path
from Pages.views import MainMenu_view
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from Pages.Stop_All_Pumps import StopAllPumpsHTML
from Pages.PreWash_Sterilization import Prewashster
print("Hello World!")
print(auth_views)
urlpatterns = [
    path('', auth_views.LoginView.as_view(), name='home'),
    # path("logout", auth_views.LoginView.as_view(), name="logout"),
    path('Infinity2.0/', MainMenu_view,name='Infinity2.0'),
    path('admin/', admin.site.urls),
    path('account/', include("django.contrib.auth.urls")),
    path('Infinity2.0/Stop_Pumps/', MainMenu_view ,name='Stop_Pumps'),
    path('Infinity2.0/StopPumpOne/', MainMenu_view ,name='Stop_Pump_One'),
    #path('Infinity2.0/StopPumpTwo/', MainMenu_view ,name='Start_Pumps'),
    #path('Infinity2.0/StopPumpThree/', MainMenu_view ,name='Start_Pumps'),
    #path('Infinity2.0/StopPumpFour/', MainMenu_view ,name='Start_Pumps'),
]
    
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)