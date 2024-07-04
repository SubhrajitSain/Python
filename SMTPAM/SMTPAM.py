# SMTPAM.py © 2024 by Subhrajit Sain (ANormalWintrovert) is licensed under CC BY-SA 4.0
# CC BY-SA 4.0: https://creativecommons.org/licenses/by-sa/4.0/
# ANormalWintrovert YT Channel: https://www.youtube.com/@ANormalWintrovert

# imports
import datetime
from email.mime.application import MIMEApplication
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import re
import os
import platform
import subprocess

# escape codes for colors
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

# simple gradient for logo
def gradient_text(text):
    colored_text = ""
    for i, char in enumerate(text):
        color = PURPLE_TO_BLUE[i % len(PURPLE_TO_BLUE)]
        colored_text += f"{color}{char}"
    return colored_text + RESET_COLOR

# to validate email format
def validate_email(email):
    pattern = r"[^@]+@[^@]+\.[^@]+"
    return re.match(pattern, email) is not None

# to validate port number
def validate_port(port):
    try:
        port_num = int(port)
        return 1 <= port_num <= 65535
    except ValueError:
        return False

# to clear the screen
def clear_screen():
    if platform.system() == "Windows":
        subprocess.call("cls", shell=True)
    else:
        subprocess.call("clear", shell=True)

# for logging
def log(message, type):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} - {type.upper()} - {message}\n"
    date = datetime.date.today()

    log_dir = "LOG"
    os.makedirs(log_dir, exist_ok=True)
    log_file_path = os.path.join(log_dir, f"SMTPAM-{date}.log")

    with open(log_file_path, "a") as log_file_handler:
        log_file_handler.write(log_entry)

