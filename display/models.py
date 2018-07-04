import datetime

from django.db import models
from django.utils import timezone


AREA_OF_EXPERTISE_SHORT_PRINT_LIMIT = 3


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE
    )
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Country(models.Model):
    name = models.CharField(max_length=200)
    abbreviation = models.CharField(max_length=2)

    class Meta:
        verbose_name_plural = "countries"

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=200)
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name_plural = "cities"

    def __str__(self):
        return f"{self.name} ({self.country.abbreviation})"


class AreaOfExpertise(models.Model):
    name = models.CharField(max_length=200)
    subarea_of = models.ManyToManyField(
        "self",
        symmetrical=False,
        null=True,
        blank=True
    )
    description = models.TextField(
        blank = True
    )

    class Meta:
        verbose_name_plural = "areas of expertise"

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=200)
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE
    )
    areas_of_expertise = models.ManyToManyField(
        AreaOfExpertise,
        blank=True
    )

    class Meta:
        verbose_name_plural = "companies"

    def __str__(self):
        return f"{self.name} [{self.city}]"


class Member(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    city_of_residence = models.ForeignKey(
        City,
        on_delete=models.CASCADE
    )
    work_email = models.EmailField()
    private_email = models.EmailField()
    area_of_expertise = models.ManyToManyField(
        AreaOfExpertise,
        blank=True
    )
    date_joined = models.DateField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.name} {self.last_name}"


class JobDescription(models.Model):
    name = models.CharField(max_length=200)
    area_of_expertise = models.ManyToManyField(
        AreaOfExpertise
    )
    workplace = models.ForeignKey(
        Company,
        on_delete=models.CASCADE
    )
    person = models.ForeignKey(
        Member,
        on_delete=models.CASCADE
    )
    start_date = models.DateField()
    end_date = models.DateField(
        blank=True
    )

    def format_area_of_expertise(self):
        return f"({', '.join([str(item) for item in self.area_of_expertise.all()])})"

    def __str__(self):
        return f"[{self.person}] " \
               f"{self.name} " \
               f"/{self.start_date.strftime('%b %Y')} " \
               f"- {self.end_date.strftime('%b %Y')}/ " \
               f"{self.format_area_of_expertise()}"

    def short_str(self):
        return f"{self.name} " \
               f"/{self.start_date.strftime('%b %Y')} " \
               f"- {self.end_date.strftime('%b %Y')}/ " \
               f"{self.format_area_of_expertise()}"

    def workplace_str(self):
        return f"{self.workplace.name}"

    def country_str(self):
        return f"{self.workplace.city.country.abbreviation}"

    def start_date_str(self):
        return f"{self.start_date.strftime('%b %Y')}"

    def end_date_str(self):
        return f"{self.end_date.strftime('%b %Y')}"

    def area_of_expertise_str_short(self):
        if self.area_of_expertise.all().count() > AREA_OF_EXPERTISE_SHORT_PRINT_LIMIT:
            return f"{', '.join([self.area_of_expertise.all()[i].name for i in range(AREA_OF_EXPERTISE_SHORT_PRINT_LIMIT)])}"
        else:
            return f"{', '.join([expertise.name for expertise in self.area_of_expertise.all()])}"

    def name_str(self):
        return f"{self.name}"




class JobOffer(models.Model):
    name = models.CharField(max_length=200)
    area_of_expertise = models.ManyToManyField(
        AreaOfExpertise
    )
    workplace = models.ForeignKey(
        Company,
        on_delete=models.CASCADE
    )
    start_date = models.DateField()

    def __str__(self):
        return f"[{self.workplace}] self.name "
