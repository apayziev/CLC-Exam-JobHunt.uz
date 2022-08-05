from django.db import models
from common.models import User
from helpers.models import BaseModel

# Create your models here.
class Company(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="company", null=True, blank=True
    )

    class Meta:
        db_table = "company"
        verbose_name = "company"
        verbose_name_plural = "companies"

    def __str__(self):
        return self.name


class Category(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    class Meta:
        db_table = "category"
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Worker(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    min_salary = models.IntegerField(default=0, null=True, blank=True)
    max_salary = models.IntegerField(default=0, null=True, blank=True)

    class Meta:
        db_table = "worker"
        verbose_name = "worker"
        verbose_name_plural = "workers"

    def __str__(self):
        return self.name


class Vacancy(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="vacancies"
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="vacancies"
    )
    worker = models.ForeignKey(
        Worker, on_delete=models.CASCADE, related_name="vacancies"
    )

    class Meta:
        db_table = "vacancy"
        verbose_name = "vacancy"
        verbose_name_plural = "vacancies"

    def __str__(self):
        return self.name
