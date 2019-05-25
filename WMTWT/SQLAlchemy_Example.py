from flask_sqlalchemy import SQLAlchemy

######### db creation starts ###########################################
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/pages.db'
db = SQLAlchemy(app)

# table creation to contain list of movies returned by API
class Movies(db.Model):
    movie_title = db.Column(db.String(1000), primary_key=True)
    poster = db.Column(db.String(1000), nullable=True)
    movie_rating = db.Column(db.String(10), nullable=True)
    movie_release_date = db.Column(db.String(30), nullable=True)
    movie_overview = db.Column(db.String(1000), nullable=True)

# Create all tables stored in the metadata. Conditional by default, will not attempt to recreate tables already present in the target database.
db.create_all()

Movies.query.delete()
db.session.commit()

for i in range(1,10):
    db.session.add(Movies(movie_title=str(i), poster="bla bla", movie_rating="bla bla", movie_release_date="bla bla", movie_overview="bla bla"))

db.session.commit()
print(Movies.query.count())
print(Movies.query.all())

######### db creation ends ###########################################

