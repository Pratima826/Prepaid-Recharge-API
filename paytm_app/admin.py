from django.contrib import admin
from paytm_app.models import *
# Register your models here.

class OperatorAdmin(admin.ModelAdmin):
    list_display = ['id','operator_name']
admin.site.register(Operator,OperatorAdmin)

class AreaCircleAdmin(admin.ModelAdmin):
    list_display = ['id','area_name']
admin.site.register(AreaCircle,AreaCircleAdmin)


class CategoryPlanAdmin(admin.ModelAdmin):
    list_display = ['id','category_name']
admin.site.register(CategoryPlan,CategoryPlanAdmin)

class PlanAdmin(admin.ModelAdmin):
    list_display = ['id','plan_type','price','validity','operator','validity_type','data','data_type','description']
    fields = ['plan_type','price','validity','operator','validity_type','data','data_type','description']
admin.site.register(Plan,PlanAdmin)

class RechareAdmin(admin.ModelAdmin):
    list_display = ['id','mobile','operator','circle','plan','recharge_date']
admin.site.register(Recharge,RechareAdmin)
