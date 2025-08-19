import flask
import requests

app = flask.Flask(__name__)

# Hardcoded URL to make the HTTP call
TARGET_URL = '<REDACTED>'

@app.route('/')
def hello():
    try:
        # Make a GET request to the target URL
        response = requests.get(TARGET_URL)
        print "Received Response: {}\nCode: {}".format(response.text, response.status_code)
        # Check if the request was successful
        if response.status_code == 200:
            return 'HTTP call successful! Response from {}:\n{}'.format(TARGET_URL, response.text)
        else:
            return 'Error: HTTP call failed with status code {}'.format(response.status_code)

    except requests.exceptions.RequestException as e:
        # Handle network or other request-related errors
        return 'An error occurred during the HTTP call: {}'.format(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)