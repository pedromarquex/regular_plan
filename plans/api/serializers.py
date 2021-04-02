from rest_framework.serializers import ModelSerializer

from plans.models import Plan


class PlanSerializer(ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'
