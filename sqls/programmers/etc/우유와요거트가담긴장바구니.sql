-- 처음 작성한 쿼리
with milk_in_cart as (
    select cart_id, name
    from cart_products
    where name = "milk"
),
yogurt_in_cart as (
    select cart_id, name
    from cart_products
    where name = "yogurt"
)
select 
    distinct milk.cart_id
from 
    milk_in_cart as milk
join 
    yogurt_in_cart as yogurt
on 
    milk.cart_id = yogurt.cart_id
order by
    milk.cart_id;


-- 이해하기는 어렵겠지만 좀 더 간결한 쿼리
select
    cart_id
from
    cart_products
where
    name in ("milk", "yogurt")
group by
    cart_id
having
    count(distinct name) = 2;
