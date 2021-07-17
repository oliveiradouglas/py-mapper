import unittest
from pymapper import Mapper


class TestMapper(unittest.TestCase):
    """ Unit test class """

    def test_flat_mapping(self):
        """ Test flat object mapping """
        m = Mapper(
            {
                'dest_attr_1': 'source_attr_1',
                'dest_attr_2': 'source_attr_2',
            })

        source = {
            'source_attr_1': 1,
            'source_attr_2': 2,
        }

        result = m.map(source)

        assert source['source_attr_1'] == result['dest_attr_1']
        assert source['source_attr_2'] == result['dest_attr_2']


if __name__ == '__main__':
    unittest.main()
