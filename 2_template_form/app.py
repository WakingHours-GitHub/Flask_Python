"""
在这个项目中, 我们主要讲解Flask中的模板.
Flask中的模板是基于jinjia2的, 也是一个非常厉害的东西.


我们再项目结构中的templates中创建我们的模板文件, 其实就是html文件.
然后我们再 视图函数 中使用render_template()函数, 将我们的模板加载进来

"""
from flask import Flask, render_template

app = Flask(__name__) # 你可以在这修改template_folder参数, 指定到你的模板存放路径.



@app.route("/about")
def about(): # 我们要渲染.
    # 注意, 这里要return.
    return render_template("index.html") # 默认就是在templates文件中寻找, 并不是基于本文件的相对路径.

@app.route('/')
def hello_world():  # put application's code here
    # return 'Hello World!'
    return render_template("index.html") # 默认就是在templates文件中寻找, 并不是基于本文件的相对路径.

@app.route("/blog<blog_id>")
def blog(blog_id):
    return  render_template("blog_detail.html", **{
        "blog_id": blog_id, # 传入进去的是关键字参数, 所以我么采用字典解包的形式来去传入参数.
    })


if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=5000)
