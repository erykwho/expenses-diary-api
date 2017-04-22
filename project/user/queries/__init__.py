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
  first_name,
  last_name,
  email
FROM
  "user"
WHERE
  is_active IS true;
"""
#
# SELECT_USER = """
# SELECT
#   name,
#   description,
#   abbreviation
# FROM
#   "user"
# WHERE
#   id = %s
#   AND is_active IS true;
# """
#
# INSERT_USER = """
# INSERT INTO "user" (
#     user_id,
#     name,
#     description,
#     abbreviation
# ) VALUES
#   (%(user_id)s, %(name)s, %(description)s, %(abbreviation)s);
# """
#
#
# UPDATE_USER = """
# UPDATE "user"
#     SET (%s) = (%s)
# WHERE
#     id = (%s);
# """
#
#
# DELETE_USER = """
# UPDATE "user"
#     SET is_active = false
# WHERE
#     id = (%s);
# """