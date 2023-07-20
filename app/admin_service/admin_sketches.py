from app.service.auth import AdminAuth


class AdminSketch(AdminAuth):

    async def create_sketch(self, sketch_name):
        pass

    async def update_sketch(self, sketch_id):
        pass

    async def delete_sketch(self, sketch_id):
        pass


class AdminSketchCategory(AdminAuth):

    async def create_sketch_category(self, sketch_category_name):
        pass

    async def update_sketch_category(self, sketch_category_id):
        pass

    async def delete_sketch_category(self, sketch_category_id):
        pass
