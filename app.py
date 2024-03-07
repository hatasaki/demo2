from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['GET'])
def add():
    # クエリパラメータから値を取得
    num1 = request.args.get('num1', type=int)
    num2 = request.args.get('num2', type=int)

    # 加算結果を計算
    result = num1 + num2

    # 結果をJSONとして返す
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(port=8080)