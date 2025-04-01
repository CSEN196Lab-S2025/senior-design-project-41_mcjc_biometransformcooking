import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

user_ref = db.collection("users").document("jerry_chen")
user_doc = user_ref.get()

if user_doc.exists:
    print(f"User Data: {user_doc.to_dict()}")
else:
    print("User not found.")
