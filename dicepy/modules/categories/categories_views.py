from flask import Blueprint, request, render_template, redirect, url_for

from . import CategoriesController
from dicepy.lib.middleware.auth_middleware import login_required

bp = Blueprint('categories', __name__)

controller = CategoriesController()


@bp.route('/categories')
@bp.route('/categories/index')
@login_required
def index():
    ''' Displays all categories from the database '''
    
    ''' Set page parameters '''
    page = None
    limit = None
    
    if 'page' in request.args:
        page = int(request.args['page'])
    else:
        page = 1
    
    if 'limit' in request.args:
        limit = int(request.args['limit'])
    else:
        limit = 10
        
    print('Page: ' + str(page))
    print('Limit: ' + str(limit))
    
    categories = controller.select_in_range(page, limit)
    num_pages = controller.number_of_pages(limit)
    
    print('Number of Pages: ' + str(num_pages))
    
    return render_template('categories/index.html', title='Categories - Index', categories=categories, 
                           num_pages=num_pages, page=page, limit=limit)


@bp.route('/categories/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        form = {'category_name': request.form.get('name'), 'description': request.form.get('description'), 
                'notes': request.form.get('notes')}
        
        errors = controller.create(form)
        
        if len(errors) > 0:
            return render_template('categories/create.html', title='Categories - Create', errors=errors)
        else:
            return redirect(url_for('categories.index'))
    
    return render_template('categories/create.html', title='Categories - Create')


@bp.route('/categories/edit/<category_id>', methods=['GET', 'POST'])
@login_required
def edit(category_id):
    c_id = category_id
    
    if request.method == 'POST':
        form = {'category_name': request.form.get('name'), 'description': request.form.get('description'), 
                'notes': request.form.get('notes')}
        
        errors = controller.edit(c_id, form)
        
        if len(errors) > 0:
            return render_template('categories/edit.html', title='Categories - Edit', errors=errors)
        else:
            return redirect(url_for('categories.index'))
        
    category = controller.select_by_id(c_id)
    
    return render_template('categories/edit.html', title='Categories - Edit', category=category)


@bp.route('/categories/delete/<category_id>')
@login_required
def delete(category_id):
    controller.delete(category_id)
    
    return redirect(url_for('categories.index'))