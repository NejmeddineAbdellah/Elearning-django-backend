from django.db import models


class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nom


class Enseignant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()

    # departement = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.prenom} {self.nom}{self.email}"


class Cours(models.Model):
    nom = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.code}: {self.nom} {self.enseignant} "


class Inscription(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.etudiant.nom} inscrit au cours {self.cours.nom}"

