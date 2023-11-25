import smtplib
import ssl
from email.message import EmailMessage
import sys

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def send_mail(name ,recipient):
    # Set your email credentials and details
    sender_email = "codemonkeyservices@gmail.com"
    sender_password = "xvti dfry ijzy nips"
    customer_email= recipient 
    print(f"sending mail to: {recipient}\n" )


    # Create the email message
    subject = "CodeMonkey - Your Gateway to a Captivating Hotel Website!"

        
    
    em = EmailMessage()
    em["From"] = sender_email
    em["To"] = recipient
    em["Subject"] = subject


#    getting mail content from htmlMailFormat.txt file 
    mailContent = ''
    with open('htmlMailFormat.txt', 'r') as f:
        mailContent=f.read()

    mailContent=mailContent.replace("__name__", name)

    # mail content 
    html_body = f"""
              {mailContent}
    """

    em.add_alternative(html_body , subtype='html')

  # Add SSL (layer of security)
    context = ssl.create_default_context()


        # Connect to the SMTP server
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(sender_email, sender_password)
        smtp.sendmail(sender_password, customer_email, em.as_string())
    print("Email sent successfully!")

    



emails=[]
names=[]
emails_file = open('emails.txt', 'r')
Lines = emails_file.readlines()
 
# Strips the newline character
for line in Lines:
    emails.append(line.strip())

names_file = open('names.txt', 'r')
Lines = names_file.readlines()
 
# Strips the newline character
for line in Lines:
    names.append(line.strip())

if len(emails) == len(names):
    res = "\n".join("{} \t {}".format(x, y) for x, y in zip(names, emails))
    print(res)
    execute = input("\nPlease Check the name - mail pair above before sending the mails, confirm the execution below to send mail\nare you sure you want to send the mails(Y/N): ")
    execute=execute.lower()
    print(execute)
    if execute=="y":
        for i in range(0,len(emails)):
            send_mail(name=names[i], recipient=emails[i])
    else:
        sys.exit(-1)
    
else:
    print("conflict in number of names and mails")


