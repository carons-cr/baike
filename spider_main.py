#!/usr/lib/env/python2.7
#coding=utf-8
#fileName : spider_main.py

import url_manager, html_downloader, html_parser, html_outputer;

class SpiderMain(object):
    def __init__(self):
	self.urlmanager =url_manager.UrlManager();
	self.downloader = html_downloader.HtmlDownloader();
	self.parser = html_parser.HtmlParser();
	self.outputer = html_outputer.HtmlOutputer();

    def craw(self, root_url):
	count = 1;
	self.urlmanager.add_new_url(root_url);
	while self.urlmanager.has_new_url():
	    try:
  	        new_url = self.urlmanager.get_new_url();
		print "craw %d : %s" % (count, new_url);
	        html_content = self.downloader.download(new_url);
	        new_urls, new_data = self.parser.parse(new_url, html_content);
	        self.urlmanager.add_new_urls(new_urls);
	        self.outputer.collect_data(new_data);

		if count == 100:
                    break;
                count = count + 1;
	    except:
		print "craw failed";

	self.outputer.output_html();

if __name__ == "__main__":
    root_url = "https://baike.baidu.com/item/Python";
    spider = SpiderMain();
    spider.craw(root_url);

