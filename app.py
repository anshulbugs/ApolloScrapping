from flask import Flask, render_template, request, jsonify
from ApolloExtractor import my_selenium_module

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_selenium', methods=['POST'])
def run_selenium():
    try:
        url = request.form.get('url')
        csv_file_name = request.form.get('csv_file_name')
        csv_location = request.form.get('csv_location') 
        pages = request.form.get('pages')
        # Add logic to validate inputs if needed

        # Run the Selenium script with the provided inputs
        my_selenium_module(url, csv_file_name,csv_location,pages)

        return jsonify({'status': 'success', 'message': 'Selenium script executed successfully'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

# if __name__ == '__main__':
#     app.run(debug=True)
