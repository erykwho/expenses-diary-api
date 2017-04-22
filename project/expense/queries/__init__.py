COUNT_EXPENSES = """
SELECT
  COUNT(*)
FROM
  "expense"
WHERE
  is_active IS true;
"""

SELECT_EXPENSES = """
SELECT
    user_id,
    payment_origin_id,
    category_id,
    reference_date,
    description,
    amount,
    regreted,
    comments
FROM
    "expense"
WHERE 
  user_id = %s
  AND is_active IS true;
"""

SELECT_EXPENSE = """
SELECT
    user_id,
    payment_origin_id,
    category_id,
    reference_date,
    description,
    amount,
    regreted,
    comments
FROM
  "expense"
WHERE
  id = %s
  AND is_active IS true;
"""


INSERT_EXPENSE = """
INSERT INTO "expense" (
    first_name,
    last_name,
    email,
    password
) VALUES
  (%(first_name)s, %(last_name)s, %(email)s, %(password)s);
"""


UPDATE_EXPENSE = """
UPDATE "expense"
    SET (%s) = (%s)
WHERE
    id = (%s);
"""


DELETE_EXPENSE = """
UPDATE "expense"
    SET is_active = false
WHERE
    id = (%s);
"""