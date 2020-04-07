


from django.urls import path, include

from .import views

urlpatterns = [

    path('login/', views.loginPage, name='user-login'),
    path('register/', views.signUp, name='user-signup'),
    path('staff/', views.admin, name='admin'),

    path('', views.statics, name='statics'),
    path('patientform/', views.patientForm, name='userform'),

    path('logout/', views.logoutUser, name='logout'),

    path('med/', views.medSignUp, name='med'),

    
    # path('logout/', views.logoutUser, name='logout'),
   
   
]
   
