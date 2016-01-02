# -*- coding: utf-8 -*-
import json


class MoveOutputer:
    def __init__(self):
        self.contents = []
        pass

    def collect_data(self, content):
        if content is not None:
            self.contents.append(content)

    def out_put_data(self):
        opener = open("out.html", "w")
        opener.write("<html>")
        opener.write("<table>")
        for content in self.contents:
            if content is None:
                continue
            opener.write("<tr>")
            opener.write('<td><a href="%s">here</a></td>' % content['url'])
            opener.write('<td>%s</td>' % content['move_name'].encode('utf-8'))
            opener.write('<td><img src="%s"></td>' % content['move_pic'].encode('utf-8'))
            opener.write('</tr>')
        opener.write("</table>")
        opener.write("</html>")

        with open('data.json', 'w') as outfile:
            json.dump(self.contents, outfile)
