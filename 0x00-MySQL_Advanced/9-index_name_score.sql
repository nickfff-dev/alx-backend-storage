-- Creates an index 'idx_name_first_score' on 'names' table for efficient queries filtering by the first letter of 'name' and 'score'.
CREATE INDEX idx_name_first_score ON names (name(1), score);
