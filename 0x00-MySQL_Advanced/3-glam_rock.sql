-- statement to order bands by lifespan
SELECT band_name, (IFNULL(split, 2020) - formed) AS lifespan FROM metal_bands WHERE FIND_IN_SET("Glam rock", style) > 0 ORDER BY lifespan DESC;
