from django.urls import path
from . import views

# path('<int:pk>', views.pain1, name='pain1'),

urlpatterns = [
 path('', views.fon, name='home'),
 path('sco/', views.sco, name='sco'),
 path('fonpg/', views.fonpg, name='fonpg'),
 path('index/<int:comp_id>/', views.index, name='index'),
 path('fonp/<int:comp_id>/', views.fonp, name='fonp'),
 path('poart/<int:art_id>/', views.poart, name='poart'),
 path('index02/<int:exec_id>', views.index02, name='index02')
]
