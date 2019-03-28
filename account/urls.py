from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('memberinfo/<int:pk>/', views.MemberinfoView.as_view(), name='memberinfo'),
    path('changeinfo/<int:pk>/', views.ChangeinfoView.as_view(), name='changeinfo'),
    path('confirminfo/<int:pk>/',
         views.ConfirminfoView.as_view(), name='confirminfo'),
    path('succeed/', views.SucceedinfoView, name='succeed'),
]
