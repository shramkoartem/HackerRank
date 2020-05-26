set @count := 0;

select repeat('* ', @count := @count +1)
from INFORMATION_SCHEMA.TABLES limit 20;
