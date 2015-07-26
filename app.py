from databases.database import db_session
from databases.models import User
from flask import Flask

app = Flask(__name__)


@app.route('/abc')
def hello_world():
    u = User('admin', 'admin@localhost')
    db_session.add(u)
    db_session.commit()

    return 'Hello World!'


if __name__ == '__main__':
    
    app.debug = True
    app.run()

