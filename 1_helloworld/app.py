# 从flask包中导入Flask对象.

from flask import Flask, jsonify, url_for, request, redirect

import config  # 导入我们创建的模块 .

# 使用Flask创建一个app对象, 并且传入一个__name__参数.
# 如果是以主文件进行启动, 那么__name__为__main__, 以当前这个文件作为参考.
app = Flask(__name__) # 固定的.
# 我们可以通过查阅Flask的官网来查看有什么样子的配置信息.
# 然后使用app.config['name'] = value. 进行配置
# app.config['JSON_AS_ASCII'] = False # 设置为False, 这样就能够显示中文了.
# 实际中我们的config可能会非常多, 所以我们通常是放到一个py文件中去. 然后使用app.config.from_object()进行传输即可
# 以后所有的配置项, 都是放到config配置文件中.
app.config.from_object(config)



books = [
    {"id": 1, "name": "三国演义"},
    {"id": 2, "name": "水浒传"},
    {"id": 3, "name": "红楼梦"},
    {"id": 4, "name": "西游记"},

]

"""
自定义http方法:
    再app.route中加入methods参数, 然后使用列表, 指定我们可以接受的方法. 
    默认再地址栏中输入地址是使用的是显示请求, 也就是get请求. 
    如果是隐式, 那么我们就是用post请求. 
    如果是需要从服务器上获取数据, 一般都是get请求. 
    如果前端将数据发送给服务器, 一般用post请求
    再@app.route()添加methods参数, 是一个列表类型, 可以传递多个. 
"""

# 创建一个动态的路由和URL映射:
@app.route("/book/<string:book_id>", methods=['POST', 'GET']) # 当你访问指定页面下的url: 例如/book/1, 那么就会将这个book_id传给下面的函数
def book_detail(book_id): # 这样我们就可以获取到这个id.
    # 这里的book_id和上面定义好的, 传进来的类型是一样的, 所以我们注意判断.
    print(book_id)
    for book in books:
        if book["id"].__str__() == book_id: # 改变类型.
            return book

    return f"id为: {book_id} 没有找到"



@app.route("/profile")
def profile():
    """
    参数传递的两种方式:
    1. 作为url的组成部分: /book/1 (上面使用的)
    2. 查询字符串的形式: /book?id=1 (这也是非常常见的一种形式)


    """
    # 如何获取查询字符串当中的参数呢?
    user_id = request.args.get("id")
    if  user_id: # 如果传入了id进来:
        return f"user_id:{user_id}个人用户中心"
    else: # 如果没有传入id, 那么我就直接重定向到这个首页当中去. redirect
        return redirect(url_for("index")) # 然后重定向到首页当中去.





# 添加一个路由: -> 固定页面路由.
@app.route("/book/list")
def book_list():
    # return tuple(books)
    # return json.dumps(books) # 太慢.

    # 使用url_for, 通过函数找到对应的url. 并且自动处理
    for book in books:
        book['url'] = url_for("book_detail", book_id=book['id']) #
        # url_for() # 第一个参数是函数名字, 后面的参数就是函数参数, 因为函数参数就是从url中拿到的, 所以反过来我们也可以通过函数参数找到拼接好的url
        # 同时这样修改后, 我们修改该函数上的route中的url时, 就可以直接修改url了. 从而达到重构的效果.
    return jsonify(books)  # Flask提供了一个函数: 这样我们就可以快速返回我们所需要的文件了.



# 路由 -> app.route: 设置访问的url, 这里设置成一个根路径.
@app.route('/') # 访问到这个路径后, 要执行什么代码呢, 就由下面的函数进行确定. 所以是路径和函数进行映射.
def index():  # put application's code here -> 试图函数
    # return 'WDNMD World!' # 返回字符串.
    # json.dump(ensure_ascii=False) # 不易ASCII码进行显示, 这样就可以显示中午了, 上面的同理.
    return {"username": "这里是首页啊."}


# 如果我们想要改变代码, 同时直接反映到浏览器当中, 那么我们就需要开启debug mode


# 如果当作主运行文件, 那么我们就运行文件.
if __name__ == '__main__':
    app.run()
