from datetime import date


# dict1 = [
#     {
#         "id": 1,
#         "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP",
#         "nome_da_empresa": "Forces of Nature",
#         "data_de_fabricacao": "2020-07-04",
#         "data_de_validade": "2023-02-09",
#         "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
#         "instrucoes_de_armazenamento": "in blandit ultrices enim",
#     },
#     {
#         "id": 2,
#         "nome_do_produto": "sodium ferric gluconate complex",
#         "nome_da_empresa": "sanofi-aventis U.S. LLC",
#         "data_de_fabricacao": "2020-05-31",
#         "data_de_validade": "2023-01-17",
#         "numero_de_serie": "SE95 2662 8860 5529 8299 2861",
#         "instrucoes_de_armazenamento": "duis bibendum morbi",
#     }
# ]


class SimpleReport():
    def generate(list):
        date_now = date.today().__str__()
        oldest_fabrication_date = list[0]["data_de_fabricacao"]
        closest_expiration_date = list[0]["data_de_validade"]
        companies_count = []

        for product in list:
            if oldest_fabrication_date >= product["data_de_fabricacao"]:
                oldest_fabrication_date = product["data_de_fabricacao"]

            if product["data_de_validade"] >= date_now:
                if product["data_de_validade"] <= closest_expiration_date:
                    closest_expiration_date = product["data_de_validade"]

            companies_count.append(product["nome_da_empresa"])

        return (
            f'Data de fabricação mais antiga: {oldest_fabrication_date}\n'
            f'Data de validade mais próxima: {closest_expiration_date}\n'
            f'Empresa com maior quantidade de produtos estocados: '
            # https://stackoverflow.com/questions/1518522/find-the-most-common-element-in-a-list
            f'{max(set(companies_count), key=companies_count.count)}\n'
        )
