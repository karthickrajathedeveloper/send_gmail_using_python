import paho.mqtt.client as mqtt
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# MQTT Configuration
MQTT_BROKER = '' #ip
MQTT_PORT = 1883 #port
MQTT_TOPIC = "" #subscribe Topic

# Gmail Configuration
SENDER_EMAIL = "" #sender mail id
SENDER_PASSWORD = ""  # Use App Password
RECEIVER_EMAILS = "" # Receiver

# Email Setup Function
def send_email(subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = ", ".join(RECEIVER_EMAILS)
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        # SMTP server setup
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
        server.quit()

        print("Email sent successfully to:", RECEIVER_EMAILS)
    except Exception as e:
        print(f"Failed to send email: {e}")

# MQTT Callback when message is received
def on_message(client, userdata, message):
    print(f"Received message: {message.payload.decode()}")
    subject = "MQTT Data Received"
    body = f"Topic: {message.topic}\nMessage: {message.payload.decode()}"
    send_email(subject, body)

# MQTT Setup
client = mqtt.Client("")#Client Id
client.username_pw_set("", "") # user name and password

client.on_message = on_message
client.connect(MQTT_BROKER, MQTT_PORT)

client.subscribe(MQTT_TOPIC)
print(f"Subscribed to topic: {MQTT_TOPIC}")

# Start MQTT loop
try:
    client.loop_forever()
except KeyboardInterrupt:
    print("Program interrupted.")
    client.disconnect()

