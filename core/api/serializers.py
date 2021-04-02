from rest_framework.serializers import ModelSerializer

from core.models import RegularPlan


class RegularPlanSerializer(ModelSerializer):
    class Meta:
        model = RegularPlan
        fields = '__all__'
