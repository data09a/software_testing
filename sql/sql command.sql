-- 1. look up the last row from az_users
select * from az_users 
order by user_id 
desc limit 1;


-- 2. change the nickname in form az_user 
update az_users 
set nickname = 'Jack' 
where nickname = '123123';

-- 3. look up the first 10 products information by lowest price(id, product name, price, stock quantity) 
select product_id, product_name, product_count, market_price 
from az_products 
order by market_price 
asc limit 10;


-- 4. change the product price for all products who’s nickname starts with ABA
update az_products
set market_price = '100'
where nickname like 'ABA%';

-- 5. look up phone number '1231231234' for its nickname and order number
select user.nickname, order.order_number 
from az_users user inner join az_orders order 
on  user.user_id = order.user_id 
where user.mobile = '1231231234';

