import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.mark.skip(reason='TODO[ex2]: implement price endpoint + dependency; then remove skip')
def test_price_ok_with_override_rate():
    import app.main as m
    def fake_rate(): return 5000.0
    m.app.dependency_overrides[m.get_exchange_rate] = fake_rate
    r = client.get('/price/10')
    m.app.dependency_overrides.clear()
    assert r.status_code == 200
    data = r.json()
    assert data['usd'] == 10
    assert data['rate'] == 5000.0
    assert data['cop'] == 50000.0

@pytest.mark.skip(reason='TODO[ex2]: negative USD returns 400; remove skip')
def test_price_negative_rejected():
    r = client.get('/price/-1')
    assert r.status_code == 400
