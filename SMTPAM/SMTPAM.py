# SMTPAM.py © 2024 by Subhrajit Sain (ANormalWintrovert) is licensed under CC BY-SA 4.0
# CC BY-SA 4.0: https://creativecommons.org/licenses/by-sa/4.0/
# ANormalWintrovert YT Channel: https://www.youtube.com/@ANormalWintrovert

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import re
import os
import platform
import subprocess

# ANSI escape codes for colors
PURPLE = "\033[95m"
RED = "\033[91m"
YELLOW = "\033[93m"
DARK_GREEN = "\033[32m"
LIGHT_BLUE = "\033[94m"
RESET_COLOR = "\033[0m"

# ANSI escape codes for purple to blue shades
PURPLE_TO_BLUE = [
    "\033[95m",  # Light Magenta
    "\033[94m",  # Light Blue
    "\033[96m",  # Cyan
    "\033[94m",  # Light Blue
    "\033[95m",  # Light Magenta
]

def gradient_text(text):
    """Returns the text with each line colored in a gradient from purple to blue."""
    colored_text = ""
    for i, char in enumerate(text):
        color = PURPLE_TO_BLUE[i % len(PURPLE_TO_BLUE)]
        colored_text += f"{color}{char}"
    return colored_text + RESET_COLOR

def validate_email(email):
    """Validates email format."""
    pattern = r"[^@]+@[^@]+\.[^@]+"
    return re.match(pattern, email) is not None

def validate_port(port):
    """Validates if the port number is a valid integer between 1 and 65535."""
    try:
        port_num = int(port)
        return 1 <= port_num <= 65535
    except ValueError:
        return False

def clear_screen():
    """Clears the terminal screen."""
    if platform.system() == "Windows":
        subprocess.call("cls", shell=True)
    else:
        subprocess.call("clear", shell=True)

