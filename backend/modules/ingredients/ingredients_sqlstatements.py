CREATE_INGREDIENT_ITEM = """
    INSERT INTO ingredients(ingredient_id, name, amount, unit)
    VALUES(:ingredient_id, :name, :amount, :unit)
    RETURNING ingredient_id, name;
"""

GET_INGREDIENTS_LIST = """
    SELECT ingredient_id, name, amount, unit FROM ingredients;
"""

UPDATE_INGREDIENT_BY_ID = """
UPDATE ingredients
SET amount = :amount,
    name = :name,
    unit = :unit
WHERE ingredient_id = :ingredient_id;

"""

GET_INGREDIENT_BY_ID = """
    SELECT * FROM ingredients WHERE ingredient_id= :ingredient_id
"""