from django.db import models
from crum import get_current_user
from security.models import ModelBase, ModelBaseAudited
from security.constants import Gender


class Category(ModelBase):
    code = models.CharField(max_length=10, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Categoria')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['-created_at']

    def save(self, force_insert=False, force_update=False, using=None, **kwargs):
        if self.code:
            self.code = self.code.upper()

        if self.name:
            self.name = self.name.upper()

        ModelBase.save(self)

# Create your models here.
class Custumer(ModelBaseAudited):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, blank=True, null=True)
    code = models.CharField(max_length=15, blank=True, null=True, verbose_name='Código')
    identification = models.CharField(max_length=10, blank=True, null=True, unique=True)
    first_names = models.CharField(max_length=100)
    last_names = models.CharField(max_length=100)
    names = models.CharField(max_length=191, blank=True, null=True)
    gender = models.CharField(
        verbose_name="Genero",
        choices=Gender.choices,
        default=Gender.OTHER,
        max_length=10,
    )
    city = models.CharField(max_length=100, verbose_name="Ciudad", blank=True, null=True)
    address = models.CharField(max_length=1024, verbose_name="Dirección", blank=True, null=True)
    telephone = models.CharField(max_length=20, verbose_name="Teléfono", blank=True, null=True)
    email = models.CharField(max_length=150, verbose_name="Email", blank=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.names}"

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ('-created_at',)

    def save(self, *args, **kwargs):

        if self.code:
            self.code = self.code.upper()

        if self.first_names:
            self.first_names = self.first_names.upper()

        if self.last_names:
            self.last_names = self.last_names.upper()

        if self.email:
            self.email = self.email.lower()

        self.names = f"{self.first_names} {self.last_names}".strip()

        ModelBaseAudited.save(self)

    def calculate(self):
        return None
