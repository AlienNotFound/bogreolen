from backend.services.base_service import BaseService

class GeneralValidator(BaseService):
    @staticmethod
    def validate_entry_exists(model, type, id_column, id):
        entry = BaseService.get_by_id(model=model, id_column=id_column, id=id)
        if not entry:
            return False, f'{type} does not exist.'
        else:
            return True, entry
        
    @staticmethod
    def validate_required_fields(fields):
        empty_fields_array = []
        empty_fields_string = ""

        for input in fields:
            if not fields.get(input):
                empty_fields_array.append(input)

        for index, input in enumerate(empty_fields_array):
            if index == 0:
                empty_fields_string = empty_fields_string + input.capitalize()
            elif index == len(empty_fields_array) - 1:
                empty_fields_string = empty_fields_string + " and " + input
            else:
                empty_fields_string = empty_fields_string + ", " + input

        if empty_fields_string:
            return False, empty_fields_string