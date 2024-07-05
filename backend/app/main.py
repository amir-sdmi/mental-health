import sys
import os

print(sys.path)

# Determine the current file's directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory of `app` to the system path
backend_path = os.path.abspath(os.path.join(current_dir, '..'))
if backend_path not in sys.path:
    sys.path.insert(0, backend_path)


from app import create_app

# Create a new Flask app
app = create_app()

if __name__ == "__main__":
    # Run the app in debug mode
    app.run(debug=True)
