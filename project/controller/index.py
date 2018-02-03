from .. import app


@app.route('/')
def page_index():
    return "Hello Flask World!"
