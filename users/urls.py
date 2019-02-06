from django.urls import path
from .views import *

urlpatterns = [
    path('id/<user_id>/', UserInfoID.as_view()),
    path('create/', CreateUser.as_view()),
]
