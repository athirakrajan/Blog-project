from django.urls import path
from.import views

urlpatterns = [
    
    path('',views.home,name='home'),
    path('blogpage/',views.blogpage,name='blogpage'),
    path('addblog/',views.addblog,name='addblog'),
    path('signin/',views.signin,name='signin'),
    path('signup/',views.signup,name='signup'),
    path('like/<int:Blog_id>/like/',views.like,name='like'),
    path('viewmyblog',views.viewmyblog,name="viewmyblog"),
    path('deleteblog/<int:pk>',views.deleteblog,name="deleteblog"),
    path('editpage/<int:vid>',views.editpage,name="editpage"),
    path('signout/',views.signout,name='signout'),
    
]