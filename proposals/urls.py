
from django.urls import path, include 
from . import views


urlpatterns = [
    path('create_proposal/', views.create_proposal, name='create_proposal'),
    path('edit_proposal/<int:proposal_id>/<str:section>/', views.edit_proposal, name='edit_proposal'),
]
