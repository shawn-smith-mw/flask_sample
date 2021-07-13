import uuid
from modules.repository.pg_sample_data_repository import PgSampleDataRepository
from modules.models.sample_data import SampleData
from modules.db_model import db

repository = PgSampleDataRepository()
def test_get(app):
    with app.app_context():
        id = str(uuid.uuid4())
        sample = SampleData(id)
        db.session.add(sample)
        db.session.commit()
        
        data = repository.get_all()
        contained = False
        for d in data:
            if d['Data'] == id:
                contained = True
        assert contained

def test_add(app):
    with app.app_context():
        id = str(uuid.uuid4())
        sample = SampleData(id)
        repository.add(sample)
        contained = False
        for d in SampleData.query.all():
            if d.Data == id:
                contained = True
        assert contained
