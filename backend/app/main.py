import sys
import os


backend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if backend_path not in sys.path:
    sys.path.insert(0, backend_path)

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)