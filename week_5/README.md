<h1> Week_5 </h1>


insert into website.member (name ,username ,password ,follower_count) values ("name_1" ,"test" ,"test" ,11) ;  
  
insert into website.member (name ,username ,password ,follower_count) values ("name_2" ,"test2" ,"test2" ,12) ;  
  
insert into website.member (name ,username ,password ,follower_count) values ("name_3" ,"test3" ,"test3" ,13) ;  
  
insert into website.member (name ,username ,password ,follower_count) values ("name_4" ,"test4" ,"test4" ,14) ;  
  
insert into website.member (name ,username ,password ,follower_count) values ("name_5" ,"test5" ,"test5" ,15) ;  
  
**在資料庫中填入五筆資料(包括要求一測資)  **

select * from website.member ;  
select * from website.member order by time desc;  

*匯出所有資料與按照時間排列:  *

![image](https://nash15963.github.io/wehelp-assignments/week_5/img/img_2.png)

使用 SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序。
此處使用limit的方式列出排序後的2~4筆資料。

使用 SELECT 指令取得欄位 username 是 test 的會員資料。
此處用where來選取特定範圍資料

![image](https://nash15963.github.io/wehelp-assignments/week_5/img/img_4.png)


使用 SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。
此處使用and增加搜尋範圍

![image](https://nash15963.github.io/wehelp-assignments/week_5/img/img_5.png)


使用 UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2。

![image](https://nash15963.github.io/wehelp-assignments/week_5/img/img_6.png)


取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。
取得 member 資料表中，所有會員 follower_count 欄位的總和。
取得 member 資料表中，所有會員 follower_count 欄位的平均數。
三個條件需要達成:

![image](https://nash15963.github.io/wehelp-assignments/week_5/img/img_7.png)

新增message資料表，並增加資料測試

![image](https://nash15963.github.io/wehelp-assignments/week_5/img/img_8.png)


使用 SELECT 搭配 JOIN 語法，取得所有留言，結果須包含留言者會員的姓名。
使用 SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有
留言，資料中須包含留言者會員的姓名。

![image](https://nash15963.github.io/wehelp-assignments/week_5/img/img_9.png)






