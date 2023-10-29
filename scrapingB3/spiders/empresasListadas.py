import json
import scrapy


class EmpresaslistadasSpider(scrapy.Spider):
    name = "empresasListadas"
    start_urls = [
        'https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyCall/GetInitialCompanies/eyJsYW5ndWFnZSI6InB0LWJyIiwicGFnZU51bWJlciI6MSwicGFnZVNpemUiOjJ9'
    ]

    def parse(self, response):
        try:
            data = json.loads(response.body)
            for item in data['results']:
                yield {
                    'issuingCompany': item['issuingCompany'],
                    'companyName': item['companyName'],
                    'tradingName': item['tradingName'],
                    'cnpj': item['cnpj'],
                    'marketIndicator': item['marketIndicator'],
                    'typeBDR': item['typeBDR'],
                    'dateListing': item['dateListing'],
                    'status': item['status'],
                    'segment': item['segment'],
                    'segmentEng': item['segmentEng'],
                    'type': item['type'],
                    'market': item['market'],
                    'codeCVM': item['codeCVM'],
                }
            return item
        except json.JSONDecodeError:
            self.logger.error('Erro ao decodificar JSON na resposta.')
