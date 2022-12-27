"""hw_task_3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from api import views
from rest_framework import routers
#
# router = routers.DefaultRouter()
# router.register('product', views.ProductViewSet)
# router.register('category', views.CategoryViewSet)

urlpatterns = [
    path('api/product/', views.create_product),
    path('api/product/<int:pk>/', views.detail_product),
    path('api/category/', views.create_category),
    path('api/category/<int:pk>/', views.detail_category),
    path('api/firm/', views.create_firm),
    path('api/firm/<int:pk>/', views.detail_firm),
    path('admin/', admin.site.urls),
    # path('api/v-1.0/', include(router.urls)),
    # path('api/v-1.0/firm/', views.FirmCreateListView.as_view()),
    # path('api/v-1.0/firm/<int:pk>/', views.FirmRetrieveUpdateDestroyApiView.as_view()),

]
