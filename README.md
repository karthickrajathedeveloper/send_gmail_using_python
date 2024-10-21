## MQTT-Email Notification System
This project demonstrates how to subscribe to an MQTT topic and send email notifications using Gmail whenever a message is received on the subscribed topic. It utilizes the Paho MQTT client library for MQTT communication and smtplib for sending emails.
## Prerequisites
# Python Environment
Ensure you have Python installed. You can install the required libraries using:

```
pip install paho-mqtt
```
# Gmail App Password
If you use Gmail, you’ll need to enable 2-Step Verification and generate an App Password. 
- [Learn more about App Passwords](https://knowledge.workspace.google.com/kb/how-to-create-app-passwords-000009237).

# MQTT Broker Access
- Set up your MQTT broker (like Mosquitto) or use a public MQTT broker.
- Make sure you know the `IP address, port, and topic`.
# Project Setup
1. Clone or Copy the Code
  Create a Python file with the above code (e.g., mqtt_email.py).

2. Configure MQTT and Email Credentials
  Open the file and replace the following placeholders:
**python**
```
# MQTT Configuration
MQTT_BROKER = 'your_broker_ip'  # Broker IP address
MQTT_PORT = 1883  # Port (default for MQTT)
MQTT_TOPIC = 'your_topic'  # Topic to subscribe

# Gmail Configuration
SENDER_EMAIL = 'your_email@gmail.com'  # Sender email address
SENDER_PASSWORD = 'your_app_password'  # Gmail App Password
RECEIVER_EMAILS = ['receiver1@example.com', 'receiver2@example.com']  # List of receivers
```
# Install Dependencies
Use the following command to install required libraries:
```
pip install paho-mqtt
```
# Run the Program
Run the program using:
```
python mqtt_email.py
```
## How It Works
# MQTT Subscription:
- The program connects to the specified MQTT broker and subscribes to the given topic.

# Receiving Messages:
+ Whenever a message is received on the subscribed topic, it triggers the on_message() callback.

# Sending Email:
* Upon receiving an MQTT message, the program sends an email to the specified receivers with the topic and message details.

# Program Termination:
* You can stop the program using `Ctrl + C`.
* It will gracefully disconnect from the MQTT broker.

## Example Output
```
Subscribed to topic: test/topic
Received message: Hello World
Email sent successfully to: ['receiver1@example.com', 'receiver2@example.com']
```
# Troubleshooting
# 1. Authentication Error:
  - If you encounter an authentication error with Gmail, ensure that:
      * 2-Step Verification is enabled on your Gmail account.
      * You are using a valid App Password instead of the regular password.
# 2. Connection Error:
  - Ensure the MQTT broker IP and port are correct, and the broker is accessible from your machine.

# 3. Failed Email Sending:
  - Double-check the SMTP server setup and ensure that the receiver email addresses are valid.

## Dependencies
* Python 3.x
* Paho MQTT library (paho-mqtt)
* smtplib (built-in)

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Author
[M. Karthickraja](https://github.com/karthickrajathedeveloper)

This README should cover everything needed to set up, configure, and run your MQTT-Email notification system. Let me know if you need any further adjustments!
