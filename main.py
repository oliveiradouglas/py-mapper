from pymapper import Mapper

config = {
    'dest_attr_1': '$source_attr_1',
    'dest_nested_attr_1': {
        'dest_attr_2': '$source_nested_attr_1.source_attr_2',
    }
}

source = {
    'source_attr_1': 1,
    'source_nested_attr_1': {
        'source_attr_2': 2
    },
}

mapper = Mapper(config)
print(mapper.map(source))
