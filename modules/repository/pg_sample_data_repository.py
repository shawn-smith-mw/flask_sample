from modules.repository.sample_data_repository import SampleDataRespository
from modules.models.sample_data import SampleData
from modules.db_model import db

class PgSampleDataRepository(SampleDataRespository):

    def __init__(self):
        self.db = db


    def get_all(self) -> list:
        sample_data = SampleData.query.all()
        return [s.serialize() for s in sample_data]


    def add(self, data: SampleData) -> None:
        db.session.add(data)
        db.session.commit()
