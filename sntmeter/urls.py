from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'meters', views.MeterViewSet)
router.register(r'conMethods', views.ConMethodViewSet)
router.register(r'models', views.ModelViewSet)
router.register(r'vendors', views.VendorViewSet)

urlpatterns = [
    path('', views.home ,name='home'),
    path('api/', include(router.urls)),
    path('api/medidor_con/<str:con>', views.medidor_con, name='medidor_con' ),
    path('meter/', views.meter, name='meter'),
    path('report/', views.report, name='report'),
    path('ajax_ver_med',views.ajax_ver_med, name='ajax_ver_med'),
    path('ajax_lectura_simple',views.ajax_lectura_simple, name='ajax_lectura_simple'),
    path('ajax_quitar_med',views.ajax_quitar_med, name='ajax_quitar_med'),
    path('editar/<str:name>', views.ajax_editar_med, name='ajax_editar_med'),
    path('nuevo/', views.ajax_nuevo_med, name='ajax_nuevo_med'),
]