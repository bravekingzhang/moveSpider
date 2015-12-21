# -*- coding: utf-8 -*-

from dyspider import url_manger, html_downloader, html_parser, move_outputer


class SpiderMain:
    def __init__(self):
        self.urls = url_manger.UrlManger()
        self.downloader = html_downloader.HtmlDownloader()
        self.htmlParser = html_parser.HtmlParser()
        self.moveOutputer = move_outputer.MoveOutputer()

    def clawer(self, root_url):
        self.urls.add_new_url(root_url)
        i = 0
        while self.urls.has_new_url():
            try:
                if i > 100:
                    break
                current_url = self.urls.offer_new_url()
                print "current task is %d donwload url is %s" % (i, current_url)
                html_content = self.downloader.fectch_content(current_url)
                new_urls, new_content = self.htmlParser.parser_html_content(current_url, html_content)
                self.urls.add_new_urls(new_urls)
                self.moveOutputer.collect_data(new_content)
                i = i + 1
            except:
                print "netowrk err %s" % current_url

        self.moveOutputer.out_put_data()


if __name__ == '__main__':
    start_url = "http://www.dytt8.net/html/gndy/dyzz/20151220/49782.html"
    spiderObj = SpiderMain()
    spiderObj.clawer(start_url)
