from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLES = (
        ('admin', 'Administrateur'),
        ('cheikh', 'Cheikh'),
        ('etudiant', 'Étudiant'),
    )

    role = models.CharField(max_length=10, choices=ROLES, default='etudiant')

    def est_inscrit(self, cours):
        return self.inscriptions.filter(cours=cours).exists()
