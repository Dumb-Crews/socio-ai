# modify instagram.py and twitter.py as it must return json object and image / video download should begin in background

from flask import Flask, jsonify, request
from main import download_from_url
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

@app.route('/api/url', methods=['POST'])
def greet():
    try:
        url = request.json.get('url')  # Access the URL from JSON
        print(f'\n\nurl------{url}\n\n')
        if not url:
            return jsonify({"error": "URL is required"}), 400

        print(f"{url} from app.py")
        result = download_from_url(url)
        if result is None:
            return jsonify({"error": "Invalid URL format"}), 400

        if "error" in result:
            return jsonify(result), 500
        else:
            return jsonify(result), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    # Run the server
    app.run(debug=False)
    app.run(port=port)
