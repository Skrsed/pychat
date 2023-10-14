import psycopg2

# PostgreSQL connection details
db_host = "localhost"
db_port = "5432"
db_name = "postgres"
db_user = "user@domain.com"
db_password = "secret"


class Pg:
    connection = None

    def get_cursor(self) -> psycopg2.connection:
        if self.connection is not None:
            return self.connection

        connection = psycopg2.connect(
            host=db_host,
            port=db_port,
            dbname=db_name,
            user=db_user,
            password=db_password
        )

        return connection.cursor()
