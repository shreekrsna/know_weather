from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get user details
    name = "Shreekrishna G S"  # Replace with your actual name
    username = os.getenv("USER") or os.getenv("USERNAME") or "codespace"

    # Get Server Time in IST
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)

    # Get top output
    top_output = subprocess.getoutput("top -bn1")

    return f"""
    <h2>Name: {name}</h2>
    <h3>User: {username}</h3>
    <h3>Server Time (IST): {ist_time}</h3>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
