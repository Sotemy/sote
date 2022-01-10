from flask import render_template, request
from flask.json import jsonify
from flask_login import login_required, current_user
from flask_mail import Message

from app.main.chat import userchat
from app.models import Post, User
from app import db

@userchat.route('/')
@login_required
def allDialogs():
    return render_template('main/chat/allDialogs.html')

@userchat.route('/<id>')
@login_required
def userDialog(id):
    return render_template('main/chat/userDialog.html')

# @userchat.route('/chat/send_message/<item_id>', methods=['POST'])
# @login_required
# def send_message(item_id):
#     it = Post.query.filter_by(id=item_id).first_or_404()
#     if it:
#         if request.method=='POST':
#             message=request.form['message']
#             msg = Message(author=current_user, recipient=it.author,
#             body=message, item=item_id)
#             db.session.add(msg)
#             db.session.commit()
#             return jsonify({'result':'success', 'text':message})
#     return jsonify({'result':'error', 'text':'user not exist'})