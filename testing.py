
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://mkboxer14:Bhushan1718@cluster0.vrrkrjm.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)