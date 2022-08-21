from rest_framework import serializers
from customer.models import Customer

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = [
            'id',
            'fullname',
            'email',
            'national_no',
            'address',
            'created_at',
            'updated_at'
        ]