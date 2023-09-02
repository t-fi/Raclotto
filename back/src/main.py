from flask import Flask, request, render_template
from flask_cors import CORS
from flask_restless import APIManager
from flask_sqlalchemy import SQLAlchemy

from back.src.driver.app import App
from back.src.driver.config import ConfigInMemory
from back.src.driver.database import db

# @app.route("/")
# def index():
#     return render_template("index.html")
#
#
# @app.route("/api/generate/", methods=["POST"])
# def api_generate():
#     res = api.generate(request.json)
#
#     return app.response_class(
#         response=res,
#         status=200,
#         mimetype="application/json"
#     )
#
#
# @app.route("/api/sessions/validate/", methods=["GET"])
# def api_sessions_validate():
#     session_key = request.args.get("session_key")
#     res = api.validate(session_key)
#
#     return app.response_class(
#         response=res,
#         status=200,
#         mimetype="application/json"
#     )
#
#
# @app.route("/api/session/", methods=["GET"])
# def api_session():
#     session_key = request.args.get("session_key")
#     res = api.get_session(session_key)
#
#     return app.response_class(
#         response=res,
#         status=200,
#         mimetype="application/json"
#     )
#
#
# @app.route("/api/sessions/create/", methods=["POST"])
# def api_sessions_create():
#     res = api.add_session(request.json)
#
#     return app.response_class(
#         response=res,
#         status=200,
#         mimetype="application/json"
#     )
#
#
# @app.route("/api/sessions/", methods=["GET", "POST"])
# def api_sessions():
#     if request.method == "GET":
#         res = api.get_sessions()
#         return app.response_class(
#             response=res,
#             status=200,
#             mimetype="application/json"
#         )
#     else:
#         pass
#
#
# @app.route("/api/sessions/close", methods=["POST"])
# def api_sessions_close():
#     res = api.close_session(request.json)
#
#     return app.response_class(
#         response=res,
#         status=200,
#         mimetype="application/json"
#     )
#
#
# @app.route("/api/ingredients/", methods=["GET", "POST"])
# def api_ingredients():
#     if request.method == "GET":
#         session_id = request.args.get("session_key")
#         if request.args.get("type"):
#             res = api.get_ingredients(session_id, request.args.get("type"))
#         else:
#             res = api.get_ingredients(session_id)
#     else:
#         res = api.add_ingredient(request.json)
#
#     return app.response_class(
#         response=res,
#         status=200,
#         mimetype="application/json"
#     )
#
#
# @app.route("/api/ingredients/delete/", methods=["POST"])
# def api_ingredients_remove():
#     res = api.del_ingredient(request.json)
#
#     return app.response_class(
#         response=res,
#         status=200,
#         mimetype="application/json"
#     )
#
#
# @app.route("/api/ingredients/refill", methods=["POST"])
# def api_ingredients_refill():
#     res = api.ref_ingredient(request.json)
#
#     return app.response_class(
#         response=res,
#         status=200,
#         mimetype="application/json"
#     )
#
#
# @app.route("/api/pans/", methods=["GET", "POST"])
# def api_pans():
#     if request.method == "GET":
#         res = api.get_pans(request.args.get("session_key"))
#         return app.response_class(
#             response=res,
#             status=200,
#             mimetype="application/json"
#         )
#     else:
#         api.add_pan(request.json)
#
#
# @app.route("/api/ratings/", methods=["GET", "POST"])
# def api_ratings():
#     if request.method == "GET":
#         res = api.get_ratings(request.args.get("session_key"))
#     else:
#         res = api.add_rating(request.json)
#
#     return app.response_class(
#         response=res,
#         status=200,
#         mimetype="application/json"
#     )
#
#
# @app.route("/api/achievements/", methods=["GET"])
# def api_achievements():
#     res = api.get_achievements()
#
#     return app.response_class(
#         response=res,
#         status=200,
#         mimetype="application/json"
#     )


if __name__ == '__main__':
    api = App("raclotto-server", db, ConfigInMemory)
    api.run(port=3001)
