from random import choice
import string
from datetime import datetime
from core.models import ShortUrls
from  core import app, db
from flask import render_template, request ,  flash, redirect, url_for

def generate_short_id(num_of_chars:int):
    """
    Function to generate short id of specified length of characters
    """

    generated_chars = [ choice(string.ascii_letters+string.digits) for _ in range(num_of_chars)]

    return  ''.join(generated_chars)


@app.route("/")
def index():
    if request.method == 'POST':
        url = request.form['url']
        short_id = request.form['custom_id']

        if short_id and ShortUrls.query.filter_by(short_id=short_id).first() is not None:
            flash("Please enter a different custom id")
            return redirect(url_for('index'))

        if not url:
            flash('The URL is required')
            return redirect(url_for('index'))

        if not short_id:
            short_id = generate_short_id(8)

        new_link = ShortUrls(original_url = url , short_id = short_id,  created_at=datetime.now())
        db.session.add(new_link)
        db.session.commit()

        short_url = request.host_url + short_id

        return render_template('index.html', short_url=short_url)

    return render_template('index.html')
