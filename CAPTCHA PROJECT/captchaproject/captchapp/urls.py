from.import views 
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('submit',views.submit,name='submit')
]

    # Add other URLs as needed


