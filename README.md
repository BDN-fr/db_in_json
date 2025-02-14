# DB_in_JSON: A Simple JSON-Based Database Library

DB_in_JSON is a Python library designed to provide a simple and lightweight solution for managing data using JSON files. It offers basic CRUD (Create, Read, Update, Delete) operations for collections of data, allowing for efficient storage and retrieval.

## Features

- Create and manage JSON-based databases.
- Create, read, update, and delete collections within the database.
- Insert, select, update, and delete data within collections.
- Utilize conditional operations for data manipulation.

## Installation

You can install DB_in_JSON with PyPI with the command :

```sh
pip install DB_in_JSON
```

## Usage

Here's a simple example of how to use DB_in_JSON:

```python
from db_in_json import DB

# Create a database (create the file if needed)
db = DB('DB.json')

# Get a collection (create it if it doesn't exist)
test_collection = db.getCollection('test_collection')

# Insert data into the collection
insert_uuid = test_collection.queries['insert']('Some good data')

# Select data from the collection
selected_items = test_collection.queries['select'](lambda uuid, data: True)

# Update data in the collection
updated_amt = test_collection.queries['update'](lambda uuid, data: True, 'Another updated data')

# Delete data from the collection
deleted_amt = test_collection.queries['delete'](lambda uuid, data: True)
```

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.