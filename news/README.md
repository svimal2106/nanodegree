News Analytics App
=============
This project contains the code to extract and serve analytics from the news database.
The project is a part of the Udacity Nanodegree Full Stack course.

To run the project, login to the Vagrant setup with news database
````
vagrant ssh
````

Log into the news database using the command

```
psql news
```

Please create the following views from psql prompt

* View on filtered GET requests to specific articles

```
create view article_views as select * from 
(select split_part(path, '/', 3) as articlename, 
time as request_time from log where method='GET') t 
where t.articlename != '';
```

* View on article and author information merged together
```
create view articles_with_author_details as 
select * from (select name as author_name, 
slug, title, time as article_creation_time 
from authors, articles where 
authors.id = articles.author) t;
```

* View on article and author details with page view count
```
create view page_views_with_author_and_article_details 
as select * from article_views a, 
articles_with_author_details b 
where a.articlename = b.slug;
```

* View on total HTTP requests by date
```
create view total_requests_by_date as select count(*) 
as total_requests, to_char(time, 'DD Mon YYYY') as date 
from log group by date;
```

* View on failed HTTP requests by date
```
create view failed_requests_by_date as select count(*) 
as failed_requests, to_char(time, 'DD Mon YYYY') as 
date from log where status != '200 OK' group by date;
```


Then start the Flask App to fetch and serve the analytics from news database
```
python analytics.py
```

After starting the app, please navigate to ``http://localhost:8000`` on the 
browser to get the results of queries as an HTML page