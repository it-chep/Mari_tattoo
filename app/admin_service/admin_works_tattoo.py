from app.service.auth import AdminAuth


class AdminWorks(AdminAuth):

    async def create_work(self, work_name):

        pass

    async def update_work(self, work_id):

        pass

    async def delete_work(self, work_id):

        pass


class AdminWorkCategory(AdminAuth):

    async def create_work_category(self, work_name):

        pass

    async def update_work_category(self, work_id):

        pass

    async def delete_work_category(self, work_id):

        pass
