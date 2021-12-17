from sqlalchemy.orm import Session, joinedload

from back.src.model.database import Database
from back.src.model.domain.pan import Pan
from back.src.model.service.database_service import DatabaseService
from back.src.model.service.ingredient_service import IngredientService


class PanService(DatabaseService):
    def __init__(self):
        super().__init__(Pan)
        self.ingredient_service = IngredientService()

    def all(self, session_id=None):
        with Session(Database.engine()) as session:
            if session_id:
                return session.query(Pan)\
                    .options(joinedload(Pan.ratings), joinedload(Pan.ingredients))\
                    .filter(Pan.session_id == session_id)\
                    .all()
            else:
                return session.query(self.domain_type).all()

    def add(self, obj_dict):
        ingredients = []
        for i in obj_dict["ingredients"]:
            ingredients.append(self.ingredient_service.find(i))
        obj_dict["ingredients"] = ingredients

        with Session(Database.engine()) as session, session.begin():
            session.add(Pan(**obj_dict))
