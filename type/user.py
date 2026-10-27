import typing
import strawberry
from models.index import users
from conn.db import conn

@strawberry.type
class User:
    id: int
    name: str
    email: str
    password: str

@strawberry.input
class UserInput:
    name: str
    email: str
    password: str

@strawberry.input
class UserUpdateInput:
    id: int
    name: str
    email: str
    password: str

@strawberry.type
class Query:
    @strawberry.field
    def user(self, id: int) -> User:
        return conn.execute(users.select().where(users.c.id == id)).fetchone()

    @strawberry.field
    def users(self) -> typing.List[User]:
        return conn.execute(users.select()).fetchall()

@strawberry.type
class Mutation:
    @strawberry.mutation
    def createuser(self, user: UserInput) -> int:
        result = conn.execute(
            users.insert().values(
                name=user.name,
                email=user.email,
                password=user.password
            )
        )
        return int(result.inserted_primary_key[0])

    @strawberry.mutation
    def updateuser(self, user: UserUpdateInput) -> str:
        # Fixed: used users.c.id instead of users.id
        result = conn.execute(
            users.update()
            .where(users.c.id == user.id)
            .values(
                name=user.name,
                email=user.email,
                password=user.password
            )
        )
        return f"{result.rowcount} Rows updated"

    @strawberry.mutation
    def delete_user(self, id: int) -> bool:
        result = conn.execute(users.delete().where(users.c.id == id))
        return result.rowcount > 0