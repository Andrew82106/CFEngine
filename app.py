from flask import Flask, render_template
app = Flask(__name__)  # 开头必写，创建一个Flask对象从而进行后续操作
app.config["SECRET_KEY"] = "ABCDFWA"  # 为防CSRF提供一个密匙


@app.route('/')
def hello_world():  # 这是视图函数
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True, port=9999)  # 用刚刚创建的Flask对象控制程序运行