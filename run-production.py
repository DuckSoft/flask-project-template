"""
Running Script for Production Use
using WSGI in gEvent
"""

if __name__ == '__main__':
    from project import app
    from gevent.wsgi import WSGIServer

    listen_addr = (
        app.config['LISTEN_HOST_PRODUCTION'],
        app.config['LISTEN_PORT_PRODUCTION']
    )

    server = WSGIServer(listen_addr, app)
    server.serve_forever()
