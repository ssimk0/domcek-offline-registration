from pyfladesk import init_gui


PORT = 5000
ROOT_URL = 'http://localhost:{}'.format(PORT)


if __name__ == '__main__':
    from domcek.app import app
    init_gui(app)