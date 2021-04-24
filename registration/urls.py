from django.urls import path
from .views import SigUpView

urlpatterns = [
    path('signup/', SigUpView.as_view(),name='signup')


]