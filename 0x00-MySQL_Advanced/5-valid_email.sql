-- This script creates a trigger named 'reset_valid_email_on_email_change' for the 'users' table.
-- The trigger is designed to reset the 'valid_email' attribute to 0 (false) whenever the 'email' attribute of a user is updated.
-- This ensures that the email validation status is reset whenever the email address changes, allowing for re-validation.
-- The script uses the 'BEFORE UPDATE' trigger event and compares the new and old email values to determine if the email has been changed.
-- If the email is changed, the 'valid_email' attribute is set to 0.

DELIMITER //

CREATE TRIGGER reset_valid_email_on_email_change
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email <> OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END; //

DELIMITER ;
