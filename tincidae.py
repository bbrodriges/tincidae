from contextlib import contextmanager
from urllib import request


@contextmanager
def crawl(url):

    """
        @type url str
        @yalds dict

        Returns info about page
    """

    opener = request.build_opener()

    page = {
        'body':    '',
        'url':     url,
        'headers': {},
        'cookies': {},
        'status':  500,
    }

    response = None

    try:
        resp = opener.open(url)
        response = resp
    except request.HTTPError as resp:
        response = resp
    except:
        pass

    if response:
        headers = {h[0]: h[1] for h in response.headers.items()}
        cookies = __parse_cookies(headers)

        page.update({
            'body': str(response.read()),
            'headers': headers,
            'cookies': cookies,
            'status': response.getcode(),
        })

    yield page


def __parse_cookies(headers):

        """
            @type headers dict
            @return dict

            Parses cookies from response headers.
        """

        cookies = {}
        if 'Set-Cookie' in headers:
            raw_cookies = headers['Set-Cookie'].split(';')
            for cookie in raw_cookies:
                cookie = cookie.split('=', 1)
                if cookie[0].strip() and len(cookie) > 1:
                    cookies.update({cookie[0]: cookie[1]})
        return cookies
