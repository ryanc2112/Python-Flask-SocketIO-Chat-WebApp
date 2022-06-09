from flask import session, redirect, url_for, render_template, request
from . import main

@main.route('/', methods = ['GET', 'POST'])
def index():
    """
    Login form to enter room
    """
    return render_template('index.html')


@main.route('/chat', methods = ['GET', 'POST'])
def chat():
    """
    Chat Room.
    User's name and room must be stored in the session.
    """
    if(request.method == 'POST'):
        name = request.form['name']
        room = request.form['room']
        #Store data in session
        session['name'] = name
        session['room'] = room
        return render_template('chat.html', session=session)
    else:
        if(session.get('name') is not None):
            return render_template('chat.html', session=session)
        else:
            return redirect(url_for(''))
