import jwt
from insurance_django.settings import JWT_SECRET
from insurance_django.settings import db_user

def generate_jwt(payload, expiry, secret=None):
    """
    生成jwt
    :param payload: dict 载荷
    :param expiry: datetime 有效期
    :param secret: 密钥
    :return: jwt
    """
    _payload = {'exp': expiry}
    _payload.update(payload)

    if not secret:
        secret = JWT_SECRET

    token = jwt.encode(_payload, secret, algorithm='HS256')
    return token.decode()


def verify_jwt(token, secret=None):
    """
    检验jwt
    :param token: jwt
    :param secret: 密钥
    :return: dict: payload
    """
    if not secret:
        secret = JWT_SECRET

    try:
        payload = jwt.decode(token, secret, algorithm=['HS256'])
    except jwt.PyJWTError:
        payload = None
    return payload


def admin_JWT(token):
    """
    验证JWT是否是管理员
    :return:
    """
    jwt_decode = verify_jwt(token)
    if not jwt_decode:
        return 2
    item = db_user.find_one({'username': jwt_decode['username']})
    if item['is_admin'] == "1":
        return 1
    else:
        return 0