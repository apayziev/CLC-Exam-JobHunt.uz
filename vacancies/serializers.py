from vacancies.models import Company, Category, Worker, Vacancy
from rest_framework import serializers


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ("id", "name", "description")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name", "description")


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ("id", "name", "description")


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = (
            "id",
            "name",
            "description",
            "salary",
            "company",
            "category",
            "worker",
        )
