from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgres://btdb_user:ALZcuvXRdp1JTbE8uq3WMQmCZMzGoc0y@dpg-cj4766l9aq047cak6930-a/btdb")
    conn.close()
    return 'Database Connection Successful'