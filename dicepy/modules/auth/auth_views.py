from flask import Blueprint, request, render_template, redirect, url_for

from dicepy.modules.addresses import AddressesController
from dicepy.modules.people.users import UsersController

bp = Blueprint('auth', __name__)

a_controller = AddressesController()
u_controller = UsersController()


@bp.route('/auth/register', methods=['GET', 'POST'])
def register():
    ''' Registers a new user account '''

    if request.method == 'POST':
        user_form = {
            'fname': request.form.get('fname'), 'lname': request.form.get('lname'),
            'email': request.form.get('email'), 'phone': request.form.get('phone'),
            'username': request.form.get('username'),
            'password': request.form.get('password'), 'confirm_password': request.form.get('confirm_password')
        }
        address_form = {
            'street_address': request.form.get('street_address'), 'city': request.form.get('city'),
            'postal_code': request.form.get('postal_code'), 'province': request.form.get('province'),
            'country': request.form.get('country')
        }

        errors = u_controller.register(user_form, address_form)
        if errors is not None:
            return render_template('auth/register.html', title='DicePy - Registration', errors=errors)
        else:
            return redirect(url_for('auth.login'))

    return render_template('auth/register.html', title='DicePy - Registration')


@bp.route('/auth/login', methods=['GET', 'POST'])
def login():
    ''' Logs a user into there existing account '''
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        errors = u_controller.login(username, password)
        
        if errors is not None:
            return render_template('auth/login.html', title='DicePy - Login', errors=errors)
        else:
            return redirect(url_for('index'))
    
    login_required_error = request.args.get('errors')
    
    if login_required_error is not None:
        return render_template('auth/login.html', title='DicePy - Login', error=login_required_error)
    
    return render_template('auth/login.html', title='DicePy - Login')


@bp.route('/auth/logout')
def logout():
    ''' Logs the user out of their account '''
    
    u_controller.logout()
    
    return redirect(url_for('auth.login'))


@bp.route('/auth/login_required')
def login_required():
    ''' Protects pages that require the user to be logged in '''
    
    error = 'You must be logged in to view the requested page!'
    
    return redirect(url_for('auth.login', errors=[error]))