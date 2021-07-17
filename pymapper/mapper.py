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
            mapper = Mapper({'bar': 'foo'})
            result = mapper.map(obj)

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

    def map(self, from_dict):
        """Method for creating target dict instance

        :param from_dict: source dict to be mapped from

        :return: Instance of the target dict with mapped attributes
        """
        result = self.__mappings.copy()
        for k, v in result.items():
            if (isinstance(result[k], dict)):
                pass
            if (isinstance(result[k], list)):
                pass
            else:
                result[k] = self.__map_value(from_dict, v)
        return result
