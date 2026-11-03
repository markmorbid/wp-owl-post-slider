"""Verify approved sources and local HTML dependencies; standard library only."""
from hashlib import sha256
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
FINAL = {
    'owl-cards.css': '47fc0158483bfe29ebf74706028097d23e0acd6cc55a749f07f20fb258162ae5',
    'owl-cards-final.css': 'a44c916e2fc2b8590976fe319b0d16eef7da52a828ed7892470bcda654d76388',
    'owl-test.html': '74ec04864c866ba5196d349a93a6776fdb02e38b45cdecc6c5e646c42ac259d0',
    'preview.html': '258624b743c5415e21827ce4061d8e88c68c90a82f355c34ddc475f05d3d108c',
    'owl-test-corregido.html': 'dc52ff0b519909b1284206cef2dc2b33b2ba10abac84c255b0732f4a5ef7e2e6',
}

class References(HTMLParser):
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        value = attrs.get('src') if tag in ('script', 'img') else attrs.get('href') if tag == 'link' else None
        if value and not urlsplit(value).scheme and not value.startswith('//'):
            assert (ROOT / urlsplit(value).path).is_file(), f'Missing dependency: {value}'

for name, expected in FINAL.items():
    data = (ROOT / name).read_bytes()
    assert sha256(data).hexdigest() == expected, f'Approved file changed: {name}'
    if name.endswith('.html'):
        References().feed(data.decode('utf-8'))
for name in ('assets/test-cover.svg', 'assets/eb-garamond-latin-500-normal.woff2', 'assets/inconsolata-latin-400-normal.woff2'):
    assert (ROOT / name).is_file(), f'Missing preview asset: {name}'
print('OK: five approved files unchanged; local HTML and preview dependencies present.')
