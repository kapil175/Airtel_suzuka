from flask import Flask, render_template
from datetime import datetime
import pytz
import json

app = Flask(__name__)

# Define time zones
TIME_ZONES = {
    'UTC': 'UTC',
    'IST (India)': 'Asia/Kolkata',
    'EST (US)': 'US/Eastern',
    'PST (US)': 'US/Pacific',
    'GMT (UK)': 'Europe/London',
    'JST (Japan)': 'Asia/Tokyo',
    'AEST (Australia)': 'Australia/Sydney'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/time')
def get_time():
    """API endpoint to get current time in all timezones"""
    times = {}
    
    for tz_name, tz_code in TIME_ZONES.items():
        try:
            tz = pytz.timezone(tz_code)
            current_time = datetime.now(tz)
            times[tz_name] = {
                'time': current_time.strftime("%H:%M:%S"),
                'date': current_time.strftime("%A, %B %d, %Y"),
                'offset': current_time.strftime("%z")
            }
        except Exception as e:
            times[tz_name] = {'error': str(e)}
    
    return json.dumps(times)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
