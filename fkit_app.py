from flask import Flask

from api.file_upload_download import file_upload_download_bp
from api.file_show import file_show_bp


app = Flask(__name__, static_url_path='/assets', static_folder='assets')


app.register_blueprint(file_upload_download_bp)
app.register_blueprint(file_show_bp)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
