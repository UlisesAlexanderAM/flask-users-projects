#!/usr/bin/env python3
import json

from flask import Blueprint

from flask_users_projects.db import get_db

bp = Blueprint("projects", __name__, url_prefix="/proyecto")


def get_projects(id_proyecto: int):
    query = "SELECT * FROM project WHERE id=?"
    cursor = get_db().cursor()
    projects = cursor.execute(query, (id_proyecto,))

    proyectos = []

    for row in projects:
        for i in range(len(row)):
            proyectos.append(str(row[i]))

    return proyectos


def get_users():
    query = "SELECT * FROM user u JOIN user_role_association_table urt ON u.id = urt.user_id JOIN role r ON urt.role_id=r.id"
    cursor = get_db().cursor()
    users = cursor.execute(query)
    usuarios = []

    for row in users:
        usuarios.append(
            [
                row["id"],
                row["username"],
                str(row["password"]),
                row["profile_picture"],
                row["user_full_name"],
                row["user_id"],
                row["role_id"],
                row["id"],
                row["name"],
                row["description"],
            ]
        )

    return usuarios


def create_dict(projects, users):
    return {"projects": projects, "users": users}


@bp.route("/<id_proyecto>")
def project_name(id_proyecto: int):
    proyectos = get_projects(id_proyecto)
    usuarios = get_users()
    proyectos_usuarios = create_dict(proyectos, usuarios)
    return json.dumps(proyectos_usuarios)
