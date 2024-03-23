-- This script creates an index named 'idx_name_first' on the 'names' table.
-- The index is created on the first letter of the 'name' column, which allows for efficient queries that filter by the first letter of names.
-- This is a demonstration of how to create an index on an expression, specifically extracting the first letter of a column.
CREATE INDEX idx_name_first ON names (LEFT(name, 1));
