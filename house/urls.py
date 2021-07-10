from django.urls.conf import path

from house.views import (
    HouseCreateView,
    HouseDeleteView,
    HouseDetailView,
    HouseFilterView,
    HouseListView,
    HouseSearchView,
    HouseUpdateView,
    HouseFavouriteListView,
    AddFavouriteView,
    DeleteFavouriteView
)

app_name = 'house'

urlpatterns = [
    path('', HouseListView.as_view(), name='home'),
    path('create/', HouseCreateView.as_view(), name='create'),
    path('house/<int:pk>/', HouseDetailView.as_view(), name='detail'),
    path('house/<int:pk>/update/', HouseUpdateView.as_view(), name='update'),
    path('house/<int:pk>/delete/', HouseDeleteView.as_view(), name='delete'),

    path('search/', HouseSearchView.as_view(), name='search'),
    path('filter/', HouseFilterView.as_view(), name='filter'),

    path('house/favourites/', HouseFavouriteListView.as_view(), name='favourites'),
    path('house/<int:pk>/favourite/', AddFavouriteView.as_view(), name='add-favourite'),
    path('house/<int:pk>/unfavourite/', DeleteFavouriteView.as_view(), name='remove-favourite'),
]
