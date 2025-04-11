from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
        <head>
            <title>个人网站</title>
        </head>
        <body>
            <h1>欢迎来到我的个人网站！</h1>
            <p>这是我的个人简介页面。</p>
            <a href="/about">关于我</a>
        </body>
    </html>
    '''

@app.route('/about')
def about():
    return '''
    <html>
        <head>
            <title>关于我</title>
        </head>
        <body>
            <h1>关于我</h1>
            <p>这里是关于我的详细信息。</p>
            <a href="/">返回首页</a>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)