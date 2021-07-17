class Mapper:
    """
        Base class for mapping dict attributes from one dict to another one
    """

    def __init__(self, mappings=None):
        """Constructor

        Args:
            mappings: dictionary of the attribute conversions

        Examples:
            1. Mapping flat object
            In this case the mapping definition should be a dict with the destination keys,
            and the source path as the correspondent values.

            Initialization of the Mapper will be:
                obj = {'foo': 1}
                mapper = Mapper({'bar': '$foo'})
                result = mapper.map(obj)

            In this case result['bar'] will be equals to 1

            2. Mapping nested object
            In this case the mapping definition should be a dict with the destination keys,
            and the source path as the correspondent values.

            Initialization of the Mapper will be:
                obj = {'foo': {'baz': 1}}
                mapper = Mapper({'bar': '$foo.baz'})
                result = mapper.map(obj)

            In this case result['bar'] will be equals to 1

            2. Mapping with nested mapping definition
            In this case the mapping definition should be a dict with the destination keys,
            and the source path as the correspondent values.

            Initialization of the Mapper will be:
                obj = {'foo': {'baz': 1}}
                mapper = Mapper({'bar': {'foo2': '$foo.baz'}})
                result = mapper.map(obj)

            In this case result['bar']['foo2'] will be equals to 1

        :return: Instance of the ObjectMapper
        """
        self.__mappings = mappings

    def __map_value(self, from_dict, attr_key):
        attr_value = from_dict
        # attr_key[1:] to ignore the '$' sign
        # TODO: Attribute Interpolation
        for attr_section in attr_key[1:].split('.'):
            attr_value = attr_value[attr_section]
        return attr_value

    def __map_dict(self, from_dict, mappings):
        result = mappings.copy()
        for k, v in result.items():
            if (isinstance(v, dict)):
                result[k] = self.__map_dict(from_dict, v)
            elif (isinstance(v, list)):
                pass
            else:
                result[k] = self.__map_value(from_dict, v)
        return result

    def map(self, from_dict):
        """Method for creating target dict instance

        :param from_dict: source dict to be mapped from

        :return: Instance of the target dict with mapped attributes
        """
        result = None
        if isinstance(from_dict, dict):
            result = self.__map_dict(from_dict, self.__mappings)
        return result
