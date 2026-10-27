from fastapi import APIRouter
from strawberry.asgi import GraphQL

from models.index import users
from conn.db import conn

import strawberry

from type.user import Mutation, Query

user = APIRouter()

schema = strawberry.Schema(Query, Mutation)
graphql_app = GraphQL(schema)

user.add_route("/graphql", graphql_app)