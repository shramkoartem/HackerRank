set @c1:=0, @c2:=0, @c3:=0, @c4:=0;
select min(doctor), min(professor), min(singer), min(actor)
from(
    select  case when occupation = 'Doctor'      then (@c1:=@c1+1)
                 when occupation = 'Professor'   then (@c2:=@c2+1)
                 when occupation = 'Singer'      then (@c3:=@c3+1)
                 when occupation = 'Actor'       then (@c4:=@c4+1)
            end  as   RowNumber,
            case when occupation = 'Doctor'      then Name end as Doctor,
            case when occupation = 'Professor'   then Name end as Professor,
            case when occupation = 'Singer'      then Name end as Singer,
            case when occupation = 'Actor'       then Name end as Actor
    from occupations
    order by name) Temp
group by RowNumber;
