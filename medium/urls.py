from django.urls import path
from medium import views


app_name = 'medium'

urlpatterns = (

    path('<str:medium>/', views.SendMessage.as_view(), name="medium"),

)
