from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from bson import json_util

from insurance_django.apps.users.JWT_token import admin_JWT, verify_jwt
from insurance_django.settings import db_insurance_data_fyj, db_insurance_data_tpy, db_insurance_data_zabb
from .huizezabb_sele import writepage_zabb
from .huizep import select_click
from .huizefyjsele import writePage

# Create your views here.
class GethistoryForm(APIView):
    """获取用户历史表单"""
    def get(self, request, token):
        # 1.校验JWT数据
        jwt_decode = verify_jwt(str(token))
        if jwt_decode is None:
            return Response({'message': "请重新登录token过期", 'status': 402})

        data = {}
        # 2.判断是否管理员登录
        key = 0
        if admin_JWT(token) == 1:
            # 管理员返回所有数据
            fyj_data = db_insurance_data_fyj.find({"username": {'$ne': 0.0}}).limit(10)
            tpy_data = db_insurance_data_tpy.find({"username": {'$ne': 0.0}}).limit(10)
            zabb_data = db_insurance_data_zabb.find({"username": {'$ne': 0.0}}).limit(10)
            for item in [fyj_data, tpy_data, zabb_data]:
                data[key] = json_util.dumps(item)
                key += 1
            return Response({'message': data, 'status': 200, 'data': 1})
        else:
            # 非管理员返回当前用户数据
            fyj_data = db_insurance_data_fyj.find({"username": jwt_decode["username"]}).limit(3)
            tpy_data= db_insurance_data_tpy.find({"username": jwt_decode["username"]}).limit(3)
            zabb_data = db_insurance_data_zabb.find({"username": jwt_decode["username"]}).limit(3)
            for item in [fyj_data, tpy_data, zabb_data]:
                data[key] = json_util.dumps(item)
                key += 1
            return Response({'message': data, 'status': 200, 'data': 0})


class ComForm(APIView):
    """
    get 获取表单数据
    """
    def get(self, request, name_id, token):
        # 1.获取校验数据
        jwt_decode = verify_jwt(str(token))
        if jwt_decode is None:
            return Response({'message': "请重新登录token过期", 'status': 402})

        # 2.查找数据
        if name_id == '0':
            fyj = db_insurance_data_fyj.find_one({"name": "福佑金生年金保险"})
            return Response({'message': json_util.dumps(fyj), 'status': 200})
        elif name_id == '1':
            tpy = db_insurance_data_tpy.find_one({"name": "太平财富智赢年金保险+荣耀金账户终身寿险（万能型）"})
            return Response({'message': json_util.dumps(tpy), 'status': 200})
        elif name_id == '2':
            zabb = db_insurance_data_zabb.find_one({"name": "珍爱宝贝教育年金保险计划"})
            return Response({'message': json_util.dumps(zabb), 'status': 200})

        # 4.返回响应
        return Response({'message': "数据查询错误请稍后尝试!", 'status': 400})

