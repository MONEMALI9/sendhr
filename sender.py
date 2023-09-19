def sender():
    import pandas as pd
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
    from email import encoders

    # Email configuration

    # Your Gmail email address
    sender_email = 'abdelmonemalielmongy@gmail.com'  
    # Your Gmail password
    sender_password = 'tgwg ppyn axut xjwo' 

    df =  pd.read_csv('hremail.csv')  
    list_email = df[df.columns[0]] 
    list_email = list(list_email)   
             
    # List of recipient email addresses
    #recipient_emails = ['Ahmedbasouney8@gmail.com', 'monem921999@gmail.com'] 
    recipient_emails = list(list_email)  
    for i in range (0,len(recipient_emails)):
        subject = 'Data Analysis & Business intelligence Developer'

        # Open the .txt file for reading (change 'filename.txt' to your file's name)
        f =  open('message.txt', 'r')
        message = f.read()
        f.close()



        # Attach a PDF file
        pdf_file_path = "ABDELMONEM ALI ELMONGY.pdf"  # Replace with the actual path to your PDF file

        # Create a MIME attachment
        attachment = open(pdf_file_path, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename="{pdf_file_path}"')

        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = ''.join(recipient_emails[i])
        msg['Subject'] = subject

        # Attach the message to the email
        msg.attach(MIMEText(message, 'plain'))


        # Attach the PDF to the message
        msg.attach(part)

        # Connect to the SMTP server
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, sender_password)
        except Exception as e:
            print(f"Failed to connect to the SMTP server: {e}")
            exit()

        # Send the email
        try:
            server.sendmail(sender_email, recipient_emails[i], msg.as_string())
            print('Email sent successfully!')
        except Exception as e:
            print(f"Failed to send the email: {e}")
        finally:
            server.quit()
