# DataFlow Analyzer

**DataFlow Analyzer** is an AI-powered developer tool for Data Analysts designed to monitor data pipelines, detect anomalies, and validate data in real-time. Built with **Flask** for the backend and **Angular** for the frontend, this project demonstrates a fully functional prototype of a data pipeline monitoring tool.

---

## Features (Current Implementation)

- **Backend (Flask)**  
  `/train` endpoint: trains a simple ML anomaly detection model on sample data.  
  `/detect` endpoint: detects whether a given data point is an anomaly.  
  CORS enabled for integration with Angular frontend.  
  Structured with `services/`, `models/`, `utils/` directories for modularity.

- **Frontend (Angular, standalone components)**  
  `AppComponent`: main application wrapper.  
  `DashboardComponent`: displays buttons for training the model and detecting anomalies.  
  `ApiService`: communicates with the Flask backend via HTTP requests.  
  JSON responses displayed dynamically on the dashboard.  
  Fully functional button interactions with live backend responses.

---

## Getting Started

### Prerequisites

Python 3.10+, Node.js 20+ / npm 10+, Angular CLI 17+

### Backend Setup

Navigate to the backend folder, 
create a virtual environment, 
activate it, 
install dependencies with `pip install -r requirements.txt`, 
and run the Flask backend with `python app.py`. 
The backend will run at `http://127.0.0.1:5000` with `/train` and `/detect` endpoints accessible.

### Frontend Setup

Navigate to the frontend folder, 
install dependencies with `npm install`, 
and run the Angular frontend with `ng serve`. 
Open `http://localhost:4200` in your browser to see **DataFlow Analyzer** and the **Dashboard** with buttons for training and detecting points.

---

### Usage

Click **Train Model** to send sample data to the backend `/train` endpoint. Click **Detect Point** to send a sample point to the backend `/detect` endpoint. 
JSON responses are displayed below each button.

---

### Project Structure
```
dataflow-analyzer/
├─ backend/
│ ├─ app.py
│ ├─ services/
│ ├─ models/
│ ├─ utils/
│ └─ requirements.txt
├─ frontend/
│ ├─ src/app/
│ │ ├─ app.component.ts
│ │ ├─ components/dashboard/dashboard.component.ts
│ │ └─ services/api.service.ts
│ ├─ angular.json
│ └─ package.json
├─ .gitignore
└─ README.md
```
### Notes

Frontend communicates with backend at `http://127.0.0.1:5000`. Update `ApiService` if the backend URL changes. Currently, training and detection use **hardcoded sample data**. User input and more advanced ML models will be added in future updates. CORS is enabled in the backend to allow requests from the frontend.
