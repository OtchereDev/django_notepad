from django.urls import path,include
from .views import (note_list_view,
                    finish_item,
                    delete_item,
                    recover_item)


app_name='notepad'

urlpatterns = [
    path('',note_list_view),
    path('finished/<int:pk>/',finish_item,name='finish'),
    path('delete/<int:pk>/',delete_item,name='delete'),
    path('recover/<int:pk>/',recover_item,name='recover'),
]