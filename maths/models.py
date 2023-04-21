from django.db import models


class Results(models.Model):
    ADD = "ADD"
    SUB = "SUB"
    MULTI = "MULTI"
    DIVIDE = "DIVIDE"

    OPERATION_CHOICES = [
        (ADD, "Add"),
        (SUB, "Sub"),
        (MULTI, "Multi"),
        (DIVIDE, "Divide"),
    ]

    num1 = models.IntegerField()
    num2 = models.IntegerField()
    result = models.FloatField()
    action = models.CharField(
        max_length=6,
        choices=OPERATION_CHOICES,
        default=ADD,
    )