from psycopg2 import sql

def listing_exists(connection, url):
    query = "SELECT EXISTS(SELECT 1 FROM property_details WHERE url = %s)"
    with connection.cursor() as cursor:
        cursor.execute(query, (url,))
        return cursor.fetchone()[0]


def insert_listing(connection, details):
    insert_query = sql.SQL("INSERT INTO property_details ({}) VALUES ({})").format(
                    sql.SQL(', ').join(map(sql.Identifier, details.keys())),
                    sql.SQL(', ').join(map(sql.Literal, details.values()))
                )
    connection.cursor().execute(insert_query)
    connection.commit()