from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world"

##############################
#   Return a list of a users projects for them to select from
##############################
@app.route('/get_projects')
def get_projects():
    pass

##############################
#   Build a gallery for a user based on the project they selected
##############################
@app.route('/build_gallery')
def build_gallery():
    pass

##############################
#   Fetch the rendered gallery (i.e. from the iFrame)
##############################
@app.route('/galleries/<int:gallery_id>')
def get_gallery(gallery_id):
    pass



if __name__ == '__main__':
    app.run()
