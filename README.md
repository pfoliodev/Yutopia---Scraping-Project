[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/benwNeJX)

## Scraping project

This is a study project for Yutopia School. We were asked to scrape a website and then save the scraped data in a database. After that we had to set up a Rest API as well as a front end to display the data.

## Install Python & Mysql
We need python to scrap webpage and Mysql to store the data in it
Do not forget to add path environment variable
You can lauch the python script "scrap_books.py" to begin the scraping.

## Requests & Beautifulsoup
More easy for scraping
Documentation
https://www.crummy.com/software/BeautifulSoup/bs4/doc/

## Install PHP & Symfony for the back end
Link to install PHP
https://windows.php.net/download/
Do not forget to add path in environment variable.

In order to enable functionnality in symfony, you need to change the php.ini file.

extension=php_curl.dll
extension=php_fileinfo.dll
extension=php_gd2.dll
extension=php_mbstring.dll
extension=php_mysqli.dll
extension=php_pdo_mysql.dll
extension=php_openssl.dll

These extension are commented by default, you can enable by decommenting each line.

PHP have now an internal server that you can launch 
php -S localhost:8000 -t public

## Install Composer the dependency manager for PHP
In order to create project with Symfony we need to install composer.
Link to install composer.
https://getcomposer.org/download/