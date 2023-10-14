from fastapi import FastAPI, APIRouter
# from auth import router as auth_router
import psycopg2

# PostgreSQL connection details
db_host = "postgres"
db_port = "5432"
db_name = "postgres"
db_user = "user"
db_password = "password"

auth_router = APIRouter()
app = FastAPI()


@app.get("/")
def welcome():
    connection = psycopg2.connect(
        host=db_host,
        port=db_port,
        dbname=db_name,
        user=db_user,
        password=db_password
    )

    cursor = connection.cursor()

    cursor.execute('SELECT * FROM current_user, session_user')

    return cursor.fetchone()


# auth
app.include_router(auth_router, prefix="/auth")

# items
app.include_router(auth_router, prefix="/items")

# homepage
