from appointment.models import Appointment
from appointment.serializers import AppointmentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from hospital_management.email import send_email_to_client


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    def list(self, request, *args, **kwargs):
        data = list(Appointment.objects.all().values())
        return Response(
            {
                'status': status.HTTP_200_OK,
                'message': "Appointments Data Retrieved Successfully",
                'data': data
            },
        )

    def retrieve(self, request, *args, **kwargs):
            data = list(Appointment.objects.filter(appointment_id = kwargs['pk']).values())
            return Response(
                {
                    'status': status.HTTP_200_OK,
                    'message': "Appointment Data Retrieved Successfully",
                    'data': data
                },
            )
    
    def create(self, request, *args, **kwargs):
        product_serializer_data = AppointmentSerializer(data = request.data)
        product_serializer_data.is_valid(raise_exception = True)
        product_serializer_data.save()
        send_email_to_client(request.data)
        print(request.data)

        return Response(
            {
                'status': status.HTTP_201_CREATED,
                'message': 'Appointment Booked Successfully'
            },
        )
    
    def destroy(self, request, *args, **kwargs):
        product_data = Appointment.objects.filter(appintment_id = kwargs['pk'])
        if product_data:
            product_data.delete()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Product delete Sucessfully", "status": status_code})
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "Product data not found", "status": status_code})

    def update(self, request, *args, **kwargs):
        product_details = Appointment.objects.get(appointment_id = kwargs['pk'])
        product_serializer_data = AppointmentSerializer(product_details, data=request.data, partial=True)
        product_serializer_data.is_valid(raise_exception = True)
        product_serializer_data.save()
        status_code = status.HTTP_201_CREATED
        return Response({"message": "Product Update Sucessfully", "status": status_code})
        