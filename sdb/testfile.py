import sdb

db = sdb.init(True, 'testdb.sdb')
print(db)

sdb.clear(db)

count = 0
for count in range(40):
    count += 1
    sdb.insert(db, f'Line;{count};{count - 3}', f'{count}')

result = sdb.read(db, '12')
print(result)
result = sdb.get_parts(result)
print(result[0], result[1], result[2])

result = sdb.read_row(db, 40)
print(result)

test = sdb.get_ids(db)
print(test)

sdb.remove(db, '40')
