import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from actors.models import Actor

class Command(BaseCommand):
    help = 'Comando para importar atores para alimentar o banco de dados'

    def add_arguments(self, parser):
        parser.add_argument(
            'file_name',
            type=str,
            help='Recebe um arquivo e volta o nome dele'
        )

    def handle(self, *args, **options):
        file_name = options['file_name']
        with open(file_name, 'r', encoding='utf-8') as file_name:
            reader = csv.DictReader(file_name)
            for row in reader:
                name = row['name']
                age = row['age']
                character_name = row['character_name']
                birthday = datetime.strptime(row['birthday'], '%Y-%m-%d').date()
                nationality = row['nationality']

                self.stdout.write(self.style.NOTICE(name))

                Actor.objects.create(
                    name=name,
                    age=age,
                    character_name=character_name,
                    birthday=birthday,
                    nationality=nationality
                )

        self.stdout.write(self.style.SUCCESS('Atores cadastrado com sucesso no banco de dados!'))
