# week-2-level-4-python-flask
Flask API Project
Routes in this API
GET /status  
Returns a JSON message to show the API is working.

GET /hello/<name>  
Takes a name in the URL and returns a greeting.
Example: /hello/Alex

POST /add  
Accepts JSON with two numbers and returns their sum.
Example body:

json
{ "a": 5, "b": 7 }
How to Run the Server
Install Flask

Code
pip install flask
Run the app

Code
python app.py
The server will start at
http://127.0.0.1:5000 (127.0.0.1 in Bing)

How to Test a Route (Example Using Postman)
Testing the POST /add route
Open Postman

Select POST

Enter URL:
http://127.0.0.1:5000/add

Go to Body → raw → JSON

Paste this:

json
{ "a": 10, "b": 20 }
Click Send

You should see:

json
{ "result": 30 }