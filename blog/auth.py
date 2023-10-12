import click
from blog.database import mongo
from werkzeug.security import generate_password_hash, check_password_hash
from flask_simplelogin import SimpleLogin



def create_user(**data: dict) -> dict[str, str|bool]:
    """
    Creates user with encrypted password.
    
    ARGS:
        data (dict): Dictionary with username and password.
    """
    if not data['username'] and not data['password']:
        raise ValueError('Username and password are required!')
    
    try:
        data['password'] = generate_password_hash(data['password'], method='pbkdf2:sha256')
        mongo.db.users.insert_one(data)
        return {'msg': 'User created successfully!', 'created': True}
    except Exception as e:
        return {'msg': str(e), 'created': False}
    


def validate_login(data: dict) -> bool:
    """
    Check if user exists and password is correct.

    RETURNS:
        True -> User exists and password is correct.\n
        False -> User does not exist or password is incorrect.
    """
    if not data['username'] and not data['password']:
        raise ValueError('Username and password are required!')

    db_user = mongo.db.users.find_one({"username": data['username']})
    return db_user and check_password_hash(db_user['password'], data['password'])
    

def configure(app):
    SimpleLogin(app, login_checker=validate_login)

    @app.cli.command()
    @click.argument('username')
    @click.password_option()
    def add_user(username, password):
        """Add a new user to the database."""
        result = create_user(username=username, password=password)
        if result['created']:
            click.echo(f'User {username} created successfully!')
        else:
            click.echo(f'Error: {result["msg"]}')