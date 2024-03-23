-- statement to rank band countries of origin by the number of fans
SELECT origin, SUM(fans) As nb_fans FROM metal_bands GROUP BY origin ORDER BY nb_fans DESC;
