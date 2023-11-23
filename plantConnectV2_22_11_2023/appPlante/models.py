from django.db import models

from django.db import models

class Salle(models.Model):
    nom_salle = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.nom_salle

class Node(models.Model):
    num_node = models.CharField(max_length=100, null=True)
    id_salle = models.ForeignKey(Salle, on_delete=models.CASCADE)

    def __str__(self):
        return self.num_node

class Plante(models.Model):
    type_plante = models.CharField(max_length=30, null=True)
    id_node = models.ForeignKey(Node, on_delete=models.CASCADE)

    def __str__(self):
        return self.type_plante

class Measure(models.Model):
    temp = models.DecimalField(max_digits=2, decimal_places=2, null=True)
    humidity = models.DecimalField(max_digits=2, decimal_places=2, null=True)
    light = models.DecimalField(max_digits=2, decimal_places=2, null=True)
    moisture = models.IntegerField(null=True)
    datetime = models.DateTimeField(auto_now_add=True, null=True)
    id_node = models.ForeignKey(Node, on_delete=models.CASCADE)

    def __str__(self):
        return f"Measure - {self.datetime}"