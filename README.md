INDEXING
SQL queries achieve efficiency by generating a smaller table called an index from a specified column or a set of specified columns. These columns are called keys and they can be used to uniquely identify the row in the table. An index is a data structure that the database uses to find records more easily. Indexes are built on one or more columns of a table. Each index maintains a list of values within a field that are sorted in ascending or descending order. Rather than sorting the records on the field or fields during query execution, the system can access the rows in the order of the index.

When to use Indexes
Indexes are applicable when you have extensive data that you need to run queries on. With indexes, the database uses the generated index table to look up rows as opposed to introspecting each row which affects the response time.

Commonly the columns that are subject of the WHERE clauses in your commonly executed queries should be indexed.

Setting the unique constraint on an Index restricts duplicate values from appearing in the indexed columns. It is worth noting that setting a unique constraint on an index increases the write speed. This increase is because, on insertion, every row has to be checked to ensure the incoming row is unique. When you create an index from a primary key, you ensure no duplicate or null value is possible in the index. This results in a performance boost when running the InnoDB storage engine. This boost in performance is based on how InnoDB storage engines physically store data by placing null-valued rows in the key out of a contiguous sequence with rows that have values. By using the pk to generate an index we add a nonnull constraint to this column, no null values are possible and the data is stored in a contiguous sequence for faster responses.



SQL default settings allow up to 16 indexes per table. They can be added to table creation or added to an already existing table.

An index works like a B-tree which is always sorted, it enables the database to find the midpoint from which to start the search as opposed to checking every element starting from the first. 

MYSQL uses indexes for the following:
 to find rows matching a where clause easily
to eliminate rows from consideration. if there's a choice between multiple indexes, SQL chooses the one with the least rows
If the index has multiple columns the optimizer can search for a row using the first column in the index, ie. the leftmost column. if you have a multi-column index (col1, col2, col3) you have enabled search capabilities on (col1), (col1, col2), (col1, col2, col3).
to retrieve rows from other tables during a join operation.
 to find min and max values on a key_col
to sort a table




STORED PROCEDURES
MYSQL 5 introduced routines. There are two kinds of routines:

Stored procedures that you invoke by calling.
Functions that return values.
The main difference is User-Defined-Functions can be used like any other SQL expression within SQL statements but procedures have to be called. A stored procedure is a subroutine stored in a database. A procedure has a name, parameter list, and SQL statements.



Why stored procedures
Store procedures are fast. The MySQL server caches them just like prepared statements. If you have a procedure that requires checking looping, multiple statements and no user interaction a stored procedure is more applicable here.
They are portable.  A procedure stored in SQL can be run on any SQL server without installing additional runtime resources.
They are stored as source code in the database itself, which is a good OOP practice to bundle data with the methods that operate on that data.
Stored procedure syntax


CREATE [DEFINER = { user | CURRENT_USER }]          
PROCEDURE sp_name ([proc_parameter[,...]])          
[characteristic ...] routine_body    
proc_parameter: [ IN | OUT | INOUT ] param_name type    
type:          
Any valid MySQL data type    
characteristic:          
COMMENT 'string'     
| LANGUAGE SQL      
| [NOT] DETERMINISTIC      
| { CONTAINS SQL | NO SQL | READS SQL DATA | MODIFIES SQL DATA }      
| SQL SECURITY { DEFINER | INVOKER }    
routine_body:      
Valid SQL routine statement








CREATE          
[DEFINER = { user | CURRENT_USER }]          
PROCEDURE sp_name ([proc_parameter[,...]])          
[characteristic ...] routine_body    
proc_parameter: [ IN | OUT | INOUT ] param_name type 
The create statement can be in various forms including:



CREATE PROCEDURE sp_name() /* to create a procedure with no parameters*/




CREATE PROCEDURE sp_name([IN] parameter_name parameter_type) 
/* an IN parameter passes a value into the procedure */




CREATE PROCEDURE sp_name([OUT] parameter_name paramater_type)
/* an OUT parameter passes values from the procedure to the caller */




CREATE PROCEDURE sp_name([INOUT] parameter_name parameter_type)
/* an INOUT parameter is initialized by the caller and can be modified by the procedure with
its value visible to the caller when the call returns */


In a stored procedure every parameter is an IN parameter by default. You can specify otherwise using INOUT or OUT



The create procedure command creates a new stored procedure specified by the name sp_name using the optional parameters passed in the parenthesis.





characteristic:          
COMMENT 'string'     
| LANGUAGE SQL      
| [NOT] DETERMINISTIC      
| { CONTAINS SQL | NO SQL | READS SQL DATA | MODIFIES SQL DATA }      
| SQL SECURITY { DEFINER | INVOKER }


The characteristic clause comes after the parameters parenthesis but before the body and this clause is optional.

COMMENT 'string' 


The COMMENT characteristic is a MySQL extension used to describe the stored routine and the information is displayed by SHOW CREATE PROCEDURE statements.



