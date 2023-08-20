DROP DATABASE IF EXISTS hbtn_0c_0;
mysql -hlocalhost -uroot -p < remove_database.sql
cat 0-list_databases.sql | mysql -hlocalhost -uroot -p