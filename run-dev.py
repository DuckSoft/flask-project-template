from project import app

if __name__ == '__main__':
    app.run(
        debug=app.config['DEBUG'],
        host=app.config['LISTEN_HOST_DEV'],
        port=app.config['LISTEN_PORT_DEV']
    )