| LANGUAGE SQL     


The LANGUAGE characteristic shows the body of the procedure was written in SQL.


| [NOT] DETERMINISTIC   


The  NOT DETERMINISTIC characteristic is informational. A deterministic routine produces the same result for the same input parameters, while a none deterministic procedure gives different results for the same parameters




| { CONTAINS SQL | NO SQL | READS SQL DATA | MODIFIES SQL DATA }  


CONTAINS  SQL means there are no read-write statements in the procedure body. This refers to statements that execute without data being read or written to the db.

NO SQL means the routine has no SQL statements

READS SQL DATA means the routine defines read operations in the body but no write operations.

MODIFIES SQL DATA means the routine defines write operations on the db but no read operations.





| SQL SECURITY { DEFINER | INVOKER }
 

the SQL SECURITY characteristic specifies the security context and can be either SQL SECURITY DEFINER OR SQL SECURITY INVOKER. This means whether the routine is run with the privileges of the account named in the routine DEFINER clause or the user who invoked it. The account must have the privileges to access the db where the routine is stored. the default value is DEFINER, the user who invokes the routine must have EXECUTE privileges on the procedure.





Compound-Statement
This is a statement that contains other statements. Mysql defines various compound statement patterns:

BEGIN END block.
Statement label.
DECLARE
Variables stored in programs
Flow control Statements




BEGIN END block syntax



Used when you need more than one statement in a procedure.



[begin_label:]

BEGIN

[statement_list]

END

[end_label]
statement_list represents one or more statements separated by a semi-colon. The statement list is optional meaning an empty BEGIN END block is valid.

Label statement
labels are permitted for BEGIN...END blocks and LOOP, REPEAT, AND WHILE STATEMENTS.

the syntax is like:



[begin_label:]

[statements_list]

[end_label]

[begin_label:]

LOOP

statement_list

END LOOP

[end_label]

[begin_label:]

REPEAT

statement_list

UNTIL condition

END REPEAT

[end_label]

[begin_label:]

WHILE condition

DO

statement_list

END WHILE

[end_label]


The begin label must end with a full colon. When a begin label exists an end label can be omitted. If the end_label exists it has to match the begin label. an end label cannot exist without a begin label. labels at the same nesting level should have unique names and they can be up to 16 chars long max.





DECLARE

This is used to define various items that are local to a routine. They could be local variables, conditions, handlers, and cursors. It is used only inside the BEGIN...END compound statement and must be at its start before any other statement declaration. Declarations follow the following order:

cursor declaration must appear before handler declarations
variable and condition declarations must appear before cursor declarations




Variables Stored in a Program

This could be system or user-defined variables. Declare a variable.



DECLARE var_name [, var_name] ... type [DEFAULT value]






to use a default value for a variable use DEFAULT, without DEFAULT the value is initially null. local variables are declared within stored procedures and are valid within the BEGIN...END block they are declared and they can have any SQL data type.



example of the use of local variables in a compound statement.

DELIMITER $$
CREATE PROCEDURE my_procedure_Local_Variables()
BEGIN   /* declare local variables */   
DECLARE a INT DEFAULT 10;   
DECLARE b, c INT;    /* using the local variables */   
SET a = a + 100;   
SET b = 2;   
SET c = a + b;    
BEGIN      /* local variable in nested block */      
DECLARE c INT;             
SET c = 5;       
/* local variable c takes precedence over the one of the          
same name declared in the enclosing block. */       
SELECT a, b, c;   
END;    
SELECT a, b, c;
END$$


in stored procedures, user variables are referenced with an ampersand, prefixed to the user variable identifier

MySQL: If Statement
if statement implements a basic conditional construct in stored programs and must be terminated by a semicolon

Basic Syntax



IF condition THEN statement(s) 

[ELSEIF condition THEN statement(s)]

[ELSE statement(s)]

END IF


If the first condition is true then the corresponding THEN or ELSEIF statements execute, if it's false the ELSE statements execute. empty statements are not allowed.

example

CREATE DEFINER=`root`@`127.0.0.1` 
PROCEDURE `GetUserName`(INOUT user_name varchar(16),
IN user_id varchar(16))
BEGIN
DECLARE uname varchar(16);
SELECT name INTO uname
FROM user
WHERE userid = user_id;
IF user_id = "scott123" 
THEN
SET user_name = "Scott";
ELSEIF user_id = "ferp6734" 
THEN
SET user_name = "Palash";
ELSEIF user_id = "diana094" 
THEN
SET user_name = "Diana";
END IF;
END
MySQL: Case Statement
Used to create complex conditional constructs inside a stored procedure.

Basic Syntax



CASE case_value    
WHEN when_value THEN statement_list         
[WHEN when_value THEN statement_list] ...         
[ELSE statement_list] END CASE


The case_value is an expression whose value is compared to the when_value expression in each WHEN clause until one of them is equal.

