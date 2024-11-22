
from django.urls import path, re_path
from app import views

urlpatterns = [

    path('', views.index, name='home'),

    re_path(r'^transactions/(?:(?P<pk>\d+)/)?(?:(?P<action>\w+)/)?', views.TransactionView.as_view(),
            name='transactions'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('settings/', views.settings, name='settings'),


    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

]
