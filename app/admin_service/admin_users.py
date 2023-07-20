from app.service.auth import AdminAuth
from app.utils.hash import Hasher


class AdminUsers(AdminAuth):
    async def get_all_users(self, session_id):
        status, admin = self.auth_user(session_id)

        if status == 403:
            return 403, {"message": "You have not admin cookie"}

        users = await self.cache.get_value(key='users')

        if not users:
            users = await self.users_repository.get_all_users()
            for user in users:
                await self.cache.set_value(key=f'user{user.user_id}', value=f'{user}', timeout=10000)
        return users

    async def get_user_by_id(self, session_id, user_id):
        status, admin = self.auth_user(session_id)

        if status == 403:
            return 403, {"message": "You have not admin cookie"}

        result = await self.users_repository.get_user_by_id(user_id)

        return result

    async def get_user_by_email(self, session_id, email):
        status, admin = self.auth_user(session_id)

        if status == 403:
            return 403, {"message": "You have not admin cookie"}

        result = await self.users_repository.get_user_by_email(email)
        return result

    async def create_new_user(self, session_id, name: str, surname: str, email: str, password: str):
        status, admin = self.auth_user(session_id)

        if status == 403:
            return 403, {"message": "You have not admin cookie"}

        hashed_password = Hasher.get_password_hash(password=password)

        result = await self.users_repository.create_new_user(name=name, surname=surname, email=email,
                                                       hashed_password=hashed_password)

        return result

    async def update_user(self, session_id, user_id):
        status, admin = self.auth_user(session_id)

        if status == 403:
            return 403, {"message": "You have not admin cookie"}