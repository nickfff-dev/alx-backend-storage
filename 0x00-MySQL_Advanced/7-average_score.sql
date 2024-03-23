-- This script creates a stored procedure named 'ComputeAverageScoreForUser' for computing and storing the average score for a student.
-- The procedure takes one input: user_id, which is assumed to be linked to an existing user in the 'users' table.
-- It calculates the average score for all corrections associated with the given user and updates the 'average_score' column in the 'users' table.
-- This script demonstrates the use of aggregate functions and dynamic SQL within stored procedures.

DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    -- Compute the average score for the specified user by averaging the scores from the 'corrections' table
    UPDATE users
    SET average_score = (
        SELECT AVG(score)
        FROM corrections
        WHERE corrections.user_id = user_id
    )
    WHERE id = user_id;
END; //

DELIMITER ;
