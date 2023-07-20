import time

from starlette.middleware import Middleware
from starlette.responses import JSONResponse

from app.logger import Logger
from app.utils.jwt_token import decode_access_token

logger = Logger(logger_name='middleware')


async def authenticate(request, call_next):
    path = request.url.path
    if not path.startswith("/admin") and not path.startswith("/tatoo") and not path.startswith("/users"):
        cookies = request.cookies

        try:
            user = decode_access_token(token=cookies['access_token'])
            response = await call_next(request, user)

        except KeyError:
            response = JSONResponse(status_code=401, content={"message": "Unauthorized. Token missing"})

        except Exception as ex:
            # print(ex)
            logger.error(str(ex))
            response = JSONResponse(status_code=500, content={"message": "Internal Server Error"})

        return response

    return await call_next(request)
        # redirect to login


async def admin_authenticate(request, call_next):

    path = request.url.path
    if path.startswith("/admin"):

        cookies = request.cookies

        try:
            user = decode_access_token(token=cookies['admin_sessionID'])
            response = await call_next(request)

        except KeyError:
            response = JSONResponse(status_code=403, content={"message": "You have not admin cookie"})

        except Exception as ex:
            logger.error(str(ex))
            response = JSONResponse(status_code=500, content={"message": "Internal Server Error"})

        return response

    return await call_next(request)


async def work_time(request, call_next):
    start = time.time()

    response = await call_next(request)

    end = time.time()

    time_result = end - start

    # logger.info(time_result)

    return response


