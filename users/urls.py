from django.urls import path
from users.views import RegisterUserView, UpdateUserView

urlpatterns = [
  path('user/', RegisterUserView.as_view()),
  path('user/<str:id>', UpdateUserView.as_view())
]
