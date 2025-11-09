from backend.services.base_service import BaseService

class GeneralValidator(BaseService):
    @staticmethod
    def validate_entry_exists(model, type, id_column, id):
        entry = BaseService.get_by_id(model=model, id_column=id_column, id=id)
        if not entry:
            return False, f'{type} does not exist.'
        else:
            return True, entry