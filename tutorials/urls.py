from django.urls import include, re_path 
from tutorials import views 
 
urlpatterns = [ 
    re_path (r'^api/odoo$', views.tutorial_list),
    re_path (r'^api/odoo/(?P<pk>[0-9]+)$', views.tutorial_detail),
]