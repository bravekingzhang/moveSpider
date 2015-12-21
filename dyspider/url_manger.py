# -*- coding: utf-8 -*-


class UrlManger:
    def __init__(self):
        self.new_urls = set()
        self.already_visit_url = set();

    def add_new_url(self, url):
        if url is None or url in self.new_urls or url in self.already_visit_url:
            return
        self.new_urls.add(url)

    def has_new_url(self):
        return len(self.new_urls) != 0

    def offer_new_url(self):
        if len(self.new_urls) == 0:
            return None
        new_url = self.new_urls.pop()
        self.already_visit_url.add(new_url)
        return new_url

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)
