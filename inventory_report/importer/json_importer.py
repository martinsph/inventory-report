import json
# https://www.horadecodar.com.br/2021/04/17/extrair-extensao-do-arquivo-com-python/
from os.path import splitext

from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    def import_data(path):
        _, extension = splitext(path)

        if (extension != '.json'):
            raise ValueError('Arquivo inválido')

        with open(path) as file:
            products = json.load(file)

        return products


# print(JsonImporter.import_data(
#                                'inventory_report/data/inventory.json',
#                                'completo'))
