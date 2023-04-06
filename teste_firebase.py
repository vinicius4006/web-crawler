import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("./key/web-links-b05c4-firebase-adminsdk-dmkbz-2b90fced38.json")
firebase_admin.initialize_app(cred)


db = firestore.client()

sites_ref = db.collection(u'sites_info')
docs = sites_ref.stream()

for doc in docs:
    print(f'${doc.id} => {doc.to_dict()}')