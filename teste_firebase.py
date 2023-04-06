import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("./key/web-links-b05c4-firebase-adminsdk-dmkbz-2b90fced38.json")
firebase_admin.initialize_app(cred)


db = firestore.client()

obj1 = {
    "id": 1,
    "uri": "test.com"
}

obj2 = {
    "id":1,
    "id_site": 1,
    "type": "tag",
    "content": "asas"
}


doc_ref = db.collection(u's')s.document()u''id_si'