#!/usr/lib/env/python2.7
#encoding=utf-8
#pathName : html_outputer.py

class HtmlOutputer(object):
    def __init__(self):
	self.datas = [];

    def collect_data(self, data):
	if data is None:
	    return
	self.datas.append(data);

    def output_html(self):
	file_output = open("output.html", "w");

	file_output.write("<html>");
	file_output.write("<body>");
	file_output.write("<table>");

	for data in self.datas:
            file_output.write("<tr>");
	    file_output.write("<td>%s</td>" % data['url']);
	    file_output.write("<td>%s</td>" % data['title'].encode("utf-8"));
	    file_output.write("<td>%s</td>" % data['summary'].encode("utf-8"));
	    file_output.write("</tr>");	    

	file_output.write("</table>");
	file_output.write("</body>");
	file_output.write("</html>");