class DataComForm(APIView):
    """提交表单"""
    def post(self, request, name_id, token):
        # 1.获取校验数据
        jwt_decode = verify_jwt(str(token))
        if jwt_decode is None:
            return Response({'message': "请重新登录token过期", 'status': 402})

        # 2.存储数据
        try:
            if name_id == '0':
                if db_insurance_data_fyj.find_one({"username": jwt_decode["username"]}) is not None:
                    return Response({'message': "此保单您已填写，请查看记录!", 'status': 201})
                db_insurance_data_fyj.insert({
                    'username': jwt_decode["username"],
                    'sex': request.data["sex"],  # 性别
                    'insurantJob': request.data['insurantJob'],  # 承保职业
                    'insurantDateLimit': request.data['insurantDateLimit'],  # 保障期限
                    'paymentType': request.data['paymentType'],  # 缴费类型
                    'insureAgeLimit': request.data['insureAgeLimit'],  # 缴费年限
                    'premium': request.data['premium'],  # 保费
                    'coverageAreaName': request.data['coverageAreaName']  # 投保地区
                })
                writePage(str(jwt_decode["username"]))
            elif name_id == '1':
                if db_insurance_data_tpy.find_one({"username": jwt_decode["username"]}) is not None:
                    return Response({'message': "此保单您已填写，请查看记录!", 'status': 201})
                db_insurance_data_tpy.insert({
                    'username': jwt_decode["username"],
                    'sex': request.data['sex'],  # 性别
                    'insurantJob': request.data['insurantJob'],  # 承保职业
                    'insurantDateLimit': request.data['insurantDateLimit'],  # 保障期限
                    'paymentType': request.data['paymentType'],  # 缴费类型
                    'insureAgeLimit': request.data['insureAgeLimit'],  # 缴费年限
                    'premium': request.data['premium'],  # 年交保费
                    'isInsure': request.data['isInsure'],  # 荣耀金万能账户
                })
                select_click(str(jwt_decode["username"]))
            elif name_id == '2':
                if db_insurance_data_zabb.find_one({"username": jwt_decode["username"]}) is not None:
                    return Response({'message': "此保单您已填写，请查看记录!", 'status': 201})
                db_insurance_data_zabb.insert({
                    'username': jwt_decode["username"],
                    'policyholderExemption': request.data["policyholderExemption"],  # 投保人保费豁免
                    'additionalInsureAgeLimit': request.data["additionalInsureAgeLimit"],  # 投保人保费豁免缴费年限
                    'vesterSex': request.data["vesterSex"],  # 投保人性别
                    'sex': request.data["sex"],  # 被保险人性别
                    'province': request.data["province"],  # 投保地区
                    'leastamount': request.data["leastamount"],  # 基本保额
                    'insurantDateLimit': request.data["insurantDateLimit"],  # 保障期限
                    'insureAgeLimit': request.data["insureAgeLimit"],  # 缴费年限
                    'paymentType': request.data["paymentType"],  # 缴费类型
                    'seniorUniversityEdu': request.data["seniorUniversityEdu"],  # 高中大学教育年金保额
                    'seriousIllness': request.data["seriousIllness"],  # 重大疾病保险保额
                    'hospitalAllowance': request.data["hospitalAllowance"],  # 长期住院津贴保额
                    'accidentalInjury': request.data["accidentalInjury"],  # 长期意外伤害医疗保险保额
                    'regular': request.data["regular"],  # 臻爱定期寿险保额
                    'additionalRiskPeriod': request.data["additionalRiskPeriod"],  # 高中大学教育年金保障期限
                })
                writepage_zabb(str(jwt_decode["username"]))
        except Exception as e:
            if name_id == '0':
                db_insurance_data_fyj.delete_one({'username': jwt_decode["username"]})
            elif name_id == '1':
                db_insurance_data_tpy.delete_one({'username': jwt_decode["username"]})
            elif name_id == '2':
                db_insurance_data_zabb.delete_one({'username': jwt_decode["username"]})
            print("浏览器错误:"+ str(e.args))
            return Response({'message': "数据存储错误请稍后尝试!", 'status': 400})
        # 4.返回响应
        return Response({'message': "OK", 'status': 200})

class Image(APIView):
    """获取图片url"""
    def get(self, request):
        # 1. 获取数据
        try:
            fyj = db_insurance_data_fyj.find_one({"name": "福佑金生年金保险"})
            tpy = db_insurance_data_tpy.find_one({"name": "太平财富智赢年金保险+荣耀金账户终身寿险（万能型）"})
            zabb = db_insurance_data_zabb.find_one({"name": "珍爱宝贝教育年金保险计划"})

            # 格式化数据
            data = {}
            key = 0
            for item in [fyj['image_url'], tpy['image_url'], zabb['image_url']]:
                data[key] = json_util.dumps(item)
                key += 1
        except Exception as e:
            return Response({'message': "获取失败, 请稍后尝试!", 'status': 400})

        # 返回响应
        return Response({'message': data, 'status': 200})