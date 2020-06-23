# Important Links:
# 1. https://docs.python.org/3/library/email.examples.html
# 2. https://docs.python.org/3/library/email.html#module-email
# 3. https://www.geeksforgeeks.org/simple-mail-transfer-protocol-smtp/

import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Gayathri Kaliaperumal'
email['to'] = 'to_email@gmail.com'
email['subject'] = 'Sending email via python'
email.set_content('Yippee!! It worked')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('from_email@gmail.com', 'password')
    smtp.send_message(email)
    print('SUCCESS!!')
