from django.urls import path
from . import views

urlpatterns = [
    # path('boats/', views.boat_list, name='boat_list'),
    # path('', views.index, name='index'),
    path('boats/', views.boat_list_view, name='boat-list'),
    path('boat/<uuid:id>/', views.boat_detail, name='boat_detail'),

    path('home/', views.tours_list_view, name='tour-list'),
    path('tour/<uuid:id>/', views.tour_detail, name='tour_detail'),
]
# from main.views import index, about

# urlpatterns = [
    # path('admin/', admin.site.urls),
#     path('', index, name='home'),
#     path('about', about, name="about")
# ]
