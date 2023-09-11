from flask import Flask, request, jsonify
from datetime import datetime, timedelta
import pytz

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_info():
    # Get query parameters
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Get the current UTC time with a +/-2 minute window
    current_utc_time = datetime.now(pytz.utc)
    utc_time_formatted = current_utc_time.strftime("%Y-%m-%dT%H:%M:%SZ")

    # Get the current day of the week
    current_day = current_utc_time.strftime("%A")

    # Define GitHub URLs
    github_file_url = "https://github.com/username/repo/blob/main/file_name.ext"
    github_repo_url = "https://github.com/username/repo"

    # Response JSON
    response_json = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time_formatted,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    return jsonify(response_json)

if __name__ == '__main__':
    app.run(debug=True)