When an equal when_value is found, the corresponding THEN clause statement_list is executed. If no when_clause matches, the THEN clause statements from the ELSE clause execute.

or

​

CASE        
WHEN search_condition THEN statement_list   
[WHEN search_condition THEN statement_list] ...        
[ELSE statement_list] END CASE


each search_condition  is evaluated until one is true then the corresponding THEN clause statements execute.



MySQL: ITERATE Statement
This means starting the loop again. It is only used within LOOP, WHILE, and REPEAT statements.

ITERATE label


MySQL: LEAVE Statement
Used to exit the flow control construct that has the given label. if the label is for the outermost program block, the program exits.

It can be used within BEGIN...END statements and LOOP constructs (LOOP, REPEAT, WHILE)



LEAVE label
​

​MySQL: LOOP Statement
Used to create repeated execution of SQL statement list

Basic Syntax

[begin_label:] 
LOOP       
statement_list  
END LOOP 
[end_label]


A LEAVE statement can be used to exit a loop. Within a stored function a Return can be used to exit the program entirely





MySQL: REPEAT Statement
Used to execute statements repeatedly as long as the condition is true. The condition is checked whenever a statement finishes executing.

Basic Syntax

[begin_label:] 
REPEAT     
statement_list 
UNTIL search_condition 
END 
REPEAT 
[end_label]


MySQL: RETURN Statement
Terminates execution of a stored procedure and returns the value exprs to the caller. There must be at least one return statement in a stored function. They are not used with stored procedures. The LEAVE statement is used instead.



MySQL: WHILE Statement
Used to run statements as long as the condition is true. The condition is checked every time at the beginning of the loop.

[begin_label:] WHILE search_condition DO
    statement_list
END WHILE [end_label]




MySQL: ALTER PROCEDURE
Used to alter the characteristics of a stored procedure. More than one change may be specified. YOu are not able to change the parameters or the body, this is done by dropping the stored procedure and creating it again.

ALTER PROCEDURE proc_name [characteristic ...]characteristic:    
COMMENT 'string'  
| LANGUAGE SQL  
| { CONTAINS SQL 
| NO SQL | READS SQL DATA 
| MODIFIES SQL DATA }  
| SQL SECURITY { DEFINER 
| INVOKER }
​The caller must have ALTER ROUTINE privileges on the stored program



MySQL: DROP PROCEDURE
Used to drop a stored function or procedure.

DROP {PROCEDURE | FUNCTION} [IF EXISTS] sp_name


MySQL: Cursors
This is a control structure that allows traversal over the records of a database. Cursors are used by db developers to process results from queries row by row. It allows for the manipulation of a whole result set at once.

In stored procedures, cursors allow for the definition of a result set and perform complex logic on the result set row by row. A stored program can also return a result set back to the caller.



Properties of Cursors

Asensitive - the server might or might not make a copy of the result table.
ReadOnly - not updatable.
Nonscrollable: can be traversed in one direction only and cannot skip rows.


To use cursors in MySQL procedures, you need to do the following :

Declare a cursor. This involves declaring a cursor and associating it with a SELECT statement that will retrieve the rows for the cursor:



DECLARE cursor_name
CURSOR FOR select_statement


Open a cursor.  The following statement opens a previously declared cursor :



OPEN cursor_name


Fetch Data into variables. The statement fetches the next row for the SELECT statement associated with the specified cursor and advances the cursor pointer. if a row exists, the fetched columns are stored in named variables. The number of columns in the result set must match the number of output variables specified in the fetch statement



FETCH [[NEXT] FROM] cursor_name 

INTO var_name [, var_name] ...


Close the cursor when done

CLOSE cursor_name


Example



CREATE PROCEDURE order_cursors(INOUT return_val VARCHAR(191))

    BEGIN

    DECLARE a VARCHAR(191);

    DECLARE b INT;

    DECLARE cur_order CURSOR FOR  SELECT name FROM OrderType; // must come after variables

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET b = 1; // must come after cursor declaration

    OPEN cur_order; // must open to fetch and close

    REPEAT FETCH cur_order INTO a;

    UNTIL b = 1 END REPEAT;

    close cur_order;

    SET return_val = a;

    END;

    $$










MySQL Triggers
This is a set of operations that are run automatically when a specified data manipulation operation (insert update or delete) is performed on a table. 

Triggers are useful for:
enforcing business rules.
validating input.
keeping an audit trail. 
generate data for a computed field.
 access system functions.
replicate data


Benefits of Triggers
Faster Application  Development  - The triggers are stored in the db hence no need to copy to each application db.
Global enforcement of Business Rules - Define a trigger once then reuse it for every application that uses the database.
Easier maintenance. - If the business logic changes then you only need to change the program trigger but not each application trigger.
Improves performance in the client/server environment since all rules are run on the server before the result returns.






MySQL Views
