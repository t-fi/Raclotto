import hashlib
import unittest
from datetime import datetime

from sqlalchemy import event
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from back.test.lib import get_session_const, get_session
from back.src.model.database import SQLiteMixin, Database
from back.src.model.domain.base import Base
from back.src.model.domain.raclotto_session import RaclottoSession
from back.src.model.domain.ingredient import Ingredient, IngredientType
from back.src.model.domain.rating import Rating
from back.src.model.domain.pan import Pan


class TestDomain(SQLiteMixin, unittest.TestCase):
    def setUp(self):
        Database.engine('sqlite://')
        Base.metadata.drop_all(Database.engine())
        Base.metadata.create_all(Database.engine())

    def test_creation(self):
        with Database.session() as session:
            self.assertEqual(session.query(Ingredient).all(), [])
            self.assertEqual(session.query(Pan).all(), [])
            self.assertEqual(session.query(RaclottoSession).all(), [])
            self.assertEqual(session.query(Rating).all(), [])

    def test_insert_ingredient(self):
        with Database.session() as session:
            with session.begin():
                session.add(self._get_ingredient())
            self.assertEqual(len(session.query(Ingredient).all()), 1)
            self.assertEqual(len(session.query(RaclottoSession).all()), 1)

    def test_insert_rating(self):
        with Database.session() as session:
            with session.begin():
                session.add(self._get_ingredient())
                session.add(self._get_rating())
            self.assertEqual(len(session.query(Rating).all()), 1)
            self.assertEqual(len(session.query(RaclottoSession).all()), 1)

    def test_insert_pan(self):
        with Database.session() as session:
            with session.begin():
                session.add(self._get_ingredient())
                session.add(self._get_pan(session))
            self.assertEqual(len(session.query(Pan).all()), 1)
            self.assertEqual(len(session.query(RaclottoSession).all()), 2)

    def test_insert_duplicate_session(self):
        with self.assertRaises(IntegrityError) as ctx:
            with Database.session() as session:
                with session.begin():
                    session.add(get_session_const())
                    session.add(get_session_const())
        self.assertEqual(ctx.exception.__class__, IntegrityError)

    def test_delete(self):
        with Database.session() as session, session.begin():
            session.add(self._get_ingredient())
            self.assertEqual(len(session.query(Ingredient).all()), 1)
            ingredient = session.query(Ingredient).first()
            session.delete(ingredient)
            self.assertEqual(len(session.query(Ingredient).all()), 0)
            self.assertEqual(len(session.query(RaclottoSession).all()), 1)

    def test_delete_associated(self):
        with self.assertRaises(IntegrityError) as ctx:
            with Database.session() as session, session.begin():
                session.add(self._get_ingredient())
                self.assertEqual(len(session.query(Ingredient).all()), 1)
                ingredient = session.query(Ingredient).first()
                session.add(self._get_pan(session))
                session.delete(ingredient)
                self.assertEqual(len(session.query(Ingredient).all()), 0)

        self.assertEqual(ctx.exception.__class__, IntegrityError)

    def _get_pan(self, session):
        return Pan(
            session=get_session(),
            ingredients=[session.query(Ingredient).first()],
            user="AldiAlfi",
            ratings=[]
        )

    def _get_rating(self):
        return Rating(
            user="AldiAlfi",
            rating=5
        )

    def _get_ingredient(self):
        return Ingredient(
            name="Potato",
            session=get_session(),
            type=IngredientType.FILL,
            vegetarian=False,
            vegan=False,
            histamine=False,
            fructose=False,
            lactose=False
        )