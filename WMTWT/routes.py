from flask import Flask, url_for, request, render_template
from app import app
from flask_sqlalchemy import SQLAlchemy

# requests being the package to retrieve API requests responses
import requests


# Function to retrieve the base url to access images (posters, logos, etc..) through the configuration url
def getPosterBasePath():
    basePath = "https://api.themoviedb.org/3/configuration"
    apiKey = "89bf4a8b688cd3ae5e0932562b79234d"
    url = basePath + '?api_key=' + apiKey
    r = requests.get(url)
    data = r.json()
    images = data['images']
    posterBasePath = images['secure_base_url']
    print (posterBasePath)
    return posterBasePath

# Server - Display index page with trending movies of the week when app is initiated / loaded
@app.route('/')
def index():
    basePath = "https://api.themoviedb.org/3/"
    requesType = "trending/"
    mediaType = "movie/"
    timeWindow = "week"
    apiKey = "89bf4a8b688cd3ae5e0932562b79234d"

    url = basePath + requesType + mediaType + timeWindow + '?api_key=' + apiKey
    print (url)
    r = requests.get(url)
    data = r.json()
    movies = data['results']

    # Render the page
    if request.method == 'GET':
        #send user the page/form. e.g, movies = movies means movies as variable to pass to the html template and movies being the dictionary from the api response
        return render_template('index.html', movies = movies, posterBasePath = getPosterBasePath(), poster_size = "w92")
    else:
        # To be formatted with proper page later
        return "<h2>Invalid Request</h2>"

@app.route('/paginate')
def paginate():
    basePath = "https://api.themoviedb.org/3/"
    requesType = "trending/"
    mediaType = "movie/"
    timeWindow = "week"
    apiKey = "89bf4a8b688cd3ae5e0932562b79234d"

    url = basePath + requesType + mediaType + timeWindow + '?api_key=' + apiKey
    print (url)
    r = requests.get(url)
    data = r.json()
    movies = data['results']
    moviesPaginate = movies.paginate()
    print("paginate:::::::::::::::::::" + moviesPaginate)

    # Render the page
    if request.method == 'GET':
        #send user the page/form. e.g, movies = movies means movies as variable to pass to the html template and movies being the dictionary from the api response
        return render_template('index.html', movies = movies, posterBasePath = getPosterBasePath(), poster_size = "w92")
    else:
        # To be formatted with proper page later
        return "<h2>Invalid Request</h2>"