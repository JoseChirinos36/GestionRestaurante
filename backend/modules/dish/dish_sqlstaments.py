CREATE_DISH_ITEM = """
    INSERT INTO dishes(dish_id, name, price)
    VALUES(:dish_id, :name, :price)
    RETURNING dish_id, name;
"""

GET_DISHES_LIST = """
    SELECT dish_id, name, price FROM dishes;
"""

UPDATE_DISHES_BY_ID = """
UPDATE dishes
SET price = :price,
    name = :name
WHERE dish_id = :dish_id;

"""

GET_DISH_BY_ID = """
    SELECT * FROM dishes WHERE dish_id= :dish_id
"""