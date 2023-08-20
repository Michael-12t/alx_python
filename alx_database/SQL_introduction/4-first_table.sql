CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
mysql -hlocalhost -uroot -p hbtn_0c_0 < first_table.sql
cat 3-list_tables.sql | mysql -hlocalhost -uroot -p hbtn_0c_0