from flask import Flask
from controller import main


app = Flask(__name__, template_folder="views")

app.register_blueprint(main)

if __name__ == '__main__':
    app.run(debug=True, port=3000)