def main():
    logo = [
        ".▄▄ · • ▌ ▄ ·. ▄▄▄▄▄ ▄▄▄· ▄▄▄· • ▌ ▄ ·.     ▄▄▄· ▄· ▄▌",
        "▐█ ▀. ·██ ▐███▪•██  ▐█ ▄█▐█ ▀█ ·██ ▐███▪   ▐█ ▄█▐█▪██▌",
        "▄▀▀▀█▄▐█ ▌▐▌▐█· ▐█.▪ ██▀·▄█▀▀█ ▐█ ▌▐▌▐█·    ██▀·▐█▌▐█▪",
        "▐█▄▪▐███ ██▌▐█▌ ▐█▌·▐█▪·•▐█ ▪▐▌██ ██▌▐█▌   ▐█▪·• ▐█▀·.",
        " ▀▀▀▀ ▀▀  █▪▀▀▀ ▀▀▀ .▀    ▀  ▀ ▀▀  █▪▀▀▀ ▀ .▀     ▀ • ",
    ]

    for line in logo:
        print(gradient_text(line))

    print(LIGHT_BLUE + "Importing: smtplib, email.mime.text (MIMEText), email.mime.multipart (MIMEMultipart)..." + RESET_COLOR)
    print(LIGHT_BLUE + "Done importing!\n" + RESET_COLOR)
    
    print(PURPLE + "SMTPAM.py 1.6\n" + RESET_COLOR)
    print(PURPLE + "SMTPAM.py © 2024 by Subhrajit Sain (ANormalWintrovert) is licensed under CC BY-SA 4.0\n" + RESET_COLOR)

    print(PURPLE + "Notes" + RESET_COLOR)
    print(PURPLE + "~~~~~\n" + RESET_COLOR)
    print(LIGHT_BLUE + "PLEASE READ THE CREATIVE COMMONS DEED AT: https://creativecommons.org/licenses/by-sa/4.0/" + RESET_COLOR)
    print(LIGHT_BLUE + "YOU MUST OBEY THE CC TERMS GIVEN IN THE ABOVE LINK BEFORE PROCEEDING TO SHARE OR MODIFY THE CREATOR'S CODE." + RESET_COLOR)
    print(LIGHT_BLUE + "FOR ATTRIBUTION USE MY YOUTUBE CHANNEL (ANormalWintrovert) LINK: https://www.youtube.com/@ANormalWintrovert" + RESET_COLOR)
    print(LIGHT_BLUE + "ANY ACT OF NON-COOPERATION TO CC TERMS CAN LEAD TO YOUR MODDED VERSION TO BE TAKEN DOWN.\n" + RESET_COLOR)
    
    print(PURPLE + "Short Instructions" + RESET_COLOR)
    print(PURPLE + "~~~~~~~~~~~~~~~~~~\n" + RESET_COLOR)
    print(LIGHT_BLUE + "Step 1: Enable '2 Step Verification' or any related feature on your mail service." + RESET_COLOR)
    print(LIGHT_BLUE + "        If you don't have it on, the program will fail to send any email from your email address, so please turn it on." + RESET_COLOR)
    print(LIGHT_BLUE + "Step 2: Generate an 'Application Password' or any related password on your mail service." + RESET_COLOR)
    print(LIGHT_BLUE + "Step 3: Enter the things asked for, and the email will be sent." + RESET_COLOR)

    print("\n" + PURPLE + "Addresses" + RESET_COLOR)
    print(PURPLE + "~~~~~~~~\n" + RESET_COLOR)
    
    sender_email = input(DARK_GREEN + "Enter your email address: " + RESET_COLOR)
    while not validate_email(sender_email):
        print(RED + "Invalid email format. Please try again." + RESET_COLOR)
        sender_email = input(DARK_GREEN + "Enter your email address: " + RESET_COLOR)
    
    recipient_email = input(DARK_GREEN + "Enter recipient's email address: " + RESET_COLOR)
    while not validate_email(recipient_email):
        print(RED + "Invalid email format. Please try again." + RESET_COLOR)
        recipient_email = input(DARK_GREEN + "Enter recipient's email address: " + RESET_COLOR)
    
    # Email server configuration
    print("\n" + PURPLE + "Email server config" + RESET_COLOR)
    print(PURPLE + "~~~~~~~~~~~~~~~~~~~\n" + RESET_COLOR)
    smtp_server = input(DARK_GREEN + "Enter SMTP server (default: smtp.gmail.com): " + RESET_COLOR) or "smtp.gmail.com"
    smtp_port = input(DARK_GREEN + "Enter SMTP port (default: 587): " + RESET_COLOR) or "587"
    while not validate_port(smtp_port):
        print(YELLOW + "Invalid port number. Please enter a valid port (1-65535)." + RESET_COLOR)
        smtp_port = input(DARK_GREEN + "Enter SMTP port (default: 587): " + RESET_COLOR) or "587"
    
    smtp_username = sender_email
    smtp_password = os.getenv('SMTP_PASSWORD') or input(DARK_GREEN + "Enter your email's application password: " + RESET_COLOR)
    
    # Message content
    print("\n" + PURPLE + "Message content" + RESET_COLOR)
    print(PURPLE + "~~~~~~~~~~~~~~~\n" + RESET_COLOR)
    subject = input(DARK_GREEN + "Enter subject (max 255 characters): " + RESET_COLOR)
    while len(subject) > 255:
        print(YELLOW + "Subject is too long. Please enter a subject with a maximum of 255 characters." + RESET_COLOR)
        subject = input(DARK_GREEN + "Enter subject (max 255 characters): " + RESET_COLOR)

    body = input(DARK_GREEN + "Enter message body (max 5000 characters): " + RESET_COLOR)
    while len(body) > 5000:
        print(YELLOW + "Message body is too long. Please enter a message with a maximum of 5000 characters." + RESET_COLOR)
        body = input(DARK_GREEN + "Enter message body (max 5000 characters): " + RESET_COLOR)
    
    # Create the MIME object
    print("\n" + LIGHT_BLUE + "Creating MIME object..." + RESET_COLOR)
    message = MIMEMultipart()
    print(LIGHT_BLUE + "Adding 'From'..." + RESET_COLOR)
    message['From'] = sender_email
    print(LIGHT_BLUE + "Adding 'To'..." + RESET_COLOR)
    message['To'] = recipient_email
    print(LIGHT_BLUE + "Adding 'Subject'..." + RESET_COLOR)
    message['Subject'] = subject
    print(LIGHT_BLUE + "Adding message body 'body'...\n" + RESET_COLOR)
    message.attach(MIMEText(body, 'plain'))
    
    # Connect to the SMTP server and send the email
    print(LIGHT_BLUE + f"Trying to connect to {smtp_server} using port {smtp_port}..." + RESET_COLOR)
    try:
        with smtplib.SMTP(smtp_server, int(smtp_port)) as server:
            print(LIGHT_BLUE + "Starting TTLS via SMTP..." + RESET_COLOR)
            server.starttls()
            print(LIGHT_BLUE + "Logging in to mail server via SMTP..." + RESET_COLOR)
            server.login(smtp_username, smtp_password)
            print(LIGHT_BLUE + f"Sending message to {recipient_email} via SMTP..." + RESET_COLOR)
            server.sendmail(sender_email, recipient_email, message.as_string())
            print(LIGHT_BLUE + "Email sent successfully." + RESET_COLOR)
    except smtplib.SMTPAuthenticationError:
        print(RED + "Error: Authentication failed. Please check your email and application password." + RESET_COLOR)
    except smtplib.SMTPConnectError:
        print(RED + "Error: Failed to connect to the SMTP server. Please check the server address and port." + RESET_COLOR)
    except smtplib.SMTPRecipientsRefused:
        print(RED + "Error: The recipient's email address was refused by the server." + RESET_COLOR)
    except smtplib.SMTPDataError:
        print(RED + "Error: The SMTP server refused the email data." + RESET_COLOR)
    except smtplib.SMTPException as e:
        print(RED + f"SMTP error occurred: {e}" + RESET_COLOR)
    except Exception as e:
        print(RED + f"An unexpected error occurred: {e}" + RESET_COLOR)

if __name__ == "__main__":
    while True:
        main()
        restart = input(DARK_GREEN + "\nDo you want to send another email? (yes/no): " + RESET_COLOR).strip().lower()
        if restart != 'yes':
            print(LIGHT_BLUE + "Exiting the program. Goodbye!" + RESET_COLOR)
            break
        clear_screen()
