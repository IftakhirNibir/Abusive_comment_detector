from django.urls import path
from . import views 

urlpatterns = [

    path('social/', views.home),
    path('',views.homepage),
    path('checker/',views.checker),
    path('pack/',views.package, name='pack'),
    path('data/', views.data),
    path('package/', views.packagepage, name='download_zip')
]