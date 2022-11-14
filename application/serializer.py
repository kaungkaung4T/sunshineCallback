from rest_framework import serializers
from application.models import kbz, kbz_request
import copy

class kbzSerializer(serializers.ModelSerializer):
    class Meta:
        model = kbz
        fields = ["appid" ,"notify_time" ,"merch_code", "merch_order_id" ,"mm_order_id" ,"trans_currency"
                  ,"total_amount" ,"trade_status" ,"trans_end_time" ,"callback_info" ,"nonce_str" ,"sign_type" ,"appid"
                  ,"sign"]


class kbzRequestSerializer(serializers.ModelSerializer):
    Request = kbzSerializer()
    class Meta:
        model = kbz_request
        fields = ["Request"]

    def create(self, validated_data):
        validated_data_old = copy.deepcopy(validated_data)

        request = validated_data.pop('Request')

        kbz_obj= kbz.objects.create(**request)

        kbz_request.objects.create(Request=kbz_obj)

        return validated_data_old