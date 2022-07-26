
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



    
        



        

    

    
if __name__ == "__main__":
    app.run(port=8000, debug=True)

