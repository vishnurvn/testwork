import unittest

from source.utils import yaml_config


class TestMisc(unittest.TestCase):

    def test_yaml_config(self):
        data = {
            'test_key': 'value',
            'test_key_two': ['value_one', 'value_two'],
            'test_key_three': {
                'test_sub_key': 'value'
            }
        }
        config = yaml_config('./test_data/config.yaml')
        self.assertDictEqual(data, config)


if __name__ == '__main__':
    unittest.main()
