# Log_Analysis:
## project Overview:
  This is the first project for the Udacity Full Stack Nanodegree. In this project, a large database with over a million rows is explored by building complex SQL queries to draw business conclusions for the data, that could have come from a real-world web application, This reporting tool is a Python program using the psycopg2 module to connect to the database. This project sets up a mock PostgreSQL database for a fictional news website. The provided Python script uses the psycopg2 library to query the database and produce a report that answers the following three questions:
 

### Required Tools:
1)python
2)vagrant
3)virtual box

### Running  process:
step1:To run the code user has to install virtual box in the system.User can download `Vagrant` and `VirtualBox` to install and configure Virtual Machine.

Step 2: Use *`vagrant up`* to bring the **virtual machine** online and **vagrant ssh** to **login**.

Step 3: Download the data and Unzip the file in order to extract `_newsdata.sql_`. This file should be inside the Vagrant folder.

Step 4:Dump the database by using the command:*psql -d news -f newsdata.sql*.

Step-5:Connect to the database by using the command: *psql  news*. And create the views given below qnd exit psql.

Step-6:Now execute the Python file - `python article_views.py`


### The following queries are given in the project:

1.What are the most popular three articles of all time?
2.Who are the most popular article authors of all time?
3.On which days did more than 1% of requests lead to errors?

### Create the following views for the above queries

#### article view:
create view article as select articles.title,count(*) as count from   log,articles where  articles.slug=substr(log.path,length('/article/')+1)group by articles.title order by count desc ;


#### author view:
create view author as select authors.name, count(*) as views from articles inner join authors on articles.author = authors.id inner join log on log.path like concat('%', articles.slug, '%') where log.status like '%200%' group by authors.name;


#### errors view:
create view errors as select date(time) as error_date,round(100.0*sum(case log.status when '404 NOT FOUND' then 1 else 0 end)/count(log.status), 2) as error from log group by error_date;

