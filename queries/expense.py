COUNT_EXPENSES = """
SELECT
  COUNT(*)
FROM
  "expense"
WHERE
  user_id = %s
  AND is_active IS true;
"""

SELECT_EXPENSES = """
SELECT
    expense.id,
    expense.user_id,
    expense.payment_origin_id,
    row_to_json(payment_origin) AS payment_origin,
    row_to_json(category) AS category,
    expense.reference_date,
    expense.description,
    expense.amount,
    expense.regreted,
    expense.comments
FROM
  "expense"
  JOIN "payment_origin"
    ON payment_origin.id = expense.payment_origin_id 
  JOIN "category"
    ON category.id = expense.category_id
WHERE 
  expense.user_id = 1
  AND expense.is_active IS true
  AND payment_origin.is_active IS true
  AND category.is_active IS true
ORDER BY
    expense.id ASC;
"""

SELECT_EXPENSE = """
SELECT
    id,
    user_id,
    payment_origin_id,
    row_to_json(payment_origin) AS payment_origin,
    row_to_json(category) AS category,
    category_id,
    reference_date,
    description,
    amount,
    regreted,
    comments
FROM
  "expense"
  INNER JOIN "payment_origin"
    ON expense.payment_origin_id = payment_origin.id 
  JOIN "category"
    ON category.id = expense.category_id
WHERE
  id = %s
  AND expense.is_active IS true
  AND payment_origin.is_active IS true
  AND category.is_active IS true;
"""


INSERT_EXPENSE = """
INSERT INTO "expense" (
    user_id,
    payment_origin_id,
    category_id,
    reference_date,
    description,
    amount,
    regreted,
    comments
) VALUES
  (%(user_id)s, %(payment_origin_id)s, %(category_id)s, %(reference_date)s,
   %(description)s, %(amount)s, %(regreted)s, %(comments)s);
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