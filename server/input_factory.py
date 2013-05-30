class InputHandler(object):

    @staticmethod
    def init_formats(input,workbook):
        """
        Handles the cell formats is any. Json should have on the dictionary a formats key in order to create formats.
        If formats value doesnt exist return empty dict of formats, else add all formats in a dict.
        Structure:
            "formats" : {
                'number' : {'num_format':'$#,##.##'}
            }
        :param input: JSON input as given by client
        :param workbook: the workbook created by xlsx_factory
        :return: Empty dict if no formats are set on JSON, dict format_name : format if formats are specified
        """
        return_dict = {}
        if not input.__contains__('formats'):
            return return_dict
        for k,v in input.pop('formats').items():
            return_dict[k] = workbook.add_format(v)
        return return_dict

    @staticmethod
    def get_args(value,formats):
        """
        Get the cell arguements.
        :param value: The value can be set up as 2 different types at the moment, either 'A1' : 'Item' or
             'A1':{'value':'Item','format':'bold'}.
        :param formats: All possible formats as generated by InputHandler.init_formats
        :return: If only a value given the value is returned else the value of the cell is returned and a the specified
            format
        """

        def is_dict():
            return value['value'],formats[value['format']]
        def is_str():
            return value
        functions = {dict:is_dict,str:is_str}
        return functions[value.__class__]()
