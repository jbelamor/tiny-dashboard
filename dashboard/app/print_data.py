import functools

from flask import (
    Blueprint, render_template, request, url_for, request, redirect)
from .database_manager import DB
import config

bp = Blueprint('show_data', __name__)

@bp.route('/')
def miau():
    return redirect('/links')

@bp.route('/stats')
def graphs():
    collections = DB.get_collections()
    total_count = DB.get_total_statistic()
    # return total_count
    return render_template(
        'stats.html',
        collections = collections,
        data = total_count
    )

@bp.route('/<collection>')
def table(collection):
    collections = DB.get_collections()
    if collection not in collections:
        collection = config.collection_links
    if collection in [config.collection_links, config.collection_apps]:
        template_to_render = collection + '_filter.html'
    else:
        template_to_render = 'table.html'
    return render_template(
        template_to_render,
        collections = collections,
        collection = collection,
        keys = DB.get_keys_coll(collection, {}, {'visible': 0}),
        elems = DB.get_all_data_collection(collection, {'visible':True}, {'visible': 0}),
        categories = DB.get_categories_apkpure()
        )    

@bp.route('/<collection>/<elem_id>', methods=['GET', 'POST'])
def view_element(collection, elem_id):
    collections = DB.get_collections()
    if request.method == 'GET':
        print(DB.get_one_elem(collection, {'_id': elem_id}, {'visible': 0}))
        return render_template(
            'elem_viewer.html',
            collection = collection,
            collections = collections,
            elem_data = DB.get_one_elem(collection, {'_id': elem_id}, {'visible': 0})
        )
    elif request.method == 'POST':
        result = request.form
        elems = dict(result.items())
        # DB.update_one_elem(collection, elem_id, json.dumps(elems))
        del elems['_id']
        for key in elems.keys():
            if elems[key] == 'True':
                elems[key] = True
            elif elems[key] == 'False':
                elems[key] = False
        # print(elems)
        DB.update_one_elem(collection, elem_id, elems)
        return render_template(
            'elem_viewer.html',
            collection = collection,
            collections = collections,
            elem_data = DB.get_one_elem(collection, {'_id': elem_id}, {'visible': 0}),
            alert = True,
            message = 'Element Updated'
        )
        # return render_template("result.html", result=result, method=request.method)
        
@bp.route('/<collection>/<elem_id>/delete', methods=['POST'])
def delete_element(collection, elem_id):
    #accion de eliminar
    DB.delete_elem(collection, elem_id)
    return (redirect('/' + collection))

@bp.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        collections = DB.get_collections()
        return render_template(
            'upload.html',
            collections=collections,
        )
    
    else:
        # elif request.method == 'POST':
        result = request.form
        file_ = request.files['file']
        if 'file' not in request.files:
            return (url_for('/upload'))
        dict_={}
        dict_['mimetype'] = file_.mimetype
        dict_['content_type'] = file_.content_type
        return render_template("result.html", result=dict_, filename=file_.content_type, method=request.method)
        # if 'file' not in request.files:
        #     flash('No file part')
        #     return (url_for('/upload'))
        # file_ = request.files['file']
        # if file_.filename == '':
        #     flash('No selected file')
        #     return (url_for('/upload'))
        # if file_.mimetype.split('/')[0] is not 'text':
        #     flash('Format not valid')
        #     return (url_for('/upload'))
        # if file_:
        #     filename = secure_filename(file_.filename)
        #     file_.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #     return (url_for('/upload'))
        
