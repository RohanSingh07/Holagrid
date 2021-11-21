from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import Signup,Signup2,LoginView,Signup3,logout_view
from django.contrib.auth import views
app_name = 'users'

urlpatterns=[
        path('signup/',Signup,name="signup"),
        path('signup/<phone>-set-username/',Signup2,name="signup2"),
        path('signup/<phone>-<username>-set-password/',Signup3,name="signup3"),
        path('login/',LoginView,name="login"),
        path('logout/',logout_view,name="logout"),

]

