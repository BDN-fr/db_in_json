from files import *
from queries import *

class DB(object):
    def __init__(self, file):
        """
        The DB object, linked to your JSON file

        Args:
            file (str): The JSON file containing your DB
        """
        assert type(file) == str, 'Your file path is not a string'
        self.file = file
        if not doesFileExists(file):
            with open(file, 'x') as f:
                f.write('{}')
        elif getRawText(file) == '':
            setFileJSON(file, {})

    def purge(self):
        """
        Purge the DB
        """
        setFileJSON(self.file, {})

    def getCollection(self, name):
        """
        Get the collection object, create the collection if does'nt exists

        Args:
            name (str): The name of the collection

        Returns:
            collection: The collection object
        """
        return self.collection(self, name)

    class collection(object):
        def __init__(self, db, name):
            """
            Initialize the collection object.

            Args:
                db (DB): The DB object to which this collection belongs.
                name (str): The name of the collection.
            """
            self.db = db
            self.name = name
            self.queries = {
                'insert': lambda data: insert(self, data),
                'delete': lambda condition: delete(self, condition),
                'select': lambda condition: select(self, condition),
                'update': lambda condition, data: update(self, condition, data)
            }

            content = getFileJSON(self.db.file)
            if not (name in content):
                content[name] = {}
                setFileJSON(self.db.file, content)

        def remove(self):
            """
            Remove your collection from the DB
            """
            content = getFileJSON(self.db.file)
            if self.name in content:
                content.pop(self.name)
            setFileJSON(self.db.file, content)

        def purge(self):
            """
            Remove all the content of the collection
            """
            content = getFileJSON(self.db.file)
            if self.name in content:
                content[self.name] = {}
            setFileJSON(self.db.file, content)


# Tests
if __name__ == '__main__':
    import time

    sleepTime = 3
    db = DB('test-DB.json')

    test2 = db.getCollection('test2')
    print('created collection')
    time.sleep(sleepTime)

    uuids = []
    for i in range(1, 6):
        insert_id = test2.queries['insert']({'message': 'I <3 code', 'id': i})
        print('inserted data', insert_id)
        uuids.append(insert_id)
    time.sleep(sleepTime)

    deleted_amt = test2.queries['delete'](lambda uuid, data: data['id'] <= 3)
    print(f'deleted {deleted_amt} entries')
    time.sleep(sleepTime)

    selected_items = test2.queries['select'](lambda uuid, data: uuid == uuids[3])
    print(f'selected {len(selected_items)} entries : ')
    print(selected_items)
    time.sleep(sleepTime)

    updated_amt = test2.queries['update'](lambda uuid, data: uuid == selected_items[0]['uuid'], 'Updated data')
    print(f'updated {updated_amt} entries')
    time.sleep(sleepTime)

    test2.purge()
    print('purged collection')
    time.sleep(sleepTime)

    test2.remove()
    print('removed collection')
    time.sleep(sleepTime)

    os.remove('test-DB.json')
    print('removed file')
    del db, test2