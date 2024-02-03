from urllib.parse import urljoin

BASE_API_URL = "https://hackapi.hellozelf.com/backend/api/v1/"


def get_content_url(page):
    return urljoin(BASE_API_URL, f"contents?page={page}")


def get_author_url(author_id):
    return urljoin(BASE_API_URL, f"authors/{author_id}")


def get_headers():
    return {'x-api-key': '3e767e3bsk_c3d4sk_4748sk_a8d7sk_b287fce835c91706933458'}
