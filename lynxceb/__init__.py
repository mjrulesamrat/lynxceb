"""SMTP email backend class."""
import smtplib

from django.core.mail.backends.smtp import EmailBackend as CoreEmailBackend
from django.core.mail.message import sanitize_address

from django.template.loader import render_to_string

class EmailBackend(CoreEmailBackend):

    def _send(self, email_message):
        """A helper method that does the actual sending."""
        if not email_message.recipients():
            return False
        from_email = sanitize_address(email_message.from_email, email_message.encoding)
        recipients = [sanitize_address(addr, email_message.encoding)
                      for addr in email_message.recipients()]

        my_header = render_to_string('lynxceb_header.html', {})
        my_footer = render_to_string('lynxceb_footer.html', {})        

        if email_message.content_subtype == "plain":
            email_message.body = my_header + "<pre style='font-family:arial;'>" + email_message.body+ "</pre>" + my_footer
            email_message.content_subtype = "html"

        message = email_message.message()

        try:
            self.connection.sendmail(from_email, recipients, message.as_bytes(linesep='\r\n'))
        except smtplib.SMTPException:
            if not self.fail_silently:
                raise
            return False
        return True
