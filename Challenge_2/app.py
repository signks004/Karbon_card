from flask import Flask, request, render_template
import json
from model import probe_model_5l_profit  # Import the function

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Page 1: Upload data

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file uploaded", 400
    
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    
    if file:
        # Read the uploaded JSON file
        data = json.load(file)
        
        # Analyze the data using the model function
        results = probe_model_5l_profit(data)

        # Redirect to the results page with the analyzed data
        return render_template('results.html', results=results["flags"])

if __name__ == '__main__':
    app.run(debug=True)
