import sdb

db = sdb.init(False, 'testdb.sdb')

sdb.clear(db)

count = 0
for count in range(40):
    count += 1
    sdb.insert(db, f'Line {count};{count - 3}', f'00{count}')

result = sdb.read(db, 8)
print(result)
sdb.get_parts(result)
print(result[0], result[1])

#result = sdb.read(db, 40)
#print(result)

sdb.remove(db, '005')