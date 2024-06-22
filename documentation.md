## Documentation (v1.0.7)

### Load the Database (init)

The init() function loads the database
in a string variable.

```python
# Importing the module
import sdb

database_name = sdb.init(output=True, 
                         file='mydatabase.sdb')
```

The init() function takes 2 arguments

- output » The output argument takes only ```True``` or ```False```. If the output argument is ```True``` it will print the version of the database that is installed. If it is ```False``` it will skip this process.
- file   » In this argument you need to give the filename and location so it can load it.

### Insert Data in the Database (insert)

With the insert() function you can put data in the database.

```python
# Importing the module
import sdb

database = sdb.init(output=True,
                    file='mydatabase.sdb')

# Adding Data to the database
# Use ; if you want multiple entries in one row
sdb.insert(database=database,
           data='David;25;USA',
           id='1')
```
The insert() function takes 3 arguments

- database » In the database argument you need to put your variable that you initialised in.
- data     » The data argument is what you want to insert into the database. To put multiple things in one row u can use a ```;```.
- id       » In here you need to put the id you want to safe this data to. This will be important if you want to access the data or remove the data.

### Read Data from the Database (read & read_row)

With the read() function and read_row() function you can access the data in the database

#### read()
```python
# Importing the module
import sdb

database = sdb.init(output=True,
                    file='mydatabase.sdb')

content = sdb.read(database=database,
                   id='1')
print(content)
```
The read() function takes 2 arguments

- database » In the database argument you need to put your variable that you initialised in.
- id       » In here put the id you want to access the data from as a string.

#### read_row()
```python
# Importing the module
import sdb

database = sdb.init(output=True,
                    file='mydatabase.sdb')

content = sdb.read_row(database=database,
                       row=1)
print(content)
```
The read_row() function takes 2 arguments

- database » In the database argument you need to put your variable that you initialised in.
- row       » In here put the row you want to access the data from as an integer.

#### get_parts()
```python
...

content = get_parts(content)
print(content[0], content[1])
```
The get_parts() function takes 1 argument

- string » The data you want to split.

### Remove Data from the Database (remove & remove_row)

With the remove() function and remove_row() function you can remove specific data from the database

#### remove()
```python
# Importing the module
import sdb

database = sdb.init(output=True,
                    file='mydatabase.sdb')

# Removing the Data with the id '1'
sdb.remove(database=database,
           id='1')
```

The remove() function takes 2 arguments

- database » In the database argument you need to put your variable that you initialised in.
- id       » In here put the id you want to delete the data from as a string.

#### remove_row()
```python
# Importing the module
import sdb

database = sdb.init(output=True,
                    file='mydatabase.sdb')

# Removing the Data in row 1
sdb.remove_row(database=database,
               row=1)
```

The remove_row() function takes 2 arguments

- database » In the database argument you need to put your variable that you initialised in.
- row       » In here put the row you want to delete the data from as an integer.

### Clearing the Database (clear)
You can use the clear() function from sdb to completly wipe the database

```python
# Importing the module
import sdb

database = sdb.init(output=True,
                    file='mydatabase.sdb')

# Removing every single piece of data that is stored in the database
sdb.clear(database=database)
```

The clear() function takes 1 argument

- database » In the database argument you need to put your variable that you initialised in.


### Bye!

If you read all that stuff. Thank you.

I hope you enjoyed your time here!

I hope to see you again soon :)