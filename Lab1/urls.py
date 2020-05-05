from django.urls import path
from . import views


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('links/<int:id>/', views.LinkView.as_view(), name='link'),
    path('ajax/add-visit/', views.AjaxAddVisit.as_view()),
    path('admin-statistics/', views.AdminStatistics.as_view(),name='admin-statistics'),
]