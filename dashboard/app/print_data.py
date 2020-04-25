import functools

from flask import (
    Blueprint, render_template, request, url_for, request, redirect)
from .database_manager import DB
import config

bp = Blueprint('show_data', __name__)

@bp.route('/')
def miau():
    return redirect('/stats')

@bp.route('/stats')
def graphs():
    collections = DB.get_collections()
    total_count = DB.get_total_statistic()
    return render_template(
        'stats.html',
        collections = collections,
        data = total_count
    )

@bp.route('/<collection>')
def table(collection):
    collections = DB.get_collections()
    if collection not in collections:
	return redirec('/stats')
    template_to_render = 'table.html'
    return render_template(
        template_to_render,
        collections = collections,
        collection = collection,
        keys = DB.get_keys_coll(collection, {}, {'visible': 0}),
        elems = DB.get_all_data_collection(collection, {'visible':{'$ne': False}}, {'visible': 0}),
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
        del elems['_id']
        for key in elems.keys():
            if elems[key] == 'True':
                elems[key] = True
            elif elems[key] == 'False':
                elems[key] = False
        DB.update_one_elem(collection, elem_id, elems)
        return render_template(
            'elem_viewer.html',
            collection = collection,
            collections = collections,
            elem_data = DB.get_one_elem(collection, {'_id': elem_id}, {'visible': 0}),
            alert = True,
            message = 'Element Updated'
        )

@bp.route('/<collection>/<elem_id>/delete', methods=['POST'])
def delete_element(collection, elem_id):
    DB.delete_elem(collection, elem_id)
    return (redirect('/' + collection))
