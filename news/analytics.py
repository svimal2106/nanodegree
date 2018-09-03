#!/usr/bin/env python
from flask import Flask, request, redirect, url_for
from newsdb import NewsQueryProcessor
from constants import *

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    """Main page of the analytics of news website"""
    news_query_processor = NewsQueryProcessor()
    html_content_list = []
    for query in QUERY_MAP.keys():
        query_results = news_query_processor.\
            get_query_results(QUERY_MAP[query])
        query_results_table = "".join("<tr><td>" + str(value1) +
                                      "</td><td>" + str(value2) +
                                      "</td></tr>" for
                                      (value1, value2) in query_results)

        if query == "topArticles":
            html_content = TABLE_TEMPLATE % ("Article Name",
                                             "Page View Count",
                                             query_results_table)
        elif query == "topAuthors":
            html_content = TABLE_TEMPLATE % ("Author Name",
                                             "Page View Count",
                                             query_results_table)
        else:
            html_content = TABLE_TEMPLATE % ("Date",
                                             "Request Error Percent",
                                             query_results_table)

        html_content_list.append(html_content)

    analytics_section_html = NEWS_ANALYTICS_SECTION % (html_content_list[0],
                                                       html_content_list[1],
                                                       html_content_list[2])
    html = HTML_WRAP % analytics_section_html
    return html


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
