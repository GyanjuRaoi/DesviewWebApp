from django.urls import path
from .views import (
    RegisterView,
    login_user,
    logout_user,
    add_friend_view,


)

urlpatterns = [
    path('register/', RegisterView.as_view(), name= 'register-user' ),
    path('login/', login_user, name= 'login-user'),
    path('add/<int:profile_id>', add_friend_view, name='add-friend'),
    path('logout/', logout_user, name='logout-user')
]