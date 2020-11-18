from flask import Blueprint, request, render_template, redirect, url_for

from . import CategoriesController

bp = Blueprint('categories', __name__)

controller = CategoriesController()


@bp.route('/categories')
@bp.route('/categories/index')
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
        
    categories = controller.select_in_range(page, limit)
    num_pages = controller.number_of_pages(limit)
    
    return render_template('categories/index.html', title='Categories - Index', categories=categories, 
                           num_page=num_pages, page=page, limit=limit)


@bp.route('/categories/create', methods=['GET', 'POST'])
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