from flask import (
    Blueprint, flash, g, redirect, render_template, session, request, url_for
)

from flaskr.auth import login_required
from flaskr.db import get_db


bp = Blueprint('profile', __name__, url_prefix='/profile')

@bp.route('/<int:id>')
def profile(id):
    db = get_db()
    user = db.execute(
        'SELECT username, bio, id FROM user WHERE id = ?',
        (id,)
    ).fetchone()
    return render_template('profile/profile.html', user=user)


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
        return redirect(url_for('profile.profile', id=user_id))

    return render_template('profile/edit.html')
