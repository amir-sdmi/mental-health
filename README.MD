# GovDat Project

## Overview

This project is part of the M604 Advanced Programming course at Gisma University of Applied Sciences. Our task is to develop a data-driven graphical user interface (GUI) to address a societal issue using data insights. The GUI integrates data from open-source repositories to provide interactive visualizations and promote informed decision-making.

## Project Structure

The project is divided into two main parts:

1. **Frontend**: Developed using React.js.
2. **Backend**: Developed using Python and Flask.

## Team Members

- Amir
- Ehsan

## Datasets

We are using two datasets for this project:

1. **Mental Health Depression Disorder Data**
2. **World Happiness Report (2005-2021)**

## Features

- Data connection to open-source repositories.
- Data preprocessing and cleaning.
- Interactive visualizations using Chart.js.
- Robust error handling.
- Unit testing for data processing and API endpoints.

## Installation

### Prerequisites

- Node.js and npm
- Python 3.x
- Git

### Frontend Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/amir-sdmi/mental-health.git
   cd mental-health/frontend
   ```
2. Install dependencies:
```bash
npm install
```

3. Run Frontend:
``` bash 
npm run dev
```
4. Install CORS extension
pleas install CORS extension to let help app work correctly, and please turn it on when you are using this app
https://chromewebstore.google.com/detail/allow-cors-access-control/lhobafahddgcelffkeicbaginigeejlf?hl=en

###
Backend Setup

1. Navigate to the backend directory:
   cd ../backend

2. Create a virtual environment:
   python -m venv venv

3. Activate the virtual environment:
   On Windows:
   .\venv\Scripts\activate
   On macOS/Linux:
   source venv/bin/activate

4. Install the required packages
   pip install -r requirements.txt

### Running the Project

## Run the Backend

Ensure the virtual environment is activated.
Navigate to the backend directory if not already there.
Run the Flask application: python app/main.py

### Running Tests

Ensure the virtual environment is activated.
Navigate to the "backend" directory if not already there.
Run the tests: pytest

### Sending Manual Requests to the Server

Ensure the backend server is running.
Enter request in your browser: http://127.0.0.1:5000/data/canada/2009/2010?Schizophrenia=true&Life-Ladder=true&GDP=true
