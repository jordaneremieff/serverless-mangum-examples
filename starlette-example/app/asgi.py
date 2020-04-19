from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route

from mangum import Mangum


async def homepage(request):
    return JSONResponse({"hello": "world"})


app = Starlette(debug=True, routes=[Route("/", homepage)])

handler = Mangum(app)
