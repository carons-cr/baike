#!/usr/lib/env/python2.7
#encoding=utf-8
#pathName : html_downloader.py

import urllib2;

class HtmlDownloader(object):
    def download(self, url):
	if url is None:
	    return None;
	response = urllib2.urlopen(url);
	if response.getcode() != 200:
	    return None;
	return response.read();