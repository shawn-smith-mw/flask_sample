from modules.models.sample_data import SampleData
from typing import List,Dict

class SampleDataRespository:
    def get_all(self) -> list:
        raise NotImplementedError


    def add(self, data) -> None:
        raise NotImplementedError
