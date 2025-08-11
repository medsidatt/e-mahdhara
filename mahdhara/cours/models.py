from django.db import models
from accounts.models import User


class Cours(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    prix = models.DecimalField(max_digits=8, decimal_places=2)
    est_gratuit = models.BooleanField(default=False)
    date_creation = models.DateTimeField(auto_now_add=True)
    createur = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role':'cheikh'})

    def __str__(self):
        return self.titre

