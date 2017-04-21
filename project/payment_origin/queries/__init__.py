COUNT_PAYMENT_ORIGINS = """
SELECT
  COUNT(*)
FROM
  "payment_origin"
WHERE
  user_id = 1
  AND is_active IS true;
"""

SELECT_PAYMENT_ORIGINS = """
SELECT
  name,
  description,
  abbreviation
FROM
  "payment_origin"
WHERE
  user_id = 1
  AND is_active IS true;
"""