from django.urls import path

from users.views import UserView

urlpatterns = [
  path('user/', UserView.as_view()),
  path('user/<str:id>', UserView.as_view())
]