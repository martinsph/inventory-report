from collections import Counter

from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(list):
        simple_report = SimpleReport.generate(list)

        # https://stackoverflow.com/questions/18940540/how-can-i-count-the-occurrences-of-an-item-in-a-list-of-dictionaries
        products_quantity_by_company = Counter(product.get('nome_da_empresa')
                                               for product in list)

        report_lines = [f'- {key}: {value}\n'
                        for key, value in products_quantity_by_company.items()]

        complete_report = (simple_report +
                           '\nProdutos estocados por empresa: \n' +
                           ''.join(report_lines))

        return complete_report
