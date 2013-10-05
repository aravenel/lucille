from flask import Flask, render_template, jsonify, request, abort
from behance_python.api import API
import os
import json

app = Flask(__name__)

#CONFIG
api_key = os.environ.get('BEHANCE_API_KEY')


@app.route('/')
def index():
    return render_template('index.html')

##############################
#   Return a list of a users projects for them to select from
##############################
@app.route('/get_projects')
def get_projects():
    user_id = request.args.get('user_id')
    app.logger.debug('user id is %s' % user_id)
    if user_id:
        if api_key:
            behance = API(api_key)
            user = behance.get_user(user_id) #What if invalid user?
            projects = user.get_projects()
            app.logger.debug('%s projects returned' % len(projects))
            ret_data = []
            for project in projects:
                app.logger.debug('Cover is %s' % project.covers.values()[0])
                if len(project.covers.values()) > 0:
                    cover = project.covers.values()[0]
                else:
                    cover = None

                d = {
                    'id': project.id,
                    'title': project.name,
                    'cover': cover,
                }
                ret_data.append(d)
            #return jsonify(ret_data)
            return json.dumps(ret_data)
        else:
            app.logger.critical('No API key set!')
            abort(400)
    else:
        abort(400)


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
    app.debug = True
    app.run()
