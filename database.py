import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Apoorva@9963",  # Replace with your MySQL password
        database="doctor_assistant"
    )
