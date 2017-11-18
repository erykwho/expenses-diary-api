COUNT_USERS = """
SELECT
  COUNT(*)
FROM
  "user"
WHERE
  is_active IS true;
"""

SELECT_USERS = """
SELECT
  id,
  first_name,
  last_name,
  email
FROM
  "user"
WHERE
  is_active IS true;
"""

SELECT_USER = """
SELECT
  id,
  first_name,
  last_name,
  email
FROM
  "user"
WHERE
  id = %s
  AND is_active IS true;
"""


INSERT_USER = """
INSERT INTO "user" (
    first_name,
    last_name,
    email,
    password
) VALUES
  (%(first_name)s, %(last_name)s, %(email)s, %(password)s)
RETURNING id;
"""


UPDATE_USER = """
UPDATE "user"
    SET (%s) = (%s)
WHERE
    id = (%s);
"""


DELETE_USER = """
UPDATE "user"
    SET is_active = false
WHERE
    id = (%s);
"""