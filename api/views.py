from rest_framework import generics
from rest_framework.response import Response
from .models import HealthData
from .serializers import HealthDataSerializer
from .predict import predict_health_risk

class HealthDataListCreate(generics.ListCreateAPIView):
    queryset = HealthData.objects.all()
    serializer_class = HealthDataSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Get the saved instance
        instance = serializer.instance
        # Predict health risk
        risk = predict_health_risk(instance.heart_rate, instance.sleep_hours)
        # Add the prediction to the response
        response_data = serializer.data
        response_data['health_risk'] = risk

        return Response(response_data, status=201)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        # Add health risk prediction to each item
        response_data = serializer.data
        for item in response_data:
            risk = predict_health_risk(item['heart_rate'], item['sleep_hours'])
            item['health_risk'] = risk
        return Response(response_data)