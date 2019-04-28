import datetime
import os
import sys

import aiohttp
from aiohttp import web
from aiohttp_session import get_session
import random

class Handers:
    routes = web.RouteTableDef()

    @routes.get('/t/{myname}', name="myroute")
    async def myroute(request):
        t = request.app.router['myroute'].url_for(myname="fc").with_query({"a": "b", "c": "d"})
        assert request.match_info['myname'] != "e"

        return web.Response(
            text="Hello, {} {}".format(request.match_info['myname'], t))

    @routes.get('/json', name="myjson")
    async def myjson(request):
        data = {'some': 'data' + str(random.randint(0, 1000))}
        return web.json_response(data)

    @routes.get('/session')
    async def session(request):
        session = await get_session(request)
        last_visit = session['last_visit'] if 'last_visit' in session else None
        session["last_visit"] = str(datetime.datetime.now())
        text = 'Last visited: {}'.format(last_visit)
        return web.Response(text=text)

    @routes.get('/')
    async def root(request):
        return web.Response(text='''<html><head></head><body>
                        Hello, World.<br /><br />
                        <a href="/login">Log me in</a><br />
                    </body></html>''', content_type='text/html')

    @routes.get('/r')
    async def redirect(request):
        raise web.HTTPFound('/login')

    @routes.get('/login')
    async def get_login(request):
        return web.Response(text='''<form action="/login" method="post" accept-charset="utf-8"
      enctype="application/x-www-form-urlencoded">

    <label for="login">Login</label>
    <input id="login" name="login" type="text" value="" autofocus/>
    <label for="password">Password</label>
    <input id="password" name="password" type="password" value=""/>

    <input type="submit" value="login"/>
</form>''', content_type='text/html')

    @routes.post('/login')
    async def post_login(request):
        data = await request.post()
        return web.json_response({"id":data["login"], "pass":data["password"]})

    @routes.get('/upload')
    async def upload(request):
        return web.Response(text='''<form action="/upload" method="post" accept-charset="utf-8"
      enctype="multipart/form-data">

    <label for="content">选择文件</label>
    <input id="content" name="content" type="file" value=""/>

    <input type="submit" value="submit"/>
</form>''', content_type='text/html')

    @routes.post('/upload')
    async def upload(request):
        reader = await request.multipart()

        # /!\ Don't forget to validate your inputs /!\
        # reader.next() will `yield` the fields of your form
        field = await reader.next()
        assert field.name == 'content'

        # You cannot rely on Content-Length if transfer is chunked.
        size = 0
        with open(os.path.join(sys.path[0], field.filename), 'wb') as f:
            while True:
                chunk = await field.read_chunk()  # 8192 bytes by default.
                if not chunk:
                    break
                size += len(chunk)
                f.write(chunk)

        return web.Response(text='{} sized of {} successfully stored'
                                 ''.format(field.filename, size))

    @routes.get('/ws')
    async def websocket_handler(request):

        ws = web.WebSocketResponse()
        print("ws get")

        await ws.prepare(request)

        print("ws init complete")

        async for msg in ws:
            if msg.type == aiohttp.WSMsgType.TEXT:
                if msg.data == 'close':
                    await ws.close()
                else:
                    print(msg.data)
                    await ws.send_str(msg.data + '-> answer')
            elif msg.type == aiohttp.WSMsgType.ERROR:
                print('ws connection closed with exception %s' %
                      ws.exception())

        print('websocket connection closed')

        return ws





