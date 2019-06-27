def index():
    with open('/home/morat/program/python/aiohttp2/socket/templates/index.html') as template:
        return template.read()


def blog():
    with open('/home/morat/program/python/aiohttp2/socket/templates/blog.html') as template:
        return template.read()
