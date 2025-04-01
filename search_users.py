import firebase_admin
from firebase_admin import credentials, firestore

# Load the service account key
cred = credentials.Certificate("/Users/jianchen/Desktop/BIOME_Food_App/BIOME_FirebaseDB_Key.json")

# Initialize Firebase with the Firestore DB
firebase_admin.initialize_app(cred)

# Reference Firestore client
db = firestore.client()

# Reference the "users" collection in Firestore and retrieve the document for "jerry_chen"
user_ref = db.collection("users").document("jerry_chen")

# Fetch the document
user_doc = user_ref.get()

# Check if the document exists
if user_doc.exists:
    # Document exists, print the data
    print(f"User Data: {user_doc.to_dict()}")
else:
    print("User not found.")
