from django.db import models


NATIONALITY_CHOICES = (
    ('USA', 'Estados Unidos'),
    ('BRAZIL', 'Brasil'),
    ('JAPAN', 'Japão'),
    ('UK', 'Reino Unido'),
    ('GERMANY', 'Alemanha'),
    ('BELGIUM', 'Bélgica'),
    ('FRANCE', 'França'),
    ('CANADA', 'Cánada')

)


class Actor(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    character_name = models.CharField(max_length=200, null=True, blank=True)
    birthday = models.DateField()
    nationality = models.CharField(
        max_length=100,
        choices=NATIONALITY_CHOICES,
        blank=True,
        null=True)

    def __str__(self):
        return self.name
