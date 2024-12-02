# FastAPI Project

## Setup Instructions

1. Create a virtual environment for the project:
   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

3. Install FastAPI and Uvicorn:
   ```bash
   pip install fastapi uvicorn
   ```

## Running the FastAPI Application

1. Navigate to the `app` directory:
   ```bash
   cd app
   ```

2. Run the FastAPI application using Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```

3. Open your browser and go to `http://127.0.0.1:8000` to see the "Hello World" message.

## Testing Instructions

You can test the "Hello World" endpoint using curl:

```bash
curl -X GET "http://127.0.0.1:8000/"
```
