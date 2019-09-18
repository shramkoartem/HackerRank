select if (s.Marks < 70, 'NULL', s.Name), g.Grade, s.Marks
from Students as s, Grades as g
where s.Marks between g.Min_Mark and g.Max_Mark
order by g.grade desc, s.Name;
