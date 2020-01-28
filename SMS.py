import smtplib
import creds
carriers = {
    'att':    '@mms.att.net',
    'tmobile': ' @tmomail.net',
    'verizon':  '@vtext.com',
    'sprint':   '@page.nextel.com',
    'free': '@txt.freedommobile.ca'
}


def send(message):
    # Replace the number with your own, or consider using an argument\dict for multiple people.
    to_number = creds.phone + '{}'.format(carriers['free'])
    auth = (creds.email, creds.password)

    # Establish a secure session with gmail's outgoing SMTP server using your gmail account
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(auth[0], auth[1])

    # Send text message through SMS gateway of destination number
    server.sendmail(auth[0], to_number, message)
