from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('gpt1/',views.gpt1,name='gpt1'),
    path('gpt2/',views.gpt2,name='gpt2')
]