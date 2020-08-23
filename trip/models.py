from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Trip(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    CLASSIFICATIONS = (
        (1, "Trabalho"),
        (2, "Atividade Fisica"),
        (3, "Lazer"),
        (4, "Deslocamento"),
    )
    classification = models.CharField(
        max_length=32,
        blank=True,
        null=True,
        choices=CLASSIFICATIONS,
        verbose_name="Classification",
    )
    rate = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Rate",
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )

    class Meta:
        ordering = ['-id']
        verbose_name = "Trip"
        verbose_name_plural = "Trips"

    def __str__(self):
        return self.user.email
