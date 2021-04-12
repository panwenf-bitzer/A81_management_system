import pymssql

def OEE_from_input():
    conn=pymssql.connect(host='10.15.1.199',user='sa',password='bitzer,.123',database='input')
    cur=conn.cursor()
    cur.execute('select OEE_for_shift_A,OEE_for_shift_B,OEE_for_shift_C from Daily_OEE')
    OEE=cur.fetchall()
    cur.close()
    conn.close()
    print(list(OEE[0]))
    return list(OEE[0])

def productivity_from_input():
    conn=pymssql.connect(host='10.15.1.199',user='sa',password='bitzer,.123',database='input')
    cur=conn.cursor()
    cur.execute('select shift_a_productivity,shift_b_productivity,shift_c_productivity from Productivity')
    Productivity = cur.fetchall()
    cur.close()
    conn.close()
    print(list(Productivity[0]))
    return list(Productivity[0])
if __name__ == '__main__':
    OEE_from_input()
    productivity_from_input()