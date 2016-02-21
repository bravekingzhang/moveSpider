# -*- coding: utf-8 -*-

import urllib2

import cookielib


class HtmlDownloader:
    def __init__(self):
        pass

    def fectch_content(self, url):
        if url is None:
            return
        cj = cookielib.CookieJar()
        cook_handler = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        urllib2.install_opener(cook_handler)
        req = urllib2.Request(url)
        req.add_header("User-Agent", "Mozilla/5.0")
        response = urllib2.urlopen(req)
        if response.code == 200:
            try:
                if url.startswith("http://www.dytt8.net/"):
                    return response.read().decode('gbk').encode('utf-8')
                else:
                    return response.read()
            except:
                return None
        else:
            return None
