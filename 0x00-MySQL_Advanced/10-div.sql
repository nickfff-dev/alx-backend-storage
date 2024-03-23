-- Creates a function 'SafeDiv' that safely divides two numbers, returning 0 if the divisor is 0.

DELIMITER //

CREATE FUNCTION SafeDiv(a INT, b INT) RETURNS DECIMAL(10, 6)
BEGIN
    IF b = 0 THEN
        RETURN 0;
    ELSE
        RETURN a / b;
    END IF;
END; //

DELIMITER ;
