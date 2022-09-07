from flask import Flask, render_template
from mongo_server.read_mongo import read_mongo

app = Flask(__name__, template_folder='/Users/user/PycharmProjects/reboot_remote_desktop/static')
app.config["MONGO_URI"] = "mongodb://localhost:27017/test_db"


@app.route('/')
def index():
    data = read_mongo()
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)