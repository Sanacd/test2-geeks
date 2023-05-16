from . import views
from django.urls import path

urlpatterns = [
    path('',views.portfolio,name='portfolio'),
    path('testimonials',views.testimonials,name='testimonials'),
    path('projects',views.projects,name='projects')
]