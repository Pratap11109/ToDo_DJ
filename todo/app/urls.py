from django.urls import path,include
from .views import home, SignupView, LoginView,ProfileView,logout_view,AddView, UpdatTodoView,ToDoDeleteView
urlpatterns = [
    path("",home,name="home"),
    path("login/",LoginView.as_view(),name="login"),
    path("logout/",logout_view,name="logout"),
    path("signup/",SignupView.as_view(),name="signup"),
    path("profile/",ProfileView.as_view(),name="profile"),
    path("update/<int:pk>",UpdatTodoView.as_view(),name="update"),
    path("add/",AddView.as_view(),name="add"),
    path("delete/<int:pk>",ToDoDeleteView.as_view(),name="delete"),
]
