from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'your_password',
    'database': 'your_database'
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    password = data['password']

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    cursor.execute('SELECT * FROM users WHERE email = %s AND password = %s', (email, password))
    user = cursor.fetchone()

    if user:
        return jsonify({'success': True, 'message': 'Login successful!'})
    else:
        return jsonify({'success': False, 'message': 'Invalid credentials!'})

if __name__ == '__main__':
    app.run()
