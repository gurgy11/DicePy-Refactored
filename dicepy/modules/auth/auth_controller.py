from dicepy.lib.controller.controller import Controller
from flask import current_app, session, redirect, url_for


class AuthController(Controller):
    
    def set_user_in_session(self, user_id, user_username):
        ''' Sets a session variable for the user's ID and username '''
        
        with current_app.app_context():
            
            session['user_id'] = user_id
            session['user_username'] = user_username
            
    def remove_user_from_session(self):
        ''' Removes the user's ID and username from the session '''
        
        with current_app.app_context():
            
            if 'user_id' in session:
                session.pop('user_id')
                
            if 'user_username' in session:
                session.pop('user_username')
                
    def get_user_from_session(self):
        ''' Gets the user's ID and username from the session '''
        
        with current_app.app_context():
            
            user_id = session.get('user_id')
            user_username = session.get('user_username')
            
            user_params = {'user_id': user_id, 'user_username': user_username}
            
            return user_params
        
    def authenticated(self):
        ''' Checks if user's ID and username is in the session '''
        
        with current_app.app_context():
            
            if 'user_id' in session and 'user_username' in session:
                return True
            else:
                return False
            
    def login_required(self):
        ''' Protects a page where only logged in user's can access '''
        
        with current_app.app_context():
            
            if self.authenticated() is not True:
                
                return redirect(url_for('auth.login_required'))