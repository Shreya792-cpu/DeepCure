// Add a new patient
document.getElementById('patientForm').addEventListener('submit', async (e) => {
  e.preventDefault();  // Prevent the form from submitting the traditional way
  
  const data = {
    name: document.getElementById('name').value,
    age: document.getElementById('age').value,
    gender: document.getElementById('gender').value,
    contact: document.getElementById('contact').value,
    medical_history: document.getElementById('medical_history').value
  };

  // Send POST request to the backend
  const response = await fetch('/api/patient', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)  // Send patient data as JSON
  });

  const result = await response.json();  // Get the response as JSON
  alert(`Patient added with ID: ${result.patient_id}`);  // Show success message
});

// Chatbot function
async function sendMessage() {
  const message = document.getElementById('chatInput').value;  // Get user's message
  if (!message) return;  // If no message, return early

  const chatbox = document.getElementById('chatbox');
  chatbox.innerHTML += `<div><strong>You:</strong> ${message}</div>`;  // Show user message

  // Send message to the chatbot API
  const response = await fetch('/api/chatbot', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message })  // Send the message to the chatbot
  });

  const botResponse = await response.json();  // Get chatbot's response as JSON
  chatbox.innerHTML += `<div><strong>Bot:</strong> ${botResponse.response}</div>`;  // Show bot response
  document.getElementById('chatInput').value = '';  // Clear the input field
}
