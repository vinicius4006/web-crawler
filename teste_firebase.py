from firebase import firebase
firebase = firebase.FirebaseApplication('https://web-links-b05c4-default-rtdb.firebaseio.com', None)
result = firebase.get('/sites', None)
print(result)
