
import mysql.connector



class Scrapingb3Pipeline(object):
    # Connect to the MySQL database.

    def __init__(self):
        
        self.conn = mysql.connector.connect(
            host='localhost',
            port= 3307,
            user='root',
            password='root',
            database='b3'
        )

        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):

        self.cursor.execute("""
                    INSERT INTO empresas_listadas (
                        issuingCompany,
                        companyName,
                        tradingName,
                        cnpj,
                        marketIndicator,
                        typeBDR,
                        dateListing,
                        statusCompany,
                        segment,
                        segmentEng,
                        typeCompany,
                        market,
                        codeCVM
                    ) VALUES (
                        %(issuingCompany)s,
                        %(companyName)s,
                        %(tradingName)s,
                        %(cnpj)s,
                        %(marketIndicator)s,
                        %(typeBDR)s,
                        %(dateListing)s,
                        %(status)s,
                        %(segment)s,
                        %(segmentEng)s,
                        %(type)s,
                        %(market)s,
                        %(codeCVM)s
                    )
                """, item)
               
        self.conn.commit()

        return item

