from app import app, db

app.app_context().push()
db.create_all()
app.run(debug=True, port=5001)
