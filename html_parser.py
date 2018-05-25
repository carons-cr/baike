#!/usr/lib/env/python2.7
#encoding=utf-8
#pathName : html_parser

from bs4 import BeautifulSoup
import re;
import urlparse;

class HtmlParser(object):
    def _get_new_urls(self, page_url, beautiful_soup):
	new_urls = set();
	links = beautiful_soup.find_all("a", href=re.compile(r"/item/"));
	for link in links:
	    new_url = link["href"];
	    new_full_url = urlparse.urljoin(page_url, new_url);
	    new_urls.add(new_full_url);
	return new_urls;

    def _get_new_data(self, page_url, beautiful_soup):
	new_data = {};

	new_data["url"] = page_url;

	title_node = beautiful_soup.find("dd", class_="lemmaWgt-lemmaTitle-title").find("h1");
	new_data["title"] = title_node.get_text();

	summary_node = beautiful_soup.find("div", class_="lemma-summary");
	new_data["summary"] = summary_node.get_text();

	return new_data;

    def parse(self, page_url, html_content):
        if page_url is None or html_content is None:
            return
        beautiful_soup = BeautifulSoup(html_content, "html.parser", from_encoding="utf-8");
        new_urls = self._get_new_urls(page_url, beautiful_soup);
        new_data = self._get_new_data(page_url, beautiful_soup);
        return new_urls, new_data;


