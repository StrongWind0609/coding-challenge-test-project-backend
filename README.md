# Blueshores Test Task Backend

This is a FastAPI backend application for the Blueshores test task.

## Getting Started

### Prerequisites

- Python 3.11 or higher
- Windows OS (instructions below are for Windows)

### Setup

1. **Clone the repository**

   ```cmd
   git clone <your-repo-url>
   cd blueshores_test_task\backend
   ```

2. **Create and activate a virtual environment**
   If not already created:

   ```cmd
   python -m venv myenv
   myenv\Scripts\activate.bat
   ```

   If already created, activate:

   ```cmd
   myenv\Scripts\activate.bat
   ```

3. **Install dependencies**
   ```cmd
   pip install -r requirements.txt
   ```
   If `requirements.txt` is missing, install manually:
   ```cmd
   pip install fastapi uvicorn
   ```

### Running the Application

1. **Start the FastAPI server**
   ```cmd
   uvicorn main:app --reload
   ```
   - The API will be available at: http://127.0.0.1:8000
   - Interactive docs: http://127.0.0.1:8000/docs

### Project Structure

- `main.py` — Main entry point for the FastAPI app
- `myenv/` — Python virtual environment
- `Lib/site-packages/` — Installed Python packages

### Useful Commands

- Activate venv: `myenv\Scripts\activate.bat`
- Install packages: `pip install <package>`
- Run server: `uvicorn main:app --reload`

### Troubleshooting

- If you see errors about missing packages, ensure your virtual environment is activated and run `pip install fastapi uvicorn`.
- For PowerShell, use `myenv\Scripts\Activate.ps1` to activate.

---

For any issues, please contact the project maintainer.
