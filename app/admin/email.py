from flask import render_template, current_app

from app.email import send_email

def send_warn_message(error, recipients):
    sender=current_app.config['ADMINS']
    subject='error PLEASE CHECK!'
    text_body=render_template('email/reset_password.txt', error=error)
    html_body=render_template('email/reset_password.html', error=error)
    return send_email(subject, sender, recipients, text_body, html_body)