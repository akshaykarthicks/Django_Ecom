from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path("login/",views.login_user,name="login"),
    path("register/",views.register_user,name="register"),
    path("logout/",views.logout_user,name="logout"),
    path("product/<int:pk>/",views.product_detail,name="product"), #product page
    path('category/<str:cn>/',views.category,name='category'),
    path('category_summary/',views.category_summary,name='category_summary'),
    path('update_user/',views.update_user,name='update_user'),
    path('update_password/',views.update_password,name='update_password'),

]