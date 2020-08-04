from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework


@app.route('/')
def shoppingmall():
    return render_template('index_shoppingmall.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    # 여길 채워나가세요!
    name_receive = request.form['name_give']
    count_receive = request.form['count_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']

    doc = {
        'name': name_receive,
        'count': count_receive,
        'address': address_receive,
        'phone': phone_receive
    }

    db.shoppingmall.insert_one(doc)

    return jsonify({'result': 'success', 'msg': '주문이 완료되었습니다. 곧 맑은물 한바가지가 배송될 예정입니다. : )'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():

    orders = list(db.shoppingmall.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)