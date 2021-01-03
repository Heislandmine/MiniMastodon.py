from requests import post
import json
import requests


def create_app(
    client_name: str,
    base_url: str,
    redirect_uris: str = "urn:ietf:wg:oauth:2.0:oob",
    scopes: str = None,
    website: str = None,
    to_file: str = None,
) -> dict:

    request_body: dict = {
        "client_name": client_name,
        "redirect_uris": redirect_uris,
        "scopes": scopes,
        "website": website,
    }

    response: requests.Response = post(base_url + "/api/v1/apps", request_body)
    response_json: dict = json.loads(response.text)
    response_dict: dict = {"status_code": response.status_code, "data": response_json}

    if to_file:
        with open(to_file, "w", encoding="utf-8") as f:
            f.write(response_json["client_id"] + "\n")
            f.write(response_json["client_secret"] + "\n")
            f.write(response_json["vapid_key"] + "\n")

    return response_dict
