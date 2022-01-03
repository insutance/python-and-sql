with heavy_user as(
    select host_id
    from places
    group by host_id
    having count(host_id) > 1
)
select *
from places
where host_id in (select host_id from heavy_user)
order by id;
