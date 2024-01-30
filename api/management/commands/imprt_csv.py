import csv
from django.core.management.base import BaseCommand

from api.models import Product


class Command(BaseCommand):
    help="import data"

    def add_arguments(self, parser):
        parser.add_argument('csv_file',type=str,help="C:/Users/amart/PycharmProjects/Product_review/dataset.csv")


    def handle(self, *args, **options):
        csv_file_path=options['csv_file']
        with open("C:/Users/amart/Downloads/dataset.csv", 'r',encoding='latin-1') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # print(row)
                Product.objects.create(**row)

        self.stdout.write(self.style.SUCCESS('data imported'))