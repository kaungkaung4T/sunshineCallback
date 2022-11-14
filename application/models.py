from django.db import models

# Create your models here.
class kbz(models.Model):
    notify_time = models.CharField(max_length=255)
    merch_code = models.CharField(max_length=255)
    merch_order_id = models.CharField(max_length=255)
    mm_order_id = models.CharField(max_length=255)
    trans_currency = models.CharField(max_length=255)
    total_amount = models.CharField(max_length=255)
    trade_status = models.CharField(max_length=255)
    trans_end_time = models.CharField(max_length=255)
    callback_info = models.CharField(max_length=255)
    nonce_str = models.CharField(max_length=255)
    sign_type = models.CharField(max_length=255)
    appid = models.CharField(max_length=40)
    sign = models.CharField(max_length=255)


class kbz_request(models.Model):
    Request = models.ForeignKey(kbz, on_delete=models.CASCADE, default=None, null=True)