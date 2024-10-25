from pymongo import MongoClient

class User():
    def __init__(self, name, password):
        self.name = name
        self.password = password
    
    def serialize(self):
        return {"name": self.name, "password":self.password}

# Replace the placeholders with your actual values
username = "root"
password = "Password0-"
host = "localhost"
port = "27017"

# Format the connection string with username and password
uri = f"mongodb://{username}:{password}@{host}:{port}"
client = MongoClient(uri)

# Access the database (creates it if it doesn't exist)
db = client["cs411"]

# Access the collection (like a table in SQL, creates it if it doesn't exist)
collection = db["user"]

u = User("berkan", "0x72ab")

#collection.insert_one(u.serialize())
print("u.name=",collection.find_one({"name":u.name }))
