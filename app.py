from os import getenv

from app import create_app

if __name__ == '__main__':
    app = create_app()
    app.run(host=getenv('HOST'), port=getenv('PORT'))
