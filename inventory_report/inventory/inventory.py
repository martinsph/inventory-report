import os
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory():
    def import_data(path, report_type):
        # print("teste")
        file_name, extension = os.path.splitext(path)
        if extension == ".csv":
            raw_file = CsvImporter.import_data(path)
        elif extension == ".json":
            raw_file = JsonImporter.import_data(path)
        elif extension == ".xml":
            raw_file = XmlImporter.import_data(path)

        if report_type == "simples":
            return SimpleReport.generate(raw_file)

        return CompleteReport.generate(raw_file)
