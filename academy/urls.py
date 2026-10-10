from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('courses/', views.courses_view, name='courses'),
    path('course/<int:course_id>/', views.course_detail_view, name='course_detail'),
    path('enroll/', views.enroll_view, name='enroll'),
    path('contact/', views.contact_view, name='contact'),
]