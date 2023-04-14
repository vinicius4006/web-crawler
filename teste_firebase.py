import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import io

cred = credentials.Certificate("./key/web-links-b05c4-firebase-adminsdk-dmkbz-2b90fced38.json")

firebase_admin.initialize_app(cred)


db = firestore.client()


def salvarSite(url):
    _, data = db.collection("sites").add({
    "site": url,
        })
    return data.id
 
        

def salvarBody(id, content):
       db.collection("sites").document(id).collection("info").add({
        "type": "body",
        "content": convertBlob(content)
        })
 

def salvarMetaTags(id, tags):
        for tag in tags:
            
            db.collection("sites").document(id).collection("info").add({
            "type": tag.name,
            "content": convertBlob(tag.text)
             })
        

def convertBlob(content):
        blob = io.BytesIO()
        blob.write(b"{content}")
        return blob.getvalue()
            



