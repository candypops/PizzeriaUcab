from django.db import models

class Promo(models.Model):
    codigo = models.CharField(max_length=10)
    descuento = models.FloatField()

class Combo(models.Model):
    nombre = models.CharField(max_length=50)
    costo = models.FloatField()

class Pedido(models.Model):
    nombre = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    total = models.FloatField()
    fecha = models.DateField()
    pedido_promo = models.ForeignKey(Promo, on_delete=models.CASCADE)
    pedido_combo = models.ForeignKey(Combo, on_delete=models.CASCADE)

class Tamano(models.Model):
    tamano = models.CharField(max_length=20)
    abreviado = models.CharField(max_length=2)
    costo = models.FloatField()

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=20)
    abreviado = models.CharField(max_length=2)
    costo = models.FloatField()

class Pizza(models.Model):
    nombre = models.CharField(max_length=50)
    abreviado = models.CharField(max_length=2)
    tamano_pizza = models.ForeignKey(Tamano, on_delete=models.CASCADE)
    ingrediente_pizza = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)

class Pedido_Pizza(models.Model):
    pedido_fk = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    pizza_fk = models.ForeignKey(Pizza, on_delete=models.CASCADE)