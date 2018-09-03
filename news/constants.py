#!/usr/bin/env python

# HTML template for the news analytic web page
HTML_WRAP = '''\
<!DOCTYPE html>
<html>
  <head>
    <title>News Website Analytics</title>
    <style>
      h1 { text-align: center; }
      div.top_articles, div.top_authors, div.error_days
                { border: 1px solid #999;
                 padding: 10px 10px;
                 margin: 10px 20%%; }
      table, th, td {
            border: 1px solid black;
            text-alight: left;
        }
    </style>
  </head>
  <body>
    <h1>News Website Stats</h1>
    %s
  </body>
</html>
'''

# HTML template to construct a table
TABLE_TEMPLATE = '''\
            <table>
                <tr>
                    <th>%s</th>
                    <th>%s</th>
                </tr>
                %s
            </table>
'''

# HTML template to display analytics from news database
NEWS_ANALYTICS_SECTION = '''\
    <div class=top_articles><h2>Top Articles</h2>%s</div>
    <div class=top_authors><h2>Top Authors</h2>%s</div>
    <div class=error_days><h2>Days with High Error rate in request</h2>%s</div>
'''

QUERY_MAP = {
    "topArticles": """select title, count(*) as page_view_count from
                   page_views_with_author_and_article_details group by
                   title order by page_view_count desc limit 3;""",

    "topAuthors": """select author_name, count(*) as page_view_count from
                  page_views_with_author_and_article_details
                  group by author_name order by page_view_count desc;""",

    "errorDays": """select date, fail_percentage from (select
                 ((failed_requests * 100) / total_requests) as
                 fail_percentage, b.date from total_requests_by_date a,
                 failed_requests_by_date b
                 where a.date = b.date) t where fail_percentage > 1;"""
}
