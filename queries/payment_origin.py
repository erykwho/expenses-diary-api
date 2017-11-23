COUNT_PAYMENT_ORIGINS = """
SELECT
  COUNT(*)
FROM
  "payment_origin"
WHERE
  user_id = %s
  AND is_active IS true;
"""

SELECT_PAYMENT_ORIGINS = """
SELECT
  id,
  name,
  description,
  abbreviation
FROM
  "payment_origin"
WHERE
  user_id = %s
  AND is_active IS true
ORDER BY
    id ASC;
"""

SELECT_PAYMENT_ORIGIN = """
SELECT
  id,
  name,
  description,
  abbreviation
FROM
  "payment_origin"
WHERE
  id = %s
  AND is_active IS true
ORDER BY
    id ASC;
"""

INSERT_PAYMENT_ORIGIN = """
INSERT INTO "payment_origin" (
    user_id,
    name, 
    description,
    abbreviation
) VALUES
  (%(user_id)s, %(name)s, %(description)s, %(abbreviation)s);
"""


UPDATE_PAYMENT_ORIGIN = """
UPDATE "payment_origin"
    SET (%s) = (%s)
WHERE
    id = (%s);
"""


DELETE_PAYMENT_ORIGIN = """
UPDATE "payment_origin"
    SET is_active = false
WHERE
    id = (%s);
"""