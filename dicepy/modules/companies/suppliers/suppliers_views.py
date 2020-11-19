from dicepy.modules.addresses import addresses_controller
from flask import Blueprint, request, render_template, redirect, url_for, jsonify

from . import SuppliersController
from ...addresses import AddressesController
from dicepy.lib.middleware.auth_middleware import login_required

bp = Blueprint('suppliers', __name__)
controller = SuppliersController()
addresses_controller = AddressesController()


@bp.route('/suppliers')
@bp.route('/suppliers/index')
@login_required
def index():
    page = None
    limit = None
    
    # Set page parameters
    if 'page' in request.args:
        page = int(request.args.get('page'))
    else:
        page = 1
    if 'limit' in request.args:
        limit = int(request.args.get('limit'))
        
    suppliers, num_pages = controller.select_in_range(page, limit)
    
    return render_template('suppliers/index.html', title='Suppliers - Index', suppliers=suppliers, 
                           num_pages=num_pages, page=page, limit=limit)


@bp.route('/suppliers/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        form = {'company_name': request.form.get('')}
    
    return render_template('suppliers/create.html', title='Suppliers - Create')


@bp.route('/suppliers/edit/<supplier_id>', methods=['GET', 'POST'])
@login_required
def edit(supplier_id):
    return render_template('suppliers/edit.html', title='Suppliers - Edit')


@bp.route('/suppliers/delete/<supplier_id>')
@login_required
def delete(supplier_id):
    return redirect(url_for('suppliers.index'))