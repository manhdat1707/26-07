

from config import *



@app.route('/user', methods=['GET'])
def get_User():
    results = []
    if r.exists('user'):
        results = json.loads(r.get('user'))
    else :
        data = User.get_list_user()
        rval = json.dumps(data)
        r.set('user' ,rval)
        results = data
    return jsonify({
        "data": results
    })
@app.route('/update/<int:id>', methods=['PUT'])
def update_User(id):
    query = User.select().where(User.id == id)
    if query.exists():
        request_data = request.get_json()
        User.update_one_user(id ,request_data['name'], request_data['age'])
        r.delete("user")
        results = list(User.select().where(User.id == id).dicts())
        return jsonify({
            "data": results
        }), 200
    else :
        return "khong tim thay id ",400
            




    
if __name__ == "__main__":
    app.run(port=8000, debug=True)

