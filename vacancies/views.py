from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers


from rest_framework import views
from rest_framework.response import Response
from vacancies.models import Company, Category, Worker, Vacancy
from vacancies.serializers import (
    CompanySerializer,
    CategorySerializer,
    WorkerSerializer,
    VacancySerializer,
)

# Create your views here.
class HomePageView(views.APIView):
    @method_decorator(cache_page(60 * 60 * 2))
    def get(self, request):
        vacancies_count = Vacancy.objects.count()
        companies_count = Company.objects.count()
        workers_count = Worker.objects.count()

        return Response(
            {
                "vacancies_count": vacancies_count,
                "companies_count": companies_count,
                "workers_count": workers_count,
            }
        )
