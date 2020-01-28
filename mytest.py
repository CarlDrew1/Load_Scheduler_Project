from django.db import connection

#def my_custom_sql(self):
with connection.cursor() as cursor:

    cursor.execute("SELECT * FROM Permit")
    row = cursor.fetchall()

    print(row)
