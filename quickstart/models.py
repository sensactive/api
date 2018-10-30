from django.db import models
from datetime import datetime, timedelta

class TempModel(models.Model):
    date = models.DateTimeField('Дата/Время')
    temperature = models.IntegerField('Температура')


