select city.name 
from city inner join country on CITY.CountryCode = COUNTRY.Code
where continent = 'Africa';
