import subprocess

# Start FastAPI backend
backend_process = subprocess.Popen(["uvicorn", "backend.main:app", "--reload"])

# Start Streamlit frontend
frontend_process = subprocess.Popen(["streamlit", "run", "frontend/app.py"])

# Wait for both processes to finish
backend_process.wait()
frontend_process.wait()
