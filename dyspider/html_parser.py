# -*- coding: utf-8 -*-
import urlparse
from bs4 import BeautifulSoup
import re


class HtmlParser:
    def __init__(self):
        pass

    def _get_new_links(self, url, soup):
        links_to_be_return = set()
        links = soup.findAll("a", href=re.compile(r"/html/gndy/[a-z]+/\d+/\d+.html"))
        for link in links:
            links_to_be_return.add(urlparse.urljoin(url, link["href"]))
        return links_to_be_return

    def _get_new_content(self, url, soup):
        content_to_be_return = {}
        content_to_be_return['url'] = url
        try:
            content_to_be_return['move_name'] = soup.find("div",class_="bd3r").find("div", class_="co_area2").find("div", class_="title_all").text
            content_to_be_return['move_pic'] = soup.find("div", id="Zoom").find("span").find("p").find("img")["src"]
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
