from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime, timedelta
# Create your views here.

from insurance_django.settings import db_user
from insurance_django.settings import JWT_EXPIRY_HOURS
from .JWT_token import generate_jwt


# 用户业务
class UserView(APIView):
    def _generate_tokens(self, username):
        """
        生成token
        :param username: username
        :return: token
        """
        # 颁发JWT
        now = datetime.utcnow()
        expiry = now + timedelta(hours=JWT_EXPIRY_HOURS)
        token = generate_jwt({'username': username, 'refresh': False}, expiry)
        return token

    def get(self, request, username, password, mobile):
        """用户注册"""
        # 1.校验数据
        if not all([username, password, mobile]):
            return Response({"message": "数据错误", "status": 400})
        # 查重
        if db_user.find_one({'username': str(username)}) is not None:
            return Response({"message": "用户名已存在", "status": 400})

        # 2. 存入数据库
        db_user.insert({
            "username": str(username),
            "password": str(password),
            "mobile": str(mobile),
            "is_admin": "0"
        })

        return Response({"message": "注册成功", "status": 200})

    def post(self, request, username, password):
        """用户登录"""
        # 1.校验数据
        if not all([username, password]):
            return Response({"message": "数据错误"})
        item = db_user.find_one({'username': username})
        if item is None:
            return Response({'message': "登录失败！", "status": 400})
        if item['is_admin'] == 1:
            if item["password"] == password:
                token = self._generate_tokens(username)
                return Response({'message': "admin登录成功", 'login_token': token, "status": 200})
        else:
            if item["password"] == password:
                token = self._generate_tokens(username)
                return Response({'message': "登录成功", 'login_token': token, "status": 200})
        return Response({'message': "账号或密码错误，登录失败！", "status": 400})