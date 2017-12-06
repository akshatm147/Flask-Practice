from flask import *
from flask_mail import Mail, Message

app = Flask(__name__)

app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 587,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = '*******@gmail.com',
    MAIL_PASSWORD = '*****',
))

mail = Mail(app)

@app.route('/')
def index():
    msg = Message('Hello', sender='abc4267xyz@gmail.com', recipients=['akshat14714@gmail.com'])
    msg.body = "Hello Flask message sent from Flask-Mail"
    mail.send(msg)
    return 'Sent'

if __name__ == '__main__':
    app.run(debug=True)
