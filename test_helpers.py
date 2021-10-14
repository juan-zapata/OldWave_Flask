import json as jsonlib

def response_success(response, code=200):
    if 200 <= code < 300:
        assert 200 <= response.status_code < 300
    assert code == response.status_code

def response_error(response, code=400):
    if 400 <= code < 500:
        assert 400 <= response.status_code < 500
    assert code == response.status_code

def response_redirect(response, target=None):
    assert response.status_code in [301, 302]
    

def json_response(response, code=200):
    # Checks that the status code is OK and returns the json
    assert response.status_code == code
    return jsonlib.loads(response.data)

def check_cookie(response, name, value):
    # Checks for existence of a cookie and verifies the value of it.
    from werkzeug.http import parse_cookie
    cookies = response.headers.getlist('Set-Cookie')
    for cookie in cookies:
        c_key, c_value = parse_cookie(cookie).items()[0]
        if c_key == name:
            assert c_value == value
            return
    # Cookie not found
    assert False