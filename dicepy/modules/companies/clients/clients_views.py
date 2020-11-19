from dicepy.modules.addresses import addresses_controller
from flask import Blueprint, request, render_template, redirect, url_for, jsonify

from . import ClientsController
from ...addresses import AddressesController
from dicepy.lib.middleware.auth_middleware import login_required

bp = Blueprint('clients', __name__)
controller = ClientsController()
addresses_controller = AddressesController()


@bp.route('/clients')
@bp.route('/clients/index')
@login_required
def index():
    ''' Fetches and displays all clients from the database '''

    page = None
    limit = None

    # Set page parameters
    if 'page' in request.args:
        page = int(request.args.get('page'))
    else:
        page = 1
    if 'limit' in request.args:
        limit = int(request.args.get('limit'))
    else:
        limit = 10  # Default limit

    # Log to console
    print('--- Clients Index Page ---')
    print('Page Number: ' + str(page))
    print('Limit Per Page: ' + str(limit))

    # Get the clients for this page
    clients = controller.select_in_range(page, limit)

    # Get number of pages for pagination
    num_pages = controller.get_number_of_pages(limit)

    return render_template('clients/index.html', title='Clients - Index', clients=clients, num_pages=num_pages,
                           page=page, limit=limit)


@bp.route('/clients/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        # Client data from the form
        client_form = {'company_name': request.form.get('company_name'), 'about': request.form.get('about'),
                       'email': request.form.get('email'), 'phone': request.form.get('phone'),
                       'notes': request.form.get('notes')}

        # Address data from the form
        address_form = {'street_address': request.form.get('street_address'), 'city': request.form.get('city'),
                        'postal_code': request.form.get('postal_code'), 'province': request.form.get('province'),
                        'country': request.form.get('country')}
        
        errors = controller.create(client_form, address_form)
        
        if len(errors) > 0:
            return render_template('clients/create.html', title='Clients - Create', errors=errors)
        else:
            return redirect(url_for('clients.index'))

    return render_template('clients/create.html', title='Clients - Create')


@bp.route('/clients/edit/<client_id>', methods=['GET', 'POST'])
@login_required
def edit(client_id):
    client = controller.select_by_id(client_id)
    address = addresses_controller.select_by_id(client.address_id)
    
    if request.method == 'POST':
        # Client data from form
        client_form = {'company_name': request.form.get('company_name'), 'about': request.form.get('about'), 
                       'email': request.form.get('email'), 'phone': request.form.get('phone'),
                       'notes': request.form.get('notes')}
        
        # Address data from form
        address_form = {'street_address': request.form.get('street_address'), 'city': request.form.get('city'),
                        'postal_code': request.form.get('postal_code'), 'province': request.form.get('province'), 
                        'country': request.form.get('country')}
        
        errors = controller.edit(client_form, address_form, client_id)
        
        if len(errors) > 0:
            return render_template('clients/edit.html', title='Clients - Edit', client=client, address=address, 
                                   errors=errors)
        else:
            return redirect(url_for('clients.index'))
    
    return render_template('clients/edit.html', title='Clients - Edit', client=client, address=address)


@bp.route('/clients/delete/<client_id>')
@login_required
def delete(client_id):
    controller.delete(client_id)
    return redirect(url_for('clients.index'))


''' API Routes '''


@bp.route('/clients/api/fetch_all')
def fetch_all():
    clients = controller.select_all()
    clients_dicts = []
    
    for client in clients:
        client_dict = client.to_dict()
        clients_dicts.append(client_dict)
    
    return jsonify(clients_dicts)


@bp.route('/clients/api/fetch_by_id/<client_id>')
def fetch_by_id(client_id):
    client = controller.select_by_id(client_id)
    client_dict = client.to_dict()
    
    return jsonify(client_dict)