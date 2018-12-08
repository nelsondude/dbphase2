import psycopg2 as pg2

# Connect to an existing database
con = pg2.connect(database='postgres', user='isdb')
con.autocommit = True
# Open a cursor to perform database operations
cur = con.cursor()

# add a comment to a venmo transaction
# can only be run after the transaction table has been populated

def add_comment(trans_id, message):
    query = '''
        INSERT INTO Comments
        VALUES(%s,%s);
        
        '''
    cmd = cur.mogrify(query, [trans_id, message])
    cur.execute(cmd)
    rows = cur.fetchall()
    return rows[0][0]



def main():
    trans_id = 2
    message = 'thanks for paying me!'
    add_comment(trans_id, message)

main()