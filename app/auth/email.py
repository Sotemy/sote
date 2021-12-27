from flask import render_template, current_app
from app.email import send_email


def send_password_reset_email(user):
    token = user.reset_password_token()
    return send_email(('[Microblog] Reset Your Password'),
               sender=current_app.config['ADMINS'],
               recipients=[user.email],
               text_body=render_template('email/reset_password.txt',
                                         user=user, token=token),
               html_body=render_template('email/reset_password.html',
                                         user=user, token=token))