from django.urls import path
from vacancies.views import HomePageView


urlpatterns = [
    path("", HomePageView.as_view(), name="home_page"),
]
