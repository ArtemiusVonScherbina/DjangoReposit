from django.conf.urls import url
from .views import main_menu
urlpatterns = [
    url(r'^main/', main_menu)
]
