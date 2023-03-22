from django.urls import path
from . import views
urlpatterns = [
    path('modelTest',views.modelTest,name='modelTest'),
]