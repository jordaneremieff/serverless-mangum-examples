# serverless-mangum-examples

Example ASGI applications and [Serverless Framework](https://serverless.com/framework/docs/) configurations using [Mangum](https://github.com/erm/mangum).

There are examples for the following ASGI-compatible frameworks:

* [Django](https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/)

* [FastAPI](https://fastapi.tiangolo.com/)

* [Quart](https://pgjones.gitlab.io/quart/)

* [Starlette](https://www.starlette.io/)

The examples are all intended to be basic starting points for deploying an ASGI application to AWS Lambda & API Gateway. Things like database support will require more advanced configurations.

## Requirements

- Python 3 (minimum version depending on application framework)
- Serverless Framework (a version that includes HTTP API support)
- Docker
- npm

## Setup

### Serverless Framework

```
npm install -g serverless@1.67.3
```

### Serverless Framework plugins

#### serverless-python-requirements

```
sls plugin install -n serverless-python-requirements
```


[GitHub](https://github.com/UnitedIncome/serverless-python-requirements#readme)

#### serverless-dotenv-plugin

```
npm i -D serverless-dotenv-plugin
```

[GitHub](https://github.com/colynb/serverless-dotenv-plugin#readme)

## TODO (maybe)

- Database examples
- WebSocket examples. WebSocket support in Mangum is currently "experimental" (ie: it might be broken).

