import json
# https://www.horadecodar.com.br/2021/04/17/extrair-extensao-do-arquivo-com-python/
from os.path import splitext

from inventory_report.importer.importer import Importer
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class JsonImporter(Importer):
    def import_data(path, report_type):
        _, extension = splitext(path)

        if (extension != '.json'):
            raise ValueError

        with open(path) as file:
            products = json.load(file)

        if report_type == 'simples':
            report = SimpleReport.generate(products)
        elif report_type == 'completo':
            report = CompleteReport.generate(products)

        return report


# print(JsonImporter.import_data(
#                                'inventory_report/data/inventory.json',
#                                'completo'))
