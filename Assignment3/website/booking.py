# from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
# from .models import Booking, Event
# from .forms import BookingForm
# from . import db
# import os
# from werkzeug.utils import secure_filename
# # additional import:
# from flask_login import login_required, current_user


# bkbp = Blueprint('events', __name__, url_prefix='/events')

# @bkbp.route('/book-event', methods=['GET', 'POST'])
# @login_required
# def book_event():
#   form = BookingForm()
#   form.event_id.choice = [(event.id, event.name) for event in Event.query.all()]
#   if form.validate_on_submit():
#     booking = Booking(
#         event_id=form.event_id.data,
#         user_id=current_user.id,
#         ticket_number=form.ticket_number.data,
#         booking_date=form.booking_date.data,
#         payment_method=form.payment_method.data,
#     )
#     db.session.add(booking)
#     db.session.commit()
#     flash('Booking Successful!', 'success')
#     # Always end with redirect when form is valid
#     return redirect(url_for('index'))
#   return render_template('book_event.html', form=form)

