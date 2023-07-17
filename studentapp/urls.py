from django.urls import path
from .import views
urlpatterns = [path('',views.f4,name='f4'),
               path('details',views.details,name='details'),
               path('show',views.show,name='show'),
               path('showdetails/<int:pk>',views.showdetails,name='showdetails'),
               path('editpage/<int:pk>',views.editpage,name='editpage'),
               path('edit_details/<int:pk>',views.edit_details,name='edit_details'),
               path('deletepage/<int:pk>',views.deletepage,name='deletepage'),

]