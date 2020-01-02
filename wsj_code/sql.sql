create database project charset=utf8;
use project;
量词表
create table classifier(
id int primary key auto_increment,
name char(10) not null,
words char(10)
);

create table adjective(
id int primary key auto_increment,
name char(10) not null,
words char(10)
);
create table unusual_used(
id int primary key auto_increment,
name char(10) not null,
words char(10)
);