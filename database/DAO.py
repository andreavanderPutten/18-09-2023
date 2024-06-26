from database.DB_connect import DBConnect


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAnni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct(year(gds.Date)) as anno
                    from go_sales.go_daily_sales gds """

        cursor.execute(query, )

        for row in cursor:
            result.append(row["anno"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getNazioni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct Country 
                    from go_retailers  """

        cursor.execute(query)

        for row in cursor:
            result.append((row["Country"]))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getNodi(nazione):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
        from go_retailers as gr 
        where gr.Country = %s"""

        cursor.execute(query)

        for row in cursor:
            result.append((row["Retailer_code"],["Retailer_name"]))

        cursor.close()
        conn.close()
        return result
    @staticmethod
    def getArchi(anno,venditore1,venditore2):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select gds1.Retailer_code as ven1, gds2.Retailer_code as ven2, count(distinct gds1.Product_number) as peso
        from go_sales.go_daily_sales gds1, go_sales.go_daily_sales gds2
        where gds1.Retailer_code = 1201 and gds2.Retailer_code = 1205 and year(gds1.Date) = 2015 
        and year(gds1.Date) = year(gds2.Date) and gds1.Product_number = gds2.Product_number 
        group by ven1, ven2  """

        cursor.execute(query)

        for row in cursor:
            result.append((row["ret1"], ["ret2"], ["Peso"]))

        cursor.close()
        conn.close()
        return result