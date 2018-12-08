import psycopg2 as pg2

# Connect to an existing database
con = pg2.connect(database='postgres', user='isdb')
con.autocommit = True
# Open a cursor to perform database operations
cur = con.cursor()

print("Max (Uid 3) adds Alex (Uid 4) as a friend and Alex adds him back.")

# Adds user2 to user1's friends 
# Adds user1 to user2's friends

def add_friend(user1, user2):
    query = '''
        INSERT INTO Friends
        VALUES(%s,%s)    
        '''
    cmd = cur.mogrify(query, [user1, user2])
    
    query = '''
        INSERT INTO Friends
        VALUES(%s,%s)
        '''
    cmd = cur.mogrify(query, [user2, user1])
    
    cur.execute(cmd)
    rows = cur.fetchall()
    return rows[0][0]
    

def main():
   user1 = 3
   user2 = 4
   add_friend(user1,user2) 

