from minimastodon_py.auth import create_app
import os.path


base_url = "http://localhost:3000/"
app_name = "test_app"


def test_create_app():
    response_fields: list = [
        "id",
        "name",
        "website",
        "redirect_uri",
        "client_id",
        "client_secret",
        "vapid_key",
    ]

    res: dict = create_app(app_name, base_url)

    assert 200 == res["status_code"]
    for response_field in response_fields:
        assert response_field in res["data"]


def test_create_app_with_to_file():
    to_file = "client.secret"
    create_app(app_name, base_url, to_file=to_file)

    assert os.path.exists(to_file)
