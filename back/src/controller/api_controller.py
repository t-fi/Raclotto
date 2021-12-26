import json

from back.src.model.service.ingredient_service import IngredientService
from back.src.model.service.pan_service import PanService
from back.src.model.service.rating_service import RatingService
from back.src.model.service.session_service import SessionService
from back.src.view.api_view import ApiView


class ApiController:
    def __init__(self):
        self.view = ApiView()
        self.ingredient_service = IngredientService()
        self.pan_service = PanService()
        self.rating_service = RatingService()
        self.session_service = SessionService()

    def get_ingredients(self, session_id, of_type=None):
        items = self.ingredient_service.all(session_id, of_type)
        return self.view.get(items)

    def get_pans(self, session_id):
        items = self.pan_service.all(session_id)
        return self.view.get(items)

    def get_ratings(self, session_id):
        items = self.rating_service.all(session_id)
        return self.view.get(items)

    def add_ingredient(self, json_str):
        parsed = json.loads(json_str)
        self.ingredient_service.add(parsed)

    def add_pan(self, json_str):
        parsed = json.loads(json_str)
        self.pan_service.add(parsed)

    def add_rating(self, json_str):
        parsed = json.loads(json_str)
        self.rating_service.add(parsed)

    def del_ingredient(self, session_key, obj_id):
        self.ingredient_service.delete(session_key, obj_id)

    def gen_pan(self, json_str):
        parsed = json.loads(json_str)
        pan = self.pan_service.generate(parsed)
        return self.view.get(pan)

    def validate(self, session_key):
        validation = self.session_service.validate(session_key)
        return self.view.scalar(session_key, validation)
