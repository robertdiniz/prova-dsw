from django.db import models

class Quarto(models.Model):
    apartamento = models.IntegerField("Apartamento")
    valor = models.FloatField("Valor do quarto")

class Cliente(models.Model):
    nome = models.CharField("Nome", max_length=55)
    email = models.EmailField()
    telefone = models.CharField("Telefone", max_length=15)
    endereco = models.CharField("Endereço", max_length=150)

    def __str__(self):
        return self.nome

class Hospedagem(models.Model):
    data_entrada = models.DateField("Data de entrada")
    data_saida = models.DateField("Data de saída")
    valor = models.FloatField("Valor da hospedagem")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, blank=True, null=True)
    quarto = models.ForeignKey(Quarto, on_delete=models.CASCADE, blank=True, null=True)

class Consumo(models.Model):
    nome = models.CharField("Consumo", max_length=55)
    data = models.DateField()
    valor = models.FloatField()
    hospedagem = models.ForeignKey(Hospedagem, on_delete=models.CASCADE)