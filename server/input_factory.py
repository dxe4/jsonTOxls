class InputHandler(object):

    @staticmethod
    def foo():
        print("dsadsa")

    def init_formats(input,workbook):
        return_dict = {}
        if not input.__contains__('formats'):
            return return_dict
        for k,v in input.pop('formats').items():
            return_dict[k] = workbook.add_format(v)
        return return_dict

    def get_args(value,formats):
        def is_dict():
            return value['value'],formats[value['format']]
        def is_str():
            return value
        functions = {dict:is_dict,str:is_str}
        return functions[value.__class__]()
