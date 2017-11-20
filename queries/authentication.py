SELECT_USER_ID = """
SELECT 
  "id"
FROM
  "user"
WHERE
  "email" = %(email)s;
"""

SELECT_USER_PASSWORD = """
SELECT 
  "password"
FROM
  "user"
WHERE
  "email" = %(email)s;
"""
