from rest_framework import serializers
from paytm_app.models import *
# from phonenumbers import carrier
# class 

class OperatorSerializer(serializers.ModelSerializer):
    class Meta:
        model= Operator
        fields = ['operator_name']

class CategoryPlanSerializer(serializers.ModelSerializer):
    class Meta :
        model = CategoryPlan
        fields = ['category_name']


class PlanSerializers(serializers.ModelSerializer):
    plan_type = serializers.SerializerMethodField()
    operator = serializers.SerializerMethodField()
    class Meta:
        model = Plan
        fields = (
            "price",
            "operator",
            'validity',
            "validity_type",
            'data',
            'data_type',
            'description',
            'plan_type',
        )

    def get_plan_type(self,obj):
        data = obj.plan_type.category_name
        category = CategoryPlan.objects.get(category_name = data)
        serializer = CategoryPlanSerializer(category)
        return serializer.data
    def get_operator(self,obj):
        data = obj.operator.operator_name
        operator = Operator.objects.get(operator_name = data)
        serializer = OperatorSerializer(operator)
        return serializer.data


############ Resposible for Recharge #################

class RechargeSerializer(serializers.ModelSerializer):
    plan_details = serializers.SerializerMethodField("get_plan_detail")

    class Meta:
        model = Recharge
        fields = ["mobile", "operator", "circle", "plan","recharge_date","plan_details"]

    def get_plan_detail(self, obj):
        data = Plan.objects.filter(price=obj.plan.price)
        serializer = PlanSerializers(data, many=True)
        return serializer.data

