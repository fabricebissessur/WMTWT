from flask import Flask, url_for, request, render_template
from app import app

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

    # build the URL initially
    basePath = "https://api.themoviedb.org/3/"
    requesType = "trending/"
    mediaType = "movie/"
    timeWindow = "week"
    apiKey = "89bf4a8b688cd3ae5e0932562b79234d"
    url = basePath + requesType + mediaType + timeWindow + '?api_key=' + apiKey
    print (url)

    # Fetch results for given URL
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


# Server - Display list or movies resulted from the filters added by the user
@app.route('/results', methods=['POST'])
def results():
    # Filters should come through the POST method
    if request.method == 'POST':

        # build the URL initially
        basePath = "https://api.themoviedb.org/3/"
        requesType = "discover/"
        mediaType = "movie"
        apiKey = "89bf4a8b688cd3ae5e0932562b79234d"

        url = basePath + requesType + mediaType + '?api_key=' + apiKey

        # fetch selected values sent by the user through the POST method
        year = request.form['years']
        rating = request.form['rating']

        # complete the URL base on added filters
        if year != "any":
            url = url + "&primary_release_year=" + year
        if rating != "any":
            url = url + "&vote_average.gte=" + rating

        print ("Year Selection: " + year)
        print ("Rating Selection: " + rating)
        print (url)

        # Fetch results for given URL
        r = requests.get(url)
        data = r.json()
        movies = data['results']
        
        # Render the page
        return render_template('results.html', movies = movies, posterBasePath = getPosterBasePath(), poster_size = "w92")

    else:
        # To be formatted with proper page later
        return "<h2>Invalid Request</h2>"
    