from django.urls import path

from . import views
urlpatterns = [
    path('',views.index,name = 'realtors'),
    #path('<int:listing_id>',views.listing,name = 'realtor'),
    #path('search',views.search,name = 'search')
]