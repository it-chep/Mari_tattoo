from app.repository.tattoo.tattoo import TattooRepository
from fastapi import Depends


class TattooService:
    def __init__(self, tattoo_repository=Depends(TattooRepository)):
        self.tattoo_repository = tattoo_repository

    def get_all_jobs(self):
        works = self.tattoo_repository.works_repository.get_all()
        return works

    def main_tattoo_page(self):
        pass

    def get_calculate_tattoo(self):
        pass

    def post_calculate_tattoo(self):
        pass

    def get_tattoo_sketches(self):
        pass

    def get_random_sketch(self):
        pass

