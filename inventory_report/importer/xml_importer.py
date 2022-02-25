# https://linuxhint.com/python_xml_to_dictionary/
import xmltodict
# https://www.horadecodar.com.br/2021/04/17/extrair-extensao-do-arquivo-com-python/
from os.path import splitext

from inventory_report.importer.importer import Importer
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class XmlImporter(Importer):
    def import_data(path, report_type):
        _, extension = splitext(path)

        if (extension != '.xml'):
            raise ValueError

        with open(path) as file:
            content = file.read()
            records = xmltodict.parse(content)['dataset']['record']
            records_items = [list(record.items())
                             for record in records]
            # https://www.google.com/amp/s/www.geeksforgeeks.org/python-convert-a-list-to-dictionary/amp/
            products = [dict(record_items)
                        for record_items in records_items]

        if report_type == 'simples':
            report = SimpleReport.generate(products)
        elif report_type == 'completo':
            report = CompleteReport.generate(products)

        return report


# print(XmlImporter.import_data(
#                               'inventory_report/data/inventory.xml',
#                               'completo'))
