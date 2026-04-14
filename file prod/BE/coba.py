from rethinkdb import RethinkDB
r = RethinkDB()
r.connect("localhost", 28015).repl()

RECREATE_DB = True
if RECREATE_DB:
    r.db_drop("DAFTARINNAMA").run()
    r.db_create("DAFTARINNAMA").run()
    r.db("DAFTARINNAMA").table_create("NamaTerdaftar").run()


def addNameToDB(name):
    print(r.table("NamaTerdaftar").insert([name]))



def printAllFromDB(tablename):
    cursor = r.table(tablename).changes().run()
    print(cursor)

if __name__ == '__main__':
    addNameToDB("aku")
    # printAllFromDB("NamaTerdaftar")


    # r.table()
