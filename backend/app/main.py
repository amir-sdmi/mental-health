import sys
import os
from app import create_app

# Get the absolute path of the parent directory
backend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Check if the backend path is not already in the system's path, then add it
if backend_path not in sys.path:
    sys.path.insert(0, backend_path)

# Create a new Flask app
app = create_app()

if __name__ == "__main__":
    # run the app in debug mode
    app.run(debug=True)