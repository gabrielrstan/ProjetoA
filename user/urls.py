from django.urls import path

from user.views import HomePageView

app_name = 'user'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),

]
