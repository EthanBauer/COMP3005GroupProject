import psycopg, csv

def main():
    try:
        connection = psycopg.connect(
            "dbname=University user=postgres "
            "password=ab12345 host=localhost port=5432"
        )
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM instructor;")
            with open('test.csv', 'w', newline='\n') as out:
                csv_out=csv.writer(out)
                data = cursor.fetchall()
                for r in data:
                    csv_out.writerow(r)

    except psycopg.OperationalError as e:
        print(f"error: {e}")
        exit(1)

main()