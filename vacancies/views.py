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
