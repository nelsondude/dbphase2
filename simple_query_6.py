import psycopg2 as pg2


# Connect to an existing database
con = pg2.connect(database='postgres', user='isdb')
con.autocommit = True
# Open a cursor to perform database operations
cur = con.cursor()

# View user profile information
# Update username for individuals only


def view_profile(username):
    print("running")
    query = '''
        SELECT *
          FROM User_Info
         WHERE username = %s;    
        '''
    cmd = cur.mogrify(query,[username])
    cur.execute(cmd)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    #return rows[0][0]

def update_profile(new_username, old_username):
    query = '''
        UPDATE User_Info
           SET username = %s
         WHERE username = %s;
         '''
    cmd = cur.mogrify(query, [new_username, old_username])
    cur.execute(query, [new_username, old_username ])
    #rows = cur.fetchall()
    #return rows[0][0]

def main():
    print("start")
    username = 'AnnieS'
    new_username = 'ASpahn'
    view_profile(username)
    update_profile(new_username,username)
    view_profile(new_username)

main()
