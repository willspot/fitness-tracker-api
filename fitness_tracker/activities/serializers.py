from rest_framework import serializers
import django_filters
from .models import Activity

class ActivityFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(field_name="date", lookup_expr='gte')
    end_date = django_filters.DateFilter(field_name="date", lookup_expr='lte')
    activity_type = django_filters.CharFilter(field_name="activity_type", lookup_expr='icontains')

    class Meta:
        model = Activity
        fields = ['start_date', 'end_date', 'activity_type']

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_class = ActivityFilter

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'user', 'activity_type', 'duration', 'distance', 'calories_burned', 'date']
        read_only_fields = ['user', 'date']  # Users can not change their date or activity
