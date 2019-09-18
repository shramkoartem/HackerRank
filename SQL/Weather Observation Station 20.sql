# Problem URL:    https://www.hackerrank.com/challenges/weather-observation-station-20/

#MySQL

SET @row_id := -1;
SELECT ROUND(AVG(sub.LAT_N), 4) FROM
(
SELECT @row_id := @row_id+1 AS row_id, 
       s.LAT_N FROM STATION AS s ORDER BY s.LAT_N
) AS sub 
WHERE sub.row_id IN (FLOOR(@row_id / 2), CEIL(@row_id / 2));
