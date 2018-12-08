"""
See venmo withdrawals and deposits

"""

import psycopg2 as pg2

con = pg2.connect(database='venmo', user='isdb')
con.autocommit = True
cur = con.cursor()


print('Story 2: see all venmo withdrawals and transfers')
query = '''
SELECT abs(amount),
       CASE
         WHEN amount > 0 THEN 1
         ELSE 0 END AS is_deposit,
       CASE
         WHEN amount <= 0 THEN 1
         ELSE 0 END AS is_withdrawal
  FROM Transfers;
'''
cur.execute(query)
rows = cur.fetchall()
if rows:
    for row in rows:
        print(row)
else:
    print('No transfers found')