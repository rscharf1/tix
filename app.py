from flask import Flask, json, render_template, request, jsonify
import subprocess
from os.path import exists
import csv
import tix
import smtplib, ssl
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.application import MIMEApplication

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#background process happening without any refreshing
@app.route('/create_file')
def create_file():
    print ("Create file")
    cmd = "touch test.txt"
    subprocess.call(cmd, shell=True)
    return ("nothing")

@app.route('/delete_file')
def delete_file():
    print ("Delete file")
    cmd = "rm test.txt"
    subprocess.call(cmd, shell=True)
    return ("nothing")

@app.route('/send_email')
def send_email():
    smtp_server = 'smtp.gmail.com'
    smtp_port = 465
    #Replace with your own gmail account
    gmail = 'scharf.frontrow@gmail.com'
    password = 'nutflush'

    message = MIMEMultipart('mixed')
    message['From'] = 'scharf.frontrow@gmail.com'
    message['To'] = 'rscharf33@gmail.com'
    message['Subject'] = 'Hello'

    msg_content = '<h4>Hi There,<br> This is a testing message.</h4>\n'
    body = MIMEText(msg_content, 'html')
    message.attach(body)

    attachmentPath = "pictures.pdf"
    # attachmentPath = "temp_tix/121-K-1.jpeg"
    try:
        with open(attachmentPath, "rb") as attachment:
            p = MIMEApplication(attachment.read(),_subtype="pdf")	
            p.add_header('Content-Disposition', "attachment; filename= %s" % attachmentPath.split("\\")[-1]) 
            message.attach(p)
    except Exception as e:
        print(str(e))

    msg_full = message.as_string()

    context = ssl.create_default_context()

    server = smtplib.SMTP_SSL(smtp_server, smtp_port)
    server.login(gmail, password)
    server.sendmail(gmail, "rscharf33@gmail.com", msg_full)
    server.quit()

    return ("nothing")

@app.route('/make_tix', methods=['POST', 'GET'])
def make_tix():
    print("Make tix function")
    data = request.get_json()
    print("DATA", data)

    f = open("test_input.csv", 'w')
    writer = csv.writer(f)

    writer.writerow(["home", "opponent", "date", "time", "section", "row", "seat", "entry"])
    if "-" in data["seat"]:
        r = data["seat"].split("-")
        for i in range(int(r[0]), int(r[1])+1):
            writer.writerow([data["home"], data["opponent"], data["date"], data["time"], data["section"], data["row"], i, data["entry"]])
    else:
        writer.writerow([data["home"], data["opponent"], data["date"], data["time"], data["section"], data["row"], data["seat"], data["entry"]])

    f.close()
    
    cmd = "python3 master.py"
    subprocess.call(cmd, shell=True)

    # convert *.jpg -auto-orient pictures.pdf
    cmd = "convert temp_tix/*.jpg -auto-orient pictures.pdf"
    subprocess.call(cmd, shell=True)

    send_email()

    return ("nothing")
