# Important Links:
# 1. https://docs.python.org/3/library/email.examples.html
# 2. https://docs.python.org/3/library/email.html#module-email
# 3. https://www.geeksforgeeks.org/simple-mail-transfer-protocol-smtp/
# 4. https://treyhunner.com/2018/12/why-you-should-be-using-pathlib/

import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('HtmlTemplate.html').read_text())

email = EmailMessage()
email['from'] = 'Gayathri Kaliaperumal'
email['to'] = 'to_email@gmail.com'
email['subject'] = 'Sending email via python'

email.set_content(html.substitute({'name': 'Christopher'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('from_email@gmail.com', 'password')
    smtp.send_message(email)
    print('SUCCESS!!')
