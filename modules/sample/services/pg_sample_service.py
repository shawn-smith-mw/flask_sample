from modules.models.sample_data import SampleData
from modules.repository.pg_sample_data_repository import PgSampleDataRepository
from modules.sample.services.sample_service import SampleService
from typing import List

class PgSampleService(SampleService):

    def __init__(self):
        self.repository = PgSampleDataRepository()

    def add_sample_data(self, data) -> None:
        sample = SampleData(data['Data'])
        self.repository.add(sample)

    def get_sample_data(self) -> List[SampleData]:
        return self.repository.get_all()
    