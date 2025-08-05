# MyAngularApp (Angular + Flask)

This project consists of a frontend built with Angular and a backend API built with Flask.  
It includes a contact form that sends user input to the server, which saves the message in a JSON file.

---

## 📁 Project Structure

my-angular-app/
├── frontend/ # Angular project (your current Angular app)
│ ├── src/
│ │ └── app/
│ └── ...
├── backend/ # Flask project (API server)
│ ├── app.py
│ └── messages.json # (auto-created when messages are saved)  
---

## 🚀 Run the Angular Frontend

```bash
cd frontend
npm install
ng serve
http://localhost:4200
cd backend
pip install -r requirements.txt
python app.py
http://localhost:5000
📬 Test the Contact Form
Go to http://localhost:4200

Fill out the contact form (name, email, message)

Click Send

The Angular app sends a POST request to:

bash
Kopieren
Bearbeiten
http://localhost:5000/api/contact
The Flask backend saves the data into messages.json

The Angular app shows the server response

🧪 Run Angular Unit Tests
bash
Kopieren
Bearbeiten
ng test
Runs Karma tests with live reloading.

📦 Build Angular for Production
bash
Kopieren
Bearbeiten
ng build
This command builds the app for production and puts the output into the dist/ folder.

🛠️ Generate New Angular Components
bash
Kopieren
Bearbeiten
ng generate component my-new-component
You can also use:

bash
Kopieren
Bearbeiten
ng g c my-new-component
📚 Useful Links
Angular CLI Docs

Flask Docs

GitHub Repository

Created by Ali-Sra

yaml
Kopieren
Bearbeiten

---

✅ Let me know if you also want a **Persian version**, or a downloadable `.md` file!







ChatGPT fragen
