
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db



cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://face-recognition-mp1-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "2021182":
        {
            "name": "Devesh",
            "Department": "CSE",
            "Course": "B.Tech",
            "rno": "22",
            "starting_year": 2022,
            "total_attendance": 0,
            "year": 2,
            "last_attendance_time": "2021-01-01 00:00:01",
            "date":
                {

                },

        },
}

for key, value in data.items():
    ref.child(key).set(value)
