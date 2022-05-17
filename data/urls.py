from django.urls import path, include
from .views import transcriptUploadView, createView, updateView
#NOTE: Uncomment If you want to implement Facebook Login
#from posts.views import FacebookLogin


urlpatterns = [
    path('create/', createView.as_view()),
    path('update/<int:pk>',updateView.as_view()),  #use to update - PUT/PATCH, retrieve - GET, delete - DELETE
]