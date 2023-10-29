import scrapy


class EmpresaListada(scrapy.Item):
    
    issuingCompany = scrapy.Field()
    companyName = scrapy.Field()
    tradingName = scrapy.Field()
    cnpj = scrapy.Field()
    marketIndicator = scrapy.Field()
    typeBDR = scrapy.Field()
    dateListing = scrapy.Field()
    status = scrapy.Field()
    segment = scrapy.Field()
    segmentEng = scrapy.Field()
    type = scrapy.Field()
    market = scrapy.Field()
    codeCVM = scrapy.Field()
