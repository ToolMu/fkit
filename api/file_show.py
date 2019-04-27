"""
文件项展示部分
"""
import os
import stat

from flask import Blueprint
from flask import request, jsonify

from utils import PROJECT_PATH, KEEP_FILE_PATH


file_show_bp = Blueprint('web', __name__)


@file_show_bp.route('/api/v1/files')
def show_files():
    root_path = PROJECT_PATH + request.args.get('path', KEEP_FILE_PATH)

    res_info = {}
    if os.path.isdir(root_path):
        content = []
        total_info = {'size': 0, 'dir': 0, 'file': 0}
        for file_name in os.listdir(root_path):
            if file_name[0] == '.':
                continue
            file_stat = os.stat(os.path.join(root_path, file_name))
            content.append({
                "name": file_name,
                "mtime": file_stat.st_mode,
                "type": 'dir' if stat.S_ISDIR(file_stat.st_mode) or stat.S_ISLNK(file_stat.st_mode) else 'file',
                "size": file_stat.st_size
            })
            total_info['size'] += file_stat.st_size
            total_info_key = 'dir' if stat.S_ISDIR(file_stat.st_mode) or stat.S_ISLNK(file_stat.st_mode) else 'file'
            total_info[total_info_key] += 1
        res_info.update({
            'code': 20000,
            'files': content,
            'total_info': total_info
        })
    else:
        res_info.update({
            'code': 40000,
            'msg': "Lost"
        })

    return jsonify(res_info)


@file_show_bp.route('/api/v1/file_info')
def show_file_info():
    pass
