from django.urls import path

from App import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('getticket/', views.get_ticket, name='get_ticket'),
    path('getinfo/', views.get_info, name='get_info'),
    path('setcookie/', views.set_cookie, name='set_cookie'),
    path('getcookie/', views.get_cookie, name='get_cookie'),
    path('login/', views.login, name='login'),
    path('dologin/', views.do_login, name='do_login'),
    path('mine/', views.mine, name='mine'),
    path(r'logout/', views.logout, name='logout')
]