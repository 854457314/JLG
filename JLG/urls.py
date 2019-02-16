from django.conf.urls import url

from JLG import views

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^register/$',views.register,name='register'),
    url(r'^entry/$',views.entry,name='entry'),
]