from django.urls import path
from django.contrib import admin
from rest_framework import routers
from .views import (RegisterView, LoginView, LogoutView,UserList,SearchList,DeleteUser,
                    UpdateUser,UserDetail,UpdateProfile,Profile,Register_Restaurant,Restaurant_Retrieve,RestaurantList,
                    AddFoodType,FoodTypeList,FoodType_Retrieve,AddMenu,MenuList,Menu_Retrieve,AddReviewMenu,ListReviewMenu, ReviewMenu_Retrieve,
                    RegisterShipper,Shipper_Retrieve)

from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()

urlpatterns = router.urls

urlpatterns += [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('list_user/', UserList.as_view(), name='userlist'),
    path('search/', SearchList.as_view(), name='searchlist'),
    path('delete/', DeleteUser.as_view(), name='deletelist'),
    path('update/<uuid:pk>', UpdateUser.as_view(), name='userupdate'),
    path('retrieve/<uuid:pk>/', UserDetail.as_view(), name='userdetail'),
    path('api-token-auth/', obtain_auth_token), #gives us access to token auth
    path('update-profile/', UpdateProfile.as_view(), name='updateprofile'),
    path('profile/<uuid:pk>', Profile.as_view(), name='updateprofile'),
    path('register_restaurant/', Register_Restaurant.as_view(), name='registerrestaurant'),
    path('retrieve_restaurant/<uuid:pk>/',Restaurant_Retrieve.as_view(),name='restaurant_retrieve'),
    path('restaurant_list/',RestaurantList.as_view(),name='restaurant_list'),
    path('add_typefood/',AddFoodType.as_view(),name='add_foodtype'),
    path('list_typefood/',FoodTypeList.as_view(),name='list_foodtype'),
    path('retrieve_typefood/<uuid:pk>/',FoodType_Retrieve.as_view(),name='retrieve_foodtype'),
    path('addmenu/',AddMenu.as_view(),name='add_menu'),
    path('menulist/<uuid:pk>/',MenuList.as_view(),name='menu_list'),
    path('retrieve_menu/<uuid:pk>/',Menu_Retrieve.as_view(),name='retrieve_foodtype'),
    path('addreview/',AddReviewMenu.as_view(),name='add_reviewmenu'),
    path('list_reviewmenu/<uuid:pk>/',ListReviewMenu.as_view(),name='listreviewmenu'),
    path('retrieve_reviewmenu/<uuid:pk>/',ReviewMenu_Retrieve.as_view(),name='retrieve_reviewmenu'),
    path('register_shipper/', RegisterShipper.as_view(), name='register_shipper'),
    path('retrieve_shipper/<uuid:pk>/',Shipper_Retrieve.as_view(),name='retrieve_shipper'),






    
    








]