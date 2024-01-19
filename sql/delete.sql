use ai__arun;


delimiter %%
drop procedure if exists deletealltable;%%
create procedure deletealltable
(in tablename varchar(30),
 in conditioncolumnname varchar(98),
 in conditioncolumnvalue int )
 begin
 
 
 set @statement =concat("delete from ",tablename,"  where ",conditioncolumnname,"=",conditioncolumnvalue);
 prepare stmts from @statement;
 execute stmts;
 end %% 
 delimiter ;  
  
   call deletealltable('fk_usr_reg','user_id',2);
   select*from fk_usr_reg;

delimiter **

 create procedure altertable(
  in tablename varchar (30),
in  columnname varchar (50))
 begin
 
 set @statement=concat("alter table ",tablename,"add column"columnnmae "varchar (50)");
 prepare stmts from @statement;
 execute stmts;
 end **
 delimiter ;
 
 