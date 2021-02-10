from django.db import models


class Categorias(models.TextChoices):
    TECH = 'TC', 'Tecnologia'
    CR = 'CR', 'Curiosidades'
    GR = 'GR', 'Geral'


class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

class Perfil(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    especialidade = models.CharField(max_length=200, null=True, blank=True)
    endereco = models.CharField(max_length=200, null=True, blank=True)
    bairro = models.CharField(max_length=200, null=True, blank=True)
    cidade = models.CharField(max_length=200, null=True, blank=True)
    estado = models.CharField(max_length=200, null=True, blank=True)
    texto = models.TextField(null=True, blank=True)
    apresent = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    nrTelCelular = models.CharField(max_length=11, blank=True, null=True, verbose_name='Nº telefone celular')
    imagem = models.ImageField(upload_to='perfils', null=True, blank=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=200)
    content = models.TextField()
    categories = models.CharField(
        max_length=2,
        choices=Categorias.choices,
        default=Categorias.GR,
    )
    deleted = models.BooleanField(default=True)
    imagem = models.ImageField(upload_to='posts', null=True, blank=True)

    def __str__(self):
        return self.title

    def full_name(self):
        return self.title + self.sub_title

    def get_categoty_label(self):
        return self.get_categories_display()

    full_name.admin_order_field = 'title'
