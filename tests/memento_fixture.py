import re

MEMENTO_DATETIME = 'Memento-Datetime'
ACCEPT_DATETIME = 'Accept-Datetime'
LINK = 'Link'
VARY = 'Vary'
LINK_FORMAT = 'application/link-format'

class MementoMixin(object):
    def get_links(self, resp):
        return list(map(lambda x: x.strip(), re.split(', (?![0-9])', resp.headers[LINK])))

    def make_timemap_link(self, url, coll='pywb'):
        format_ = '<http://localhost:80/{2}/timemap/link/{0}>; rel="timemap"; type="{1}"'
        return format_.format(url, LINK_FORMAT, coll)

    def make_original_link(self, url):
        format_ = '<{0}>; rel="original"'
        return format_.format(url)

    def make_timegate_link(self, url, fmod='', coll='pywb'):
        fmod_slash = fmod + '/' if fmod else ''
        format_ = '<http://localhost:80/{2}/{1}{0}>; rel="timegate"'
        return format_.format(url, fmod_slash, coll)

    def make_memento_link(self, url, ts, dt, fmod='', coll='pywb'):
        format_ = '<http://localhost:80/{4}/{1}{3}/{0}>; rel="memento"; datetime="{2}"'
        return format_.format(url, ts, dt, fmod, coll)


