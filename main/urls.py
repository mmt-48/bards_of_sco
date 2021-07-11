from django.urls import path
from . import views

# path('<int:pk>', views.pain1, name='pain1'),

urlpatterns = [
 path('', views.index01, name='home'),
 path('index/<int:comp_id>/', views.index, name='index'),
 path('index02/<int:exec_id>/', views.index02, name='index02')
]
