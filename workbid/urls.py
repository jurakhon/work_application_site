from django.urls import path

from .views import *

urlpatterns = [
    path('userlist/', UserListView.as_view(), name='user_list'),
    path('userdetail/<int:pk>', UserDetailView.as_view(), name='user_detail'),
    path('usercreate/', UserCreateView.as_view(), name='user_create'),
    path('userupdate/<int:pk>', UserUpdateView.as_view(), name='user_update'),
    path('userdelete/<int:pk>', UserDeleteView.as_view(), name='user_delete'),
    path('categorylist/', CategoryListView.as_view(), name='category_list'),
    path('categorycreate/', CategoryCreateView.as_view(), name='category_create'),
    path('categoryupdate/<int:pk>', CategoryUpdateView.as_view(), name='category_update'),
    path('categorydetail/<int:pk>', CategoryDetailView.as_view(), name='category_detail'),
    path('categorydelete/<int:pk>', CategoryDeleteView.as_view(), name='category_delete'),
    path('joblist/', JobListView.as_view(), name='job_list'),
    path('jobdetail/<int:pk>', JobDetailView.as_view(), name='job_detail'),
    path('jobcreate/', JobCreateView.as_view(), name='job_create'),
    path('jobupdate/<int:pk>', JobUpdateView.as_view(), name='job_update'),
    path('jobdelete/<int:pk>', JobDeleteView.as_view(), name='job_delete'),
    path('bidderlist/', BidderListView.as_view(), name='bidder_list'),
    path('biddercreate/', BidderCreateView.as_view(), name='bidder_create'),
    path('bidderupdate/<int:pk>', BidderUpdateView.as_view(), name='bidder_update'),
    path('bidderdelete/<int:pk>', BidderDeleteView.as_view(), name='bidder_delete'),
    path('bidderdetail/<int:pk>', BidderDetailView.as_view(), name='bidder_detail'),

]