from django.db import models
from django.utils import timezone
import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver

class Passageiro(models.Model):
    nome = models.CharField(max_length=100)
    passaporte = models.CharField(max_length=20)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome

class CompanhiaAerea(models.Model):
    nome = models.CharField(max_length=100)
    sede = models.CharField(max_length=100)
    website = models.URLField()

    def __str__(self):
        return self.nome

class Aeronave(models.Model):
    modelo = models.CharField(max_length=100)
    capacidade_passageiros = models.PositiveIntegerField()
    ano_fabricacao = models.PositiveIntegerField()
    companhia_aerea = models.ForeignKey(CompanhiaAerea, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.modelo} ({self.ano_fabricacao})"

class Piloto(models.Model):
    nome = models.CharField(max_length=100)
    certificado_piloto = models.CharField(max_length=20)
    aeronave_associada = models.ForeignKey(Aeronave, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome

class Comissario(models.Model):
    nome = models.CharField(max_length=100)
    certificado_comissario = models.CharField(max_length=20)
    aeronave_associada = models.ForeignKey(Aeronave, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=50)
    salario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome


class Voo(models.Model):
    passagens = models.ManyToManyField('Passagem', related_name='voos')
    status = models.CharField(max_length=20, choices=[('Agendado', 'Agendado'), ('Cancelado', 'Cancelado')])
    aeronave = models.ForeignKey(Aeronave, on_delete=models.CASCADE)
    comissario = models.ForeignKey(Comissario, on_delete=models.SET_DEFAULT, default=None, null=True, blank=True)
    origem = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    data = models.DateField(default=timezone.now)
    horario = models.TimeField(default=datetime.time(12, 0))
    valor = models.DecimalField(max_digits=10, decimal_places=2, default= 500)
    url_imagem = models.URLField(default="https://www.passagenspromo.com.br/blog/wp-content/uploads/2019/09/classes-de-voo-740x415.jpg")

class Passagem(models.Model):
    origem = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    data_viagem = models.DateField(default=timezone.now)
    data_compra = models.DateField(default=timezone.now)
    descricao = models.TextField(default="Uma experiência de viagem inesquecível aguarda você, repleta de conforto, serviços excepcionais e destinos fascinantes")
    passageiro = models.ForeignKey(Passageiro, on_delete=models.CASCADE)
    voo = models.ForeignKey(Voo, on_delete=models.CASCADE, default=1) 
    valor = models.DecimalField(max_digits=10, decimal_places=2, default= 500)
    disponivel = models.BooleanField(default=True)
    def save(self, *args, **kwargs):
        if not self.origem:
            self.origem = self.voo.origem
        if not self.destino:
            self.destino = self.voo.destino
        if not self.data_viagem:
            self.data_viagem = self.voo.data
        if not self.valor:
            self.valor = self.voo.valor
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.passageiro.nome} - {self.voo.origem} to {self.voo.destino} on {self.data_viagem}"

@receiver(post_save, sender=Passagem)
def set_default_voo(sender, instance, created, **kwargs):
    if created and not instance.voo:
        # Substitua 'default_origem', 'default_destino' e 'default_data' pelos valores desejados
        default_voo = Voo.objects.create(origem='default_origem', destino='default_destino', data='default_data')
        instance.voo = default_voo
        instance.save()

@receiver(post_save, sender=Voo)
def create_default_passagens(sender, instance, created, **kwargs):
    if created and not instance.passagens.exists():
        # Criar 20 instâncias de Passagem associadas ao Voo
        for _ in range(20):
            # Criar um novo objeto Passageiro
            novo_passageiro = Passageiro.objects.create(
                nome="", 
                passaporte="", 
                email="exemplo@email.com", 
                telefone="123456789", 
            )

            # Adicionar o novo passageiro ao Voo
            nova_passagem = instance.passagens.create(
                passageiro=novo_passageiro,
            )

            # Atualizar informações de origem, destino e data da passagem
            nova_passagem.origem = instance.origem
            nova_passagem.destino = instance.destino
            nova_passagem.data_viagem = instance.data
            nova_passagem.valor = instance.valor
            nova_passagem.save()

post_save.connect(create_default_passagens, sender=Voo)


@receiver(post_save, sender=Passagem)
def create_default_passageiro(sender, instance, created, **kwargs):
    if created and not instance.passageiro_id:
        # Crie um novo objeto Passageiro associado à Passagem
        novo_passageiro = Passageiro.objects.create(
            nome="Nome do Passageiro",  # Substitua pelo valor desejado
            passaporte="Número do Passaporte",  # Substitua pelo valor desejado
            email="exemplo@email.com",  # Substitua pelo valor desejado
            telefone="123456789",  # Substitua pelo valor desejado
        )

        # Adicione o novo passageiro ao relacionamento ForeignKey da Passagem
        instance.passageiro = novo_passageiro
        instance.save()

post_save.connect(create_default_passageiro, sender=Passagem)