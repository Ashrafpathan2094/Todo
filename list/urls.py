
from django.urls import path,include

from list.views import TodosView

urlpatterns = [path('list/',TodosView.as_view(),name='lists'),
   
]
