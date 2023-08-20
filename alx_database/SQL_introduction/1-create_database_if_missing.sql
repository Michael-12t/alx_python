CREATE DATABASE IF NOT EXISTS hbtn_0c_0;
mysql -hlocalhost -uroot -p < create_database_if_missing.sql
cat 0-list_databases.sql | mysql -hlocalhost -uroot -p