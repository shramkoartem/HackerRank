select sum(city.population) 
from city inner join country on  CITY.CountryCode = COUNTRY.Code
where continent = 'Asia';
