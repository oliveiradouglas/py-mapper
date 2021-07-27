import unittest
from pymapper import Mapper


class TestMapper(unittest.TestCase):
    """ Unit test class """

    def test_flat_mapping(self):
        """ Test flat dict mapping """
        m = Mapper(
            {
                'dest_attr_1': '$source_attr_1',
                'dest_attr_2': '$source_attr_2',
            })

        source = {
            'source_attr_1': 1,
            'source_attr_2': 2,
        }

        result = m.map(source)

        assert source['source_attr_1'] == result['dest_attr_1']
        assert source['source_attr_2'] == result['dest_attr_2']

    def test_nested_source_mapping(self):
        """ Test nested source mapping """
        m = Mapper(
            {
                'dest_attr_1': '$source_attr_1',
                'dest_attr_2': '$source_nested_attr_1.source_attr_2',
            })

        source = {
            'source_attr_1': 1,
            'source_nested_attr_1': {
                'source_attr_2': 2
            },
        }

        result = m.map(source)

        assert source['source_attr_1'] == result['dest_attr_1']
        assert source['source_nested_attr_1']['source_attr_2'] == result['dest_attr_2']

    def test_nested_destination_mapping(self):
        """ Test nested destination mapping """
        m = Mapper(
            {
                'dest_attr_1': '$source_attr_1',
                'dest_nested_attr_1': {
                    'dest_attr_2': '$source_attr_2',
                }
            })

        source = {
            'source_attr_1': 1,
            'source_attr_2': 2,
        }

        result = m.map(source)

        assert source['source_attr_1'] == result['dest_attr_1']
        assert source['source_attr_2'] == result['dest_nested_attr_1']['dest_attr_2']

    def test_nested_destination_and_source_mapping(self):
        """ Test complex mapping """
        m = Mapper(
            {
                'dest_attr_1': '$source_attr_1',
                'dest_nested_attr_1': {
                    'dest_attr_2': '$source_nested_attr_1.source_attr_2',
                }
            })

        source = {
            'source_attr_1': 1,
            'source_nested_attr_1': {
                'source_attr_2': 2
            },
        }

        result = m.map(source)

        assert source['source_attr_1'] == result['dest_attr_1']
        assert source['source_nested_attr_1']['source_attr_2'] == result['dest_nested_attr_1']['dest_attr_2']

    def test_list_source_mapping(self):
        """ Test list mapping """
        m = Mapper(
            {
                'dest_attr_1': '$source_attr_1',
                'dest_attr_2': '$source_attr_2'
            })

        source = [
            {
                'source_attr_1': 1,
                'source_attr_2': 2
            },
            {
                'source_attr_1': 3,
                'source_attr_2': 4
            }
        ]

        result = m.map(source)

        assert source[0]['source_attr_1'] == result[0]['dest_attr_1']
        assert source[0]['source_attr_2'] == result[0]['dest_attr_2']
        assert source[1]['source_attr_1'] == result[1]['dest_attr_1']
        assert source[1]['source_attr_2'] == result[1]['dest_attr_2']

    def test_dest_obj_list_mapping(self):
        """ Test list mapping """
        m = Mapper(
            {
                'dest_attr_4': '$source_attr_2.source_attr_4'
            })

        source = {
            'source_attr_1': 1,
            'source_attr_2': [
                {
                    'source_attr_3': 3,
                    'source_attr_4': {
                        'source_attr_5': 5
                    }
                }
            ]
        }

        result = m.map(source)

        assert source['source_attr_2'][0]['source_attr_4']['source_attr_5'] == result['dest_attr_4'][0]['source_attr_5']

if __name__ == '__main__':
    unittest.main()
