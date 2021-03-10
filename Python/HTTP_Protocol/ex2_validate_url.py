from urllib import parse


class UrlValidation:
    @staticmethod
    def __get_host(netloc):
        if '.' not in netloc:
            return None

        return netloc.split(':')[0] if ':' in netloc else netloc

    @staticmethod
    def __get_port(netloc, scheme):
        if ':' in netloc:
            return netloc.split(':')[1]
        if scheme == 'http':
            return 80
        elif scheme == 'https':
            return 443
        else:
            return None

    @staticmethod
    def __get_path(path):
        return path or '/'

    @staticmethod
    def validate_url(url):
        components = parse.urlparse(url)
        result = {
            'Protocol': components.scheme,
            'Host': UrlValidation.__get_host(components.netloc),
            'Port': UrlValidation.__get_port(components.netloc, components.scheme),
            'Path': UrlValidation.__get_path(components.path),
            'Query': components.query,
            'Fragment': components.fragment,
        }

        required_components_names = (
            'Protocol',
            'Host',
            'Port',
            'Path',
        )

        are_required_components_present = all(result[name] for name in required_components_names)

        if are_required_components_present:
            for el in result.items():
                if el[1]:
                    print(f'{el[0]}: {el[1]}')
            print()
        else:
            print('Invalid URL')


validate_url = UrlValidation().validate_url

valid_tests = [
    'http://softuni.bg/',
    'https://softuni.bg:447/search?Query=pesho&Users=true#go',
    'http://mysite.com:80/demo/index.aspx',
    'https://my-site.bg',
    'https://mysite.bg/demo/search?id=22o#go',
    'https://mysite.bg/demo/search?id=22o&name=Doncho#go'
]


invalid_tests = [
    'https://mysite:80/demo/index.aspx',
    'somesite.com:80/search?',
    'https/mysite.bg?id=2',
    'http://google:443/',
]

[validate_url(url) for url in valid_tests + invalid_tests]
