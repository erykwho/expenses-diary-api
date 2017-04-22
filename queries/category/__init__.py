COUNT_CATEGORIES = """
SELECT
  COUNT(*)
FROM
  "category"
WHERE
  user_id = %s
  AND is_active IS true;
"""

SELECT_CATEGORIES = """
SELECT
    id,
    name,
    description
FROM
    "category"
WHERE 
  user_id = %s
  AND is_active IS true;
"""

SELECT_CATEGORY = """
SELECT
    id,
    name,
    description
FROM
  "category"
WHERE
  id = %s
  AND is_active IS true;
"""


INSERT_CATEGORY = """
INSERT INTO "category" (
    user_id,
    name,
    description
) VALUES
  (%(user_id)s, %(name)s, %(description)s);
"""


UPDATE_CATEGORY = """
UPDATE "category"
    SET (%s) = (%s)
WHERE
    id = (%s);
"""


DELETE_CATEGORY = """
UPDATE "category"
    SET is_active = false
WHERE
    id = (%s);
"""