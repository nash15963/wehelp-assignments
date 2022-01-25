create database `website`;
create table website.member(id  BIGINT  AUTO_INCREMENT PRIMARY KEY,  
			    name VARCHAR(255) NOT NULL ,
			    username VARCHAR(255) NOT NULL,
			    password VARCHAR(255) NOT NULL ,
			    follower_count INT NOT NULL ,
			    time DATETIME NOT NULL DEFAULT NOW());

insert into website.member (name ,username ,password ,follower_count) values ("name_1" ,"test" ,"test" ,11) ;
insert into website.member (name ,username ,password ,follower_count) values ("name_2" ,"test2" ,"test2" ,12) ;
insert into website.member (name ,username ,password ,follower_count) values ("name_3" ,"test3" ,"test3" ,13) ;
insert into website.member (name ,username ,password ,follower_count) values ("name_4" ,"test4" ,"test4" ,14) ;
insert into website.member (name ,username ,password ,follower_count) values ("name_5" ,"test5" ,"test5" ,15) ;

select * from website.member ;
select * from website.member order by time desc;
select * from website.member order by time desc limit 1,3;
select * from website.member where username = "test";
select * from website.member where username = "test" and password ="test";


SET SQL_SAFE_UPDATES=0;
update website.member set name = "test2" where username = "test" ;
SET SQL_SAFE_UPDATES=1;

select count(*) from website.member ;
select sum(follower_count) from website.member ;
select avg(follower_count) from website.member ;



create table website.message(id  BIGINT  AUTO_INCREMENT PRIMARY KEY,  
			     member_id BIGINT NOT NULL ,
			     content VARCHAR(255) NOT NULL,
			     time DATETIME NOT NULL DEFAULT NOW() ,
                             FOREIGN KEY(member_id) REFERENCES member(id)) ;

SELECT * FROM website.message ;
insert into website.message (member_id,content) values ("1",'Today is Good Day') ;
insert into website.message (member_id,content) values ("2",'Today is not a Good Day') ;
insert into website.message (member_id,content) values ("3",'Today seems like a Good Day') ;
insert into website.message (member_id,content) values ("4",'Today is a Good Day') ;

select a.name ,a.id ,b.content from website.member as a inner join website.message as b on a.id = b.member_id ;
select a.name ,a.id ,b.content from website.member as a inner join website.message as b on a.id = b.member_id where a.username = "test";


