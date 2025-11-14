from app import app

def test_add():
    client = app.test_client()
    r = client.get("/add?a=2&b=3")
    assert r.get_json()["result"] == 5
