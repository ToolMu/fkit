import os
from unittest import TestCase

from utils.config import ConfigRead


class TestConfigRead(TestCase):
    def test_from_mapping(self):
        config_read = ConfigRead()
        config_read.from_mapping({"TEST_WEB_KEY": 0})
        self.assertEqual(config_read['test_web_key'], 0)

    def test_from_yaml(self):
        config_read = ConfigRead()
        config_read.from_yaml('../data/config.yaml')
        self.assertEqual(config_read['readme'], {'READ': "ok"})

    def test_from_env(self):
        os.environ['PROJECT_KEY_TEST_ENV_WEB_KEY'] = 'True'
        config_read = ConfigRead()
        config_read.from_env()
        self.assertEqual(config_read['test_env_web_key'], 'True')
