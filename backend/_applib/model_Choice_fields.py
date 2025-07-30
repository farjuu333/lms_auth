from django.db import models


class TeacherStatus(models.TextChoices):
    PENDING='PENDING'
    APPROVED='APPROVED'
    DELETED='DELETED'
    

class Genderchoice(models.TextChoices):
    MALE='MALE'
    FEMALE='FEMALE'
    OTHER='OTHER'
