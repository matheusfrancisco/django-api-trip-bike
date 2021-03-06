from rest_framework import generics

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from trip.serializers import TravelSerialization
from trip.models import Trip
from trip.decorators import validate_request_data
from trip_api.pagination import CustomPagination


class TravelView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Trip.objects.all()
    # Set is necessary be Authenticated to access class
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    serializer_class = TravelSerialization

    def get(self, request) -> Response:
        queryset = self.filter_queryset(
            self.get_queryset().filter(user=request.user)
        )
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            result = self.get_paginated_response(serializer.data)
            data = result.data
        else:
            serializer = self.get_serializer(queryset, many=True)
            data = serializer.data
        return Response(data)


class TripDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET details/:id/
    PUT details/:id/ {'classification': ..., 'rate': ...}
    """
    queryset = Trip.objects.all()
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            a_trip = self.queryset.get(pk=kwargs["pk"])
            return Response(TravelSerialization(a_trip).data)
        except Trip.DoesNotExist:
            return Response(
                data={
                    "message": f"Trip with id: {kwargs['pk']} does not exist"
                },
                status=status.HTTP_404_NOT_FOUND
            )

    @validate_request_data
    def put(self, request, *args, **kwargs):
        try:
            a_trip = self.queryset.get(pk=kwargs["pk"])
            serializer = TravelSerialization()
            updated_trip = serializer.update(a_trip, request.data)
            return Response(TravelSerialization(updated_trip).data)
        except Trip.DoesNotExist:
            return Response(
                data={
                    "message": f"Trip with id: {kwargs['pk']} does not exist"
                },
                status=status.HTTP_404_NOT_FOUND
            )