# main function
def main():
    log("Started SMTPAM.py - main method called.", "info")

    logo = [
        ".▄▄ · • ▌ ▄ ·. ▄▄▄▄▄ ▄▄▄· ▄▄▄· • ▌ ▄ ·.     ▄▄▄· ▄· ▄▌",
        "▐█ ▀. ·██ ▐███▪•██  ▐█ ▄█▐█ ▀█ ·██ ▐███▪   ▐█ ▄█▐█▪██▌",
        "▄▀▀▀█▄▐█ ▌▐▌▐█· ▐█.▪ ██▀·▄█▀▀█ ▐█ ▌▐▌▐█·    ██▀·▐█▌▐█▪",
        "▐█▄▪▐███ ██▌▐█▌ ▐█▌·▐█▪·•▐█ ▪▐▌██ ██▌▐█▌   ▐█▪·• ▐█▀·.",
        " ▀▀▀▀ ▀▀  █▪▀▀▀ ▀▀▀ .▀    ▀  ▀ ▀▀  █▪▀▀▀ ▀ .▀     ▀ • ",
    ]

    #to apply gradient to logo
    for line in logo:
        print(gradient_text(line))

    print(LIGHT_BLUE + "Imported modules: datetime MIMEApplication smtplib MIMEText MIMEMultipart re os platform subprocess" + RESET_COLOR)
    
    print(PURPLE + "SMTPAM.py 2.6\n" + RESET_COLOR)
    print(PURPLE + "SMTPAM.py  2024 by Subhrajit Sain (ANormalWintrovert) is licensed under CC BY-SA 4.0\n" + RESET_COLOR)

    print(PURPLE + "Notes" + RESET_COLOR)
    print(PURPLE + "~~~~~\n" + RESET_COLOR)
    print(LIGHT_BLUE + "PLEASE READ THE CREATIVE COMMONS DEED AT: https://creativecommons.org/licenses/by-sa/4.0/" + RESET_COLOR)
    print(LIGHT_BLUE + "YOU MUST OBEY THE CC TERMS GIVEN IN THE ABOVE LINK BEFORE PROCEEDING TO SHARE OR MODIFY THE CREATOR'S CODE." + RESET_COLOR)
    print(LIGHT_BLUE + "FOR ATTRIBUTION USE MY YOUTUBE CHANNEL (ANormalWintrovert) LINK: https://www.youtube.com/@ANormalWintrovert" + RESET_COLOR)
    print(LIGHT_BLUE + "YOU MAY ALSO USE: https://github.com/SubhrajitSain/Python/blob/main/SMTPAM/SMTPAM.py" + RESET_COLOR)
    print(LIGHT_BLUE + "ANY ACT OF NON-COOPERATION TO CC TERMS CAN LEAD TO YOUR MODDED VERSION TO BE TAKEN DOWN.\n" + RESET_COLOR)
    
    print(PURPLE + "Short Instructions" + RESET_COLOR)
    print(PURPLE + "~~~~~~~~~~~~~~~~~~\n" + RESET_COLOR)
    print(LIGHT_BLUE + "Step 1: Enable '2 Step Verification' or any related feature on your mail service." + RESET_COLOR)
    print(LIGHT_BLUE + "        If you don't have it on, the program will fail to send any email from your email address, so please turn it on." + RESET_COLOR)
    print(LIGHT_BLUE + "Step 2: Generate an 'Application Password' or any related password on your mail service." + RESET_COLOR)
    print(LIGHT_BLUE + "Step 3: Enter the things asked for, and the email will be sent." + RESET_COLOR)

    # inputs
    print("\n" + PURPLE + "Addresses" + RESET_COLOR)
    print(PURPLE + "~~~~~~~~\n" + RESET_COLOR)
    
    log("Asked sender email.", "info")
    sender_email = input(DARK_GREEN + "Enter your email address: " + RESET_COLOR)
    while not validate_email(sender_email):
        log(f"Failed to validate sender email. Email: {sender_email}", "error")
        log("Asking sender email again.", "info")
        print(RED + "Invalid email format. Please try again." + RESET_COLOR)
        sender_email = input(DARK_GREEN + "Enter your email address: " + RESET_COLOR)
    
    log("Asked recipent email.", "info")
    recipient_email = input(DARK_GREEN + "Enter recipient's email address: " + RESET_COLOR)
    while not validate_email(recipient_email):
        log(f"Failed to validate recipent email. Email: {recipient_email}", "error")
        log("Asking recipent email again.", "info")
        print(RED + "Invalid email format. Please try again." + RESET_COLOR)
        recipient_email = input(DARK_GREEN + "Enter recipient's email address: " + RESET_COLOR)
    
    # Email server configuration
    print("\n" + PURPLE + "Email server config" + RESET_COLOR)
    print(PURPLE + "~~~~~~~~~~~~~~~~~~~\n" + RESET_COLOR)
    log("Asked SMTP server.", "info")
    smtp_server = input(DARK_GREEN + "Enter SMTP server (default: smtp.gmail.com): " + RESET_COLOR) or "smtp.gmail.com"
    log("Asked SMTP port.", "info")
    smtp_port = input(DARK_GREEN + "Enter SMTP port (default: 587): " + RESET_COLOR) or "587"
    while not validate_port(smtp_port):
        log(f"Failed to validate SMTP port. Port: {smtp_port}", "error")
        log("Asking SMTP port again.", "info")
        print(YELLOW + "Invalid port number. Please enter a valid port (1-65535)." + RESET_COLOR)
        smtp_port = input(DARK_GREEN + "Enter SMTP port (default: 587): " + RESET_COLOR) or "587"
    
    smtp_username = sender_email
    log("Asked email application password.", "info")
    smtp_password = os.getenv('SMTP_PASSWORD') or input(DARK_GREEN + "Enter your email's application password: " + RESET_COLOR)
    
    # Message content
    print("\n" + PURPLE + "Message content" + RESET_COLOR)
    print(PURPLE + "~~~~~~~~~~~~~~~\n" + RESET_COLOR)
    log("Asked message subject.", "info")
    subject = input(DARK_GREEN + "Enter subject (max 255 characters): " + RESET_COLOR)
    while len(subject) > 255:
        log(f"Message subject too long (>255 chars). Subject: {subject}", "error")
        log("Asking message subject again.", "info")
        print(YELLOW + "Subject is too long. Please enter a subject with a maximum of 255 characters." + RESET_COLOR)
        subject = input(DARK_GREEN + "Enter subject (max 255 characters): " + RESET_COLOR)

    log("Asked message body.", "info")
    body = input(DARK_GREEN + "Enter message body (max 5000 characters): " + RESET_COLOR)
    while len(body) > 5000:
        log(f"Message body too long (>5000 chars). Body: {body}", "error")
        log("Asking message body again.", "info")
        print(YELLOW + "Message body is too long. Please enter a message with a maximum of 5000 characters." + RESET_COLOR)
        body = input(DARK_GREEN + "Enter message body (max 5000 characters): " + RESET_COLOR)
    
    # Add hardcoded signature
    log("Added signature to body.", "info")
    signature = f"[This e-mail was sent from {sender_email} to {recipient_email} via {smtp_server} from port {smtp_port}. Sent using SMTPAM.py by Subhrajit Sain. https://github.com/SubhrajitSain/Python/blob/main/SMTPAM/SMTPAM.py]"
    body += "\n\n" + signature

    # create the MIME object
    log("Created MIME object.", "info")
    print("\n" + LIGHT_BLUE + "Creating MIME object..." + RESET_COLOR)
    message = MIMEMultipart()
    log("Added 'From'.", "info")
    print(LIGHT_BLUE + "Adding 'From'..." + RESET_COLOR)
    message['From'] = sender_email
    log("Added 'To'.", "info")
    print(LIGHT_BLUE + "Adding 'To'..." + RESET_COLOR)
    message['To'] = recipient_email
    log("Added 'Subject'.", "info")
    print(LIGHT_BLUE + "Adding 'Subject'..." + RESET_COLOR)
    message['Subject'] = subject
    log("Added body.", "info")
    print(LIGHT_BLUE + "Adding message body 'body'...\n" + RESET_COLOR)
    message.attach(MIMEText(body, 'plain'))

    # Ask for attachments
    log("Asked for attachments.", "info")
    print("\n" + PURPLE + "Attachments" + RESET_COLOR)
    print(PURPLE + "~~~~~~~~~~\n" + RESET_COLOR)
    attachments = []
    while True:
        attachment_path = input(DARK_GREEN + "Enter attachment file path (or 'done' to finish): " + RESET_COLOR)
        if attachment_path.lower() == 'done':
            break
        if os.path.exists(attachment_path):
            log(f"Added attachment: {attachment_path}", "info")
            attachments.append(attachment_path)
        else:
            log(f"Attachment not found: {attachment_path}", "error")
            print(RED + f"Error: Attachment not found at {attachment_path}" + RESET_COLOR)

    # Add attachments to the message
    for attachment_path in attachments:
        with open(attachment_path, 'rb') as attachment_file:
            attachment_data = attachment_file.read()
        attachment_mime = MIMEApplication(attachment_data, Name=os.path.basename(attachment_path))
        attachment_mime['Content-Disposition'] = f'attachment; filename="{os.path.basename(attachment_path)}"'
        message.attach(attachment_mime)
    
    # connect to the SMTP server and send the email
    log(f"Trying to connect to SMTP server. Server: {smtp_server} Port: {smtp_port}", "info")
    print(LIGHT_BLUE + f"Trying to connect to {smtp_server} using port {smtp_port}..." + RESET_COLOR)
    try:
        with smtplib.SMTP(smtp_server, int(smtp_port)) as server:
            log("Starting TTLS via SMTP.", "info")
            print(LIGHT_BLUE + "Starting TTLS via SMTP..." + RESET_COLOR)
            server.starttls()
            log("Started TTLS successfully.", "info")
            log("Logging in to SMTP server.", "info")
            print(LIGHT_BLUE + "Logging in to mail server via SMTP..." + RESET_COLOR)
            server.login(smtp_username, smtp_password)
            log("Logged in successfully.", "info")
            log("Sending email.", "info")
            print(LIGHT_BLUE + f"Sending message to {recipient_email} via SMTP..." + RESET_COLOR)
            server.sendmail(sender_email, recipient_email, message.as_string())
            log("Email sent successfully.", "info")
            print(LIGHT_BLUE + "Email sent successfully." + RESET_COLOR)
    except smtplib.SMTPAuthenticationError:
        log("SMTPAuthenticationError. Wrong username and/or password.", "error")
        print(RED + "Error: Authentication failed. Please check your email and application password." + RESET_COLOR)
    except smtplib.SMTPConnectError:
        log("SMTPConnectError. Could not connect to SMTP server.", "error")
        print(RED + "Error: Failed to connect to the SMTP server. Please check the server address and port." + RESET_COLOR)
    except smtplib.SMTPRecipientsRefused:
        log("SMTPRecipientsRefused. Recipent email refused.", "error")
        print(RED + "Error: The recipient's email address was refused by the server." + RESET_COLOR)
    except smtplib.SMTPDataError:
        log("SMTPDataError. Server refused email data.", "error")
        print(RED + "Error: The SMTP server refused the email data." + RESET_COLOR)
    except smtplib.SMTPHeloError:
        log("SMTPHeloError. Server did not respond to HELO command.", "error")
        print(RED + "Error: SMTP server didn't respond to the HELO command." + RESET_COLOR)
    except smtplib.SMTPResponseException:
        log("SMTPResponseException. Server returned an unexpected response code.", "error")
        print(RED + "Error: SMTP server returned an unexpected response code." + RESET_COLOR)
    except smtplib.SMTPNotSupportedError:
        log("SMTPNotSupportedError. Server does not support a specific function or command.", "error")
        print(RED + "Error: SMTP server doesn't support a specific feature or command." + RESET_COLOR)
    except smtplib.SMTPException as e:
        log(f"SMTPException. SMTP error: {e}", "error")
        print(RED + f"SMTP error occurred: {e}" + RESET_COLOR)
    except Exception as e:
        log(f"Exception. Unexpected error: {e}", "error")
        print(RED + f"An unexpected error occurred: {e}" + RESET_COLOR)

if __name__ == "__main__":
    while True:
        try:
            main()
            log("Asking for restart.", "info")
            restart = input(DARK_GREEN + "\nDo you want to send another email? (yes/no): " + RESET_COLOR).strip().lower()
            if restart != 'yes':
                log("Program terminated.", "info")
                print(LIGHT_BLUE + "Exiting the program. Goodbye!" + RESET_COLOR)
                break
            log("Restart requested.", "info")
            clear_screen()
        except KeyboardInterrupt:
            log("KeyboardInterrupt. Exiting program.", "error")
            print(LIGHT_BLUE + "\nKeyboardInterrupt, exiting the program. Goodbye!" + RESET_COLOR)
            break
