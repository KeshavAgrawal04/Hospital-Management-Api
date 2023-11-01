from icalendar import Calendar, Event
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

smtp_server = "smtp.gmail.com"
smtp_port = 587  
smtp_username = "agrkeshav04@gmail.com"
smtp_password = "iqcbexiduucluazm"

def send_email_to_client(data):
    cal = Calendar()
    event = Event()
    event.add('summary', 'Appointment')
    event.add('dtstart', datetime(2023, 10, 31, 8, 0, 0))
    event.add('dtend', datetime(2023, 10, 31, 10, 0, 0))
    event.add('location', 'Event Location')
    event.add('description', 'Event Description')

    cal.add_component(event)

    ics_content = cal.to_ical().decode('utf-8')

    from_email = "agrkeshav04@gmail.com"
    to_email = "keshava.bca2022@ssism.org"
    subject = "Appointment Booking Confirmation"
    body = "Test Email Using Django Rest App"

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    attachment = MIMEBase('text', 'calendar')
    attachment.set_payload(ics_content)
    encoders.encode_base64(attachment)
    msg.attach(attachment)

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()