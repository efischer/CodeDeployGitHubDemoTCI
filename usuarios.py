import json

from flask import Flask

app = Flask(__name__)

@app.route('/users')
def get_users():
    users = [
        {
            'name': 'Un ejemplo para aquitectura de Software',
            'display_name': 'Pablo Picapiedra',
            'email': 'pablo@example.com'
        }
    ]
    return json.dumps(users)

if __name__ == '__main__':
    app.run()
