# This class is responsible for sending notifications.
# class responsible for sending emails
import smtplib

class NotificationManager:
    """
    managing the sending of emails with a gamil account
    This class is responsible for sending notifications.
    """
    def __init__(self, email_app_password: str, email_from: str) -> None:
        self.email_app_password = email_app_password
        self.email_from = email_from


    def send_gmail_mail(self, email_title: str, message_to_send: str, \
        email_to: str) -> None:
        """
        sends email from a gmail account, only gmail !
        """
        # using encode utf-8 to escape the UnicodeEncodeError for specific characters
        email_message = lambda title, content: f"Subject:{title}\n\n{content}".encode('utf-8')

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls() # making the conection secure
            result = connection.login(user=self.email_from, password=self.email_app_password)
            connection.sendmail(from_addr=self.email_from, 
                                to_addrs=email_to,
                                msg=email_message(title=email_title,content=message_to_send))


    def send_emails(self, list_of_users : list[dict], email_title: str, \
        message_to_send: str) -> None:
        """
        send a email to a list of defined users
        """
        for user in list_of_users:
            self.send_gmail_mail(
                email_title=email_title,
                message_to_send=message_to_send,
                email_to=user['email']
            )