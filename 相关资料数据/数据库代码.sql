create database jdplus CHARACTER SET utf8;
use jdplus;


CREATE TABLE M1(
num int(10) AUTO_INCREMENT PRIMARY KEY NOT NULL,
act_date varchar(20),
pin varchar(20),
act_label int(10),
tried int(10),
is_1st int,
times int(10),
sku_no int(10),
stage int(5),
open_date varchar(225),
begin_date varchar(225),
end_real_date varchar(225)
)CHARACTER SET utf8;

load data infile "/var/lib/mysql-files/m1.csv"
into table M1 character set utf8
fields terminated by ',' optionally enclosed by '"' escaped by '"'
lines terminated by '\r\n';

CREATE TABLE M2(
num int(10) AUTO_INCREMENT PRIMARY KEY NOT NULL,
Date varchar(20),
pin varchar(20),
stage_label int(10),
act_date varchar(20),
max_end_date varchar(20),
max_end_to_now_day int(10),
tried int(10),
is_1st int(10),
times int(10),
stage int(5),
open_date varchar(225),
begin_date varchar(225),
end_real_date varchar(225),
v_end_date varchar(225)
)CHARACTER SET utf8;

load data infile "/var/lib/mysql-files/m2.csv"
into table M2 character set utf8
fields terminated by ',' optionally enclosed by '"' escaped by '"'
lines terminated by '\r\n';

CREATE TABLE M3(
num int(10) AUTO_INCREMENT PRIMARY KEY NOT NULL,
date varchar(20),
forming_cnt varchar(255),
add_1st_form_cnt varchar(255),
renew_form_cnt varchar(225),
end_form_cnt varchar(225),
end_loss_form_cnt varchar(225),
Loss_renew_form_cnt varchar(255)
)CHARACTER SET utf8;

load data infile "/var/lib/mysql-files/m3.csv"
into table M3 character set utf8
fields terminated by ',' optionally enclosed by '"' escaped by '"'
lines terminated by '\r\n';


CREATE TABLE plus_user(
id int(10) PRIMARY KEY NOT NULL,
sex varchar(20),
edu varchar(255),
city varchar(255),
age varchar(225),
ave_mon_con varchar(225)
)CHARACTER SET utf8;

load data infile "/var/lib/mysql-files/plus_user_sql.txt"
into table plus_user
fields terminated by ',' optionally enclosed by '"' escaped by '"'
lines terminated by '\r\n';