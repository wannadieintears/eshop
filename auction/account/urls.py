from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.index, name='account'),
    path('myacc', views.auth, name='myacc'),
    path('reg', views.RegistrationView.as_view(), name='reg'),
    path('newpost', views.Newpost.as_view(), name='newpost'),
]