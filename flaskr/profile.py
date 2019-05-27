from flask import (
    Blueprint, flash, g, redirect, render_template, session, request, url_for
)

from flaskr.auth import login_required
from flaskr.db import get_db


bp = Blueprint('profile', __name__, url_prefix='/profile')

@bp.route('/', methods=('GET',))
@login_required
def profile():
    return render_template('profile/profile.html')


@bp.route('/edit', methods=('GET', 'POST'))
@login_required
def edit():
    if request.method == 'POST':
        user_id = session.get('user_id')
        bio = request.form['bio']
        db = get_db()

        db.execute(
            'UPDATE user SET bio = ?'
            ' WHERE id = ?',
            (bio, user_id)
        )
        db.commit()
        return redirect(url_for('profile.profile'))

    return render_template('profile/edit.html')
