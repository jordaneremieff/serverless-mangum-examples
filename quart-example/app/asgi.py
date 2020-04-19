from quart import Quart

from mangum import Mangum


app = Quart(__name__)


@app.route("/")
async def hello():
    return "hello"


handler = Mangum(app)
