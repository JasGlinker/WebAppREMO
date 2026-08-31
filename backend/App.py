from flask import Flask, request, jsonify
from routes.createActivity import create_page

# Initializing flask app
app = Flask(__name__)

app.register_blueprint(create_page)



# Running app
if __name__ == '__main__':
    app.run(debug=True)