"""MilitaryDB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

import MilitaryMuseum.views
from MilitaryDB import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', MilitaryMuseum.views.response_find_form),
                  path('find_form/', MilitaryMuseum.views.response_find_form, name="find"),
                  path('found_documents/', MilitaryMuseum.views.response_found_documents, name="found"),
                  path('document/<int:document_id>', MilitaryMuseum.views.response_document, name="doc"),
                  path('about/', MilitaryMuseum.views.response_about, name="about"),
                  path('about_project/', MilitaryMuseum.views.response_about_project, name="about_project")
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
