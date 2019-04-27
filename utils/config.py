# 配置文件读取项
import os
import yaml

from utils.general_mode import SingletonMetaClass


class ConfigRead(metaclass=SingletonMetaClass):
    """
    简单参数配置   单例模式
    """
    def __init__(self):
        super(ConfigRead, self).__init__()
        self._config_info = {}

    def __getitem__(self, key_str):
        keys = key_str.split('.')
        if len(keys) >= 1:
            result = self._config_info
            for item in keys:
                item = item.upper()
                result = result[item]
            return result

        raise KeyError
    
    def from_yaml(self, filename):
        """
        从Yaml中读取配置项
        """
        with open(filename) as yaml_file:
            map_obj = yaml.load(yaml_file, Loader=yaml.SafeLoader)
            return self.from_mapping(map_obj)

    def from_env(self):
        """
        从环境变量中读取配置 读取以PROJECT_KEY为开头的键
        TODO 键裁剪判断问题
        """
        after_something = {key[12:]: val for key, val in os.environ.items() if key.startswith('PROJECT_KEY')}
        return self.from_mapping(after_something)

    def from_mapping(self, mapping):
        """
        从对象中装换配置项数据
        """
        if not mapping:
            return

        mappings = mapping.items() if hasattr(mapping, 'items') else mapping

        for (key, value) in mappings:
            if key.isupper():
                self._config_info[key] = value
