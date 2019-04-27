import os

from utils.config import ConfigRead


PROJECT_PATH = os.path.join(
    os.path.abspath(os.path.dirname(__file__)),
    '../'
)

# 读取配置项
config_read = ConfigRead()
base_config = PROJECT_PATH + '/conf/base.yaml'

config_read.from_yaml(base_config)


KEEP_FILE_PATH = config_read['file_path']
