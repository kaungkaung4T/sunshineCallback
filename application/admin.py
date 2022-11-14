from django.contrib import admin
from application.models import kbz, kbz_request

# Register your models here.

class kbz_admin(admin.ModelAdmin):
    list_display = ["notify_time","merch_code", "merch_order_id","mm_order_id","trans_currency","total_amount","trade_status","trans_end_time","callback_info","nonce_str","sign_type","appid","sign"]


class kbz_request_admin(admin.ModelAdmin):
    list_display = ["Request"]


admin.site.register(kbz, kbz_admin)
admin.site.register(kbz_request, kbz_request_admin)