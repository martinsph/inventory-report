import sys
from os.path import splitext

from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def checkFileExtension(extension):
    if extension == '.csv':
        return CsvImporter
    elif extension == '.json':
        return JsonImporter
    else:
        return XmlImporter


def main():
    try:
        _, path, report_type = sys.argv

        _, extension = splitext(path)

        importer = checkFileExtension(extension)

        print(
              InventoryRefactor(importer).import_data(path, report_type),
              end='')

    except ValueError:
        print("Verifique os argumentos", file=sys.stderr)


main()
