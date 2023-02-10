from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from paytm_app.models import *
from paytm_app.serializers import *
from rest_framework.response import Response


# Create your views here.

class ShowAllPlans(APIView):
    """ 
        API is used for show all rechage plans
    """
       
    def get(self,request):
        queryset = Plan.objects.all()
        serializer = PlanSerializers(queryset,many=True)
        
        return Response({'status':"successs",'plans': serializer.data})
    

class RechargeView(APIView):

    def post(self, request):
        """
            API is use for do recharge 
        """
        mobile = request.data.get('mobile')
        plan = request.data.get('plan')
        operator = request.data.get('operator')
        circle = request.data.get("circle")
      
        try:
            plan_obj = Plan.objects.get(price = plan)
        except ValueError as val_err:
            return Response({'error':val_err,'msg':"Plan is not valid"},status=status.HTTP_404_NOT_FOUND)
       
        try:
            operator_obj = Operator.objects.get(operator_name=operator)
        except ValueError as val_err:
            return Response({'error':val_err,'msg':"Operator is not valid"},status=status.HTTP_404_NOT_FOUND)
        
        try:
            circle_obj = AreaCircle.objects.get(area_name=circle)
        except ValueError as val_err:
            return Response({'error':val_err,'msg':"circle is not valid"},status=status.HTTP_404_NOT_FOUND)
            
        if mobile :
            recharge_obj = Recharge.objects.create(plan = plan_obj,mobile=mobile,operator=operator_obj,circle=circle_obj)
            recharge_obj.save()
            serializer = RechargeSerializer(recharge_obj)
            return Response({"success":"Recharge successfully","data":serializer.data}, status=status.HTTP_201_CREATED)
        else:
             return Response({"Somthing went wrong!"},status=status.HTTP_400_BAD_REQUEST)