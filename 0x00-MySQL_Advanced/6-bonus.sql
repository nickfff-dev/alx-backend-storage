-- This script creates a stored procedure named 'AddBonus' for adding a new correction for a student.
-- The procedure takes three inputs: user_id, project_name, and score.
-- It checks if the specified project exists in the 'projects' table. If not, it creates a new project.
-- Then, it adds a new correction for the specified user and project with the given score.
-- This script demonstrates the use of conditional logic and dynamic SQL within stored procedures.

DELIMITER //

CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
    -- Check if the project exists in the 'projects' table
    IF NOT EXISTS (SELECT 1 FROM projects WHERE name = project_name) THEN
        -- If the project does not exist, create it
        INSERT INTO projects (name) VALUES (project_name);
    END IF;

    -- Retrieve the project ID
    SET @project_id = (SELECT id FROM projects WHERE name = project_name);

    -- Add the correction to the 'corrections' table
    INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, @project_id, score);
END; //

DELIMITER ;
