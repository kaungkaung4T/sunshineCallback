from django.db import models

# Create your models here.
class kbz(models.Model):
    notify_time = models.CharField(max_length=255, blank=True, null=True)
    merch_code = models.CharField(max_length=255, blank=True, null=True)
    merch_order_id = models.CharField(max_length=255, blank=True, null=True)
    mm_order_id = models.CharField(max_length=255, blank=True, null=True)
    trans_currency = models.CharField(max_length=255, blank=True, null=True)
    total_amount = models.CharField(max_length=255, blank=True, null=True)
    trade_status = models.CharField(max_length=255, blank=True, null=True)
    trans_end_time = models.CharField(max_length=255, blank=True, null=True)
    callback_info = models.CharField(max_length=255, blank=True, null=True)
    nonce_str = models.CharField(max_length=255, blank=True, null=True)
    sign_type = models.CharField(max_length=255, blank=True, null=True)
    appid = models.CharField(max_length=40, blank=True, null=True)
    sign = models.CharField(max_length=255, blank=True, null=True)


class kbz_request(models.Model):
    Request = models.ForeignKey(kbz, on_delete=models.CASCADE, default=None, null=True)