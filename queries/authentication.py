SELECT_USER_ID = """
SELECT 
  "id"
FROM
  "user"
WHERE
  "email" = %(email)s
  AND "password" = %(password)s;
"""