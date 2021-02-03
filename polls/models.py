from django.db import models

class Promo(models.Model):
    codigo = models.CharField(max_length=10)
    descuento = models.FloatField()

class Pedido(models.Model):
    nombre = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    total = models.FloatField()
    fecha = models.DateField()
    pedido_promo = models.ForeignKey(Promo, on_delete=models.CASCADE, null=True)

class Combo(models.Model):
    nombre = models.CharField(max_length=50)
    costo = models.FloatField()

    def __str__(self):
        return self.nombre

class Pedido_Combo(models.Model):
    pedido_cfk = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    combo_cfk = models.ForeignKey(Combo, on_delete=models.CASCADE)

class Tamano(models.Model):
    tamano = models.CharField(max_length=20)
    abreviado = models.CharField(max_length=2)
    costo = models.FloatField()

    def __str__(self):
        return self.tamano

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=20)
    abreviado = models.CharField(max_length=2)
    costo = models.FloatField()

    def __str__(self):
        return self.nombre

    def __float__(self):
        return self.costo


class Pedido_Pizza(models.Model):
    pedido_fk = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    pizza_fk = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    tamano_pizza = models.ForeignKey(Tamano, on_delete=models.CASCADE)