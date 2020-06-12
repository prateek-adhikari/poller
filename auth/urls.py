from django.urls import path
from auth.views import Login,Logout
urlpatterns = [
    path('login/', Login.as_view(), name="auth_login"),
    path('logout/', Logout.as_view(), name="auth_logout"),
]