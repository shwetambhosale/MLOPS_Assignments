## Screenshot

![Screenshot](https://github.com/gaurikarkhile001/MLOPS-Assignments/blob/main/Python/TASK2/images/Screenshot%202024-11-21%20133722.png)

# House Price Predictor API  

This project uses **FastAPI** to create an endpoint that predicts house prices based on user-provided features. The predictions are generated using a **Linear Regression model** built with **scikit-learn**.

---

## Features  

- **API Endpoint**: Accepts house features via a POST request and returns the predicted price.  
- **Model**: Linear Regression model trained on the **House Prices dataset**.  
- **Interactive Documentation**: Available via Swagger UI.  

---

## Installation  

1. Clone this repository:  
   ```bash
   git clone <repository-link>
   cd <repository-folder>
   ```  

2. Install dependencies:  
   ```bash
   pip install fastapi uvicorn scikit-learn pandas numpy
   ```  

3. Start the server:  
   ```bash
   uvicorn main:app --reload
   ```  

4. Access the API at:  
   - Swagger UI: `http://127.0.0.1:8000/docs`  
   - ReDoc: `http://127.0.0.1:8000/redoc`  

---

## Usage  

### Endpoint  

- **URL**: `/predict-price/`  
- **Method**: `POST`  
- **Request Body**:  
  ```json
  {
    "area": 2500,
    "bedrooms": 3,
    "bathrooms": 2,
    "stories": 2,
    "mainroad": "yes",
    "guestroom": "no",
    "basement": "yes",
    "hotwaterheating": "no",
    "airconditioning": "yes",
    "parking": 1,
    "prefarea": "no",
    "furnishingstatus": "semi-furnished"
  }
  ```  

- **Response**:  
  ```json
  {
    "predicted_price": 7659687.06
  }
  ```  

---


---

