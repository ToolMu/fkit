"""
文件上传下载模块 API部分
"""
import os
import json

from flask import Blueprint
from flask import request, make_response, send_file

from utils.extends import secure_filename
from utils import KEEP_FILE_PATH, PROJECT_PATH

file_upload_download_bp = Blueprint('files', __name__)


@file_upload_download_bp.route('/upload', methods=['POST'])
def file_upload():
    root_path = PROJECT_PATH + request.args.get('path', KEEP_FILE_PATH)
    res_info = {}

    if os.path.exists(root_path) and os.path.isdir(root_path):
        # 存在该目录
        upload_file = request.files.get('files')

        if upload_file:
            try:
                upload_file_name = secure_filename(upload_file.filename)
                upload_file.save(os.path.join(root_path, upload_file_name))
            except Exception as e:
                res_info.update({
                    'filename': upload_file.filename,
                    'status': "failure",
                    'msg': str(e)  # TODO 直接交付错误合理？？？
                })
            else:
                res_info.update({
                    'filename': upload_file_name,
                    'status': 'success',
                    'msg': 'Upload File Saved'
                })

        res_info['code'] = 20000
    else:
        res_info['code'] = 40000
        res_info['msg'] = 'Not Exists Dir'

    response = make_response(json.dumps(res_info), 200)
    response.headers.add('Content-type', "application/json")

    return response


@file_upload_download_bp.route('/download')
def file_download():
    file_path = PROJECT_PATH + request.args.get('path', KEEP_FILE_PATH) + '/' + request.args.get('filename')

    if os.path.isfile(file_path):
        res = send_file(file_path)
        res.headers.add('Content-Disposition', 'attachment')
    else:
        res = make_response('Not found', 404)

    return res
