from urllib.parse import unquote


def decode(url):
    return unquote(url)


tests = (
    ('http://www.google.bg/search?q=C%23', 'http://www.google.bg/search?q=C#'),
    ('https://mysite.com/show?n%40m3= p3%24h0', 'https://mysite.com/show?n@m3= p3$h0'),
    ('http://url-decoder.com/i%23de%25?id=23', 'http://url-decoder.com/i#de%?id=23'),
)

for (test, expected) in tests:
    actual = decode(test)
    print(actual, expected, actual == expected)
