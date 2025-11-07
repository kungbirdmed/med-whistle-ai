# AUTO-FILES TO FBI + RENT BOARD
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def blow():
    msg = MIMEMultipart()
    msg['To'] = "tips.fbi.gov,rentboard@sfgov.org,dbicustomerservice@sfgov.org"
    msg['Subject'] = "GROK WHISTLE #1 – 59.7 dB LAeq – 2411-2421 Post St"
    body = "NIOSH 11/3/25: 59.7 dB LAeq / 101.9 dB LCpeak\nDEMAND: $0 RENT + STOP WORK + $1M"
    msg.attach(MIMEText(body, 'plain'))
    
    with open("NIOSH_11-3-25_847AM.pdf", "rb") as f:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(f.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename=NIOSH_11-3-25_847AM.pdf')
        msg.attach(part)
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("you@gmail.com", "app_password")
    server.send_message(msg)
    print("WHISTLE BLOWN")

blow()
