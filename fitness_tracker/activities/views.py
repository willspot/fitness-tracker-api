from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Activity
from .serializers import ActivitySerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Ensure users can only access their own activities.
        """
        return Activity.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically assign the user to the activity when created
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'])
    def summary(self, request):
        """
        Provide a summary of activities (total duration, distance, and calories).
        """
        activities = self.get_queryset()
        total_duration = sum([activity.duration for activity in activities])
        total_distance = sum([activity.distance for activity in activities])
        total_calories = sum([activity.calories_burned for activity in activities])

        return Response({
            'total_duration': total_duration,
            'total_distance': total_distance,
            'total_calories': total_calories,
        })
