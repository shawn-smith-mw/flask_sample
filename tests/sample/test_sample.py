from modules.sample.services.pg_sample_service import PgSampleService
import uuid
from modules.models.sample_data import SampleData
from modules.db_model import db

sample_service = PgSampleService()
def test_add(app):
    with app.app_context():
        identifier = uuid.uuid4()
        sample_service.add_sample_data({"Data": identifier})
        data = [s.serialize() for s in SampleData.query.all()]
        contained = False
        for item in data:
            if item['Data'] == str(identifier):
                contained = True
        assert contained

def test_get(app):
    with app.app_context():
        identifier = uuid.uuid4()
        sample = SampleData(data=identifier)
        db.session.add(sample)
        db.session.commit()
        data = sample_service.get_sample_data()
        contained = False
        for d in data:
            if d['Data'] == str(identifier):
                contained = True
        assert contained
