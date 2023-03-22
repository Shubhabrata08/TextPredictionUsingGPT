from django.urls import path
from . import views
urlpatterns = [
    path('apiTest',views.getData,name='getData'),
    path('modelTest',views.modelTest,name='modelTest')
]