from django.urls import path
from .views import index, register, login, contactus, about, templateexample, templatecontext, urlparams, module, \
    module11, profiles

urlpatterns = [
    path('',index,name='home'),
path('home/',index,name='home'),
path('template/',templateexample,name='home'),
path('contexttemp/',templatecontext,name='home'),
path('urlpar/<num1>/<num2>/',urlparams),
    path('registration/',register,name='register'),
path('login/',login,name='login'),
path('contact/',contactus,name='contact'),
path('about/',about,name='about'),
    path('module/',module,name='module'),
    path('module11/',module11,name='module11'),
    path('profiles/',profiles,name='profiles'),
]