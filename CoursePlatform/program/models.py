from uuid import uuid4

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models, IntegrityError
from django.template.defaultfilters import slugify


class Course(models.Model):
    title = models.CharField(primary_key=True, max_length=255, verbose_name='Название курса')
    description = models.TextField(blank=True, verbose_name='Краткое содержание курса')
    average_time = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(50)],
                                               verbose_name='Общее количество часов')
    slug = models.SlugField(unique=True,blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f' {self.title}')

        while True:
            try:
                super().save(*args, **kwargs)
                break
            except IntegrityError:
                self.slug = f'{self.slug}-{str(uuid4())[:8]}'
        return super().save()


class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True,
                               verbose_name='Название курса',
                               related_name='course')
    title = models.CharField(max_length=255, verbose_name='наименование модуля',)
    description = models.CharField(max_length=1500, blank=True, verbose_name='Характеристика модуля')
    average_time = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(50)],
                                               verbose_name='Общее количество часов', null=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return (f'{self.course} - {self.title}')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f' {self.title}')

        while True:
            try:
                super().save(*args, **kwargs)
                break
            except IntegrityError:
                self.slug = f'{self.slug}-{str(uuid4())[:8]}'
        return super().save()




class Lesson(models.Model):
    module = models.ForeignKey(Module, on_delete=models.SET_NULL, null=True,
                               verbose_name='Номер модуля', related_name='module')
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, verbose_name="Характеристика урока")
    duration_time = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(250)],
                                                verbose_name='Продолжительность урока')
    slug = models.SlugField(unique=True, max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.module} - {self.title}'

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(f'{self.module} - {self.title}')
        return super().save()






