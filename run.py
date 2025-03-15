import subprocess
import time
import signal
import sys

def start_backend():
    """Starts the FastAPI backend using uvicorn."""
    return subprocess.Popen(["uvicorn", "backend.main:app", "--reload"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def start_frontend():
    """Starts the Streamlit frontend."""
    return subprocess.Popen(["streamlit", "run", "frontend/app.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def terminate_processes(backend_process, frontend_process):
    """Terminates both backend and frontend processes safely."""
    print("\nShutting down...")
    if backend_process:
        backend_process.terminate()
        backend_process.wait()
    if frontend_process:
        frontend_process.terminate()
        frontend_process.wait()
    print("Processes terminated. Exiting.")

def main():
    """Centralized function to run both backend and frontend."""
    print("Starting FastAPI backend...")
    backend_process = start_backend()

    # Wait a bit to ensure backend starts before frontend
    time.sleep(3)

    print("Starting Streamlit frontend...")
    frontend_process = start_frontend()

    # Handle Ctrl+C or termination signal
    try:
        while True:
            time.sleep(1)  # Keep script running
    except KeyboardInterrupt:
        terminate_processes(backend_process, frontend_process)
        sys.exit(0)

if __name__ == "__main__":
    main()
