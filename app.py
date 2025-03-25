from flask import Flask, render_template, request, jsonify
from flask_cors import CORS  # For cross-origin requests (if needed)
import mysql.connector

app = Flask(__name__)
CORS(app)  # Enable CORS if your frontend is on a different port

# Database connection function
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Apoorva@9963",
        database="doctor_assistant"
    )

# Homepage route
@app.route('/')
def home():
    return render_template('index.html')

# API endpoint to get patient details
@app.route('/api/patient/<int:patient_id>', methods=['GET'])
def get_patient(patient_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM patients WHERE patient_id = %s", (patient_id,))
    result = cursor.fetchone()
    conn.close()
    return jsonify(result)

# API endpoint to add new patient
@app.route('/api/patient', methods=['POST'])
def add_patient():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    
    query = """
    INSERT INTO patients (name, age, gender, contact, medical_history)
    VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(query, (
        data['name'], 
        data['age'], 
        data['gender'], 
        data['contact'], 
        data['medical_history']
    ))
    conn.commit()
    patient_id = cursor.lastrowid
    conn.close()
    return jsonify({"success": True, "patient_id": patient_id})

# Chatbot API endpoint
@app.route('/api/chatbot', methods=['POST'])
def chatbot():
    user_message = request.json.get('message', '').lower()
    
    # Simple response logic (replace with your actual chatbot logic)
    if 'hello' in user_message:
        response = "Hello! How can I assist you today?"
    elif 'symptom' in user_message:
        response = "Please describe your symptoms in detail."
    else:
        response = "I can help with medical queries. Ask me about symptoms or medications."
    
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Explicitly set port