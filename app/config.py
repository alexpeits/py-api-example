from dotenv import dotenv_values

dotenv = dotenv_values(".env")

DB_URI = dotenv["DB_URI"]
