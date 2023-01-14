from django.db import models
from django.contrib.auth.models import User

class Raca(models.Model):
    raca = models.CharField('Raça', max_length=50)

    def __str__(self):
        return self.raca


    class Meta:
        db_table = 'Raca'
        verbose_name = 'Raça'
        verbose_name_plural = 'Raças'
        ordering = ['raca']


class Tag(models.Model):
    tag = models.CharField('Tag', max_length=100)

    def __str__(self):
        return self.tag

    class Meta:
        db_table = 'Tag'
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['tag']


class Pet(models.Model):
    choices_status = (
        ('P', 'Para Adoção'),
        ('A', 'Adotado')
    )
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Usuário')
    foto = models.ImageField('Foto', upload_to='fotos_pets')
    nome = models.CharField('Nome', max_length=100)
    descricao = models.TextField('Descrição')
    estado = models.CharField('UF', max_length=50)
    cidade = models.CharField('Cidade', max_length=50)
    telefone = models.CharField('Telefone', max_length=14)
    tags = models.ManyToManyField(Tag, verbose_name='Tag')
    raca = models.ForeignKey(Raca, on_delete=models.DO_NOTHING, verbose_name='Raça')
    status = models.CharField('Status', max_length=1, choices=choices_status)

    def __str__(self):
        return self.nome


    class Meta:
        db_table = 'Pet'
        verbose_name = 'Pet'
        verbose_name_plural = 'Pets'
        ordering = ['nome', 'raca']


