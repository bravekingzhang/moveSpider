__author__ = 'brzhang'


# -*- coding: utf-8 -*-
import urlparse
from bs4 import BeautifulSoup
import re


class QiDianHtmlParser():
    def __init__(self):
        pass

    def _get_new_links(self, url, soup):
        links_to_be_return = set()
        # Book/3681810.aspx
        links = soup.findAll("a", href=re.compile(r"/Book/\d+.aspx"))
        for link in links:
            links_to_be_return.add(urlparse.urljoin(url, link["href"]))
        return links_to_be_return

    def _get_new_content(self, url, soup):
        content_to_be_return = {}
        content_to_be_return['url'] = url
        try:
            content_to_be_return['book_name'] = soup.find("div", class_="title").find("h1", itemprop="name").text
            content_to_be_return['book_pic'] = \
            soup.find("div", class_="box_cont").find("div", class_="book_pic").find("a").find("img")["src"]
            content_to_be_return['book_some_detail'] = soup.find("div", class_="intro").find("div", class_="txt").find(
                "span").text
        except:
            print "not content to be output"
            return None

        return content_to_be_return

    def parser_html_content(self, url, html_content):
        if html_content is None:
            return None, None
        soup_ojb = BeautifulSoup(html_content, "html.parser", from_encoding="utf-8")
        links = self._get_new_links(url, soup_ojb)
        content = self._get_new_content(url, soup_ojb)
        return links, content