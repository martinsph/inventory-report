import csv
from os.path import splitext
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    def import_data(path):
        _, extension = splitext(path)

        if not path.endswith(".csv"):
            raise ValueError('Arquivo inválido')

        with open(path) as file:
            result = csv.DictReader(file, delimiter=",", quotechar='"')
            products = list(result)

        return products
