from django.urls import path

from . import views

app_name = 'parsed_data'

urlpatterns = [
    path('s_list', views.s_list, name='s_list'),
    path('s_id_<int:s_id>/', views.s_detail, name='s_detail'),
    path('b_list', views.b_list, name='b_list'),
    path('b_id_<int:b_id>/', views.b_detail, name='b_detail'),
    path('n_list', views.n_list, name='n_list'),
    path('n_id_<int:n_id>/', views.n_detail, name='n_detail'),
]