from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from .models import *

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class Applicationserializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'

class Companyserializer(serializers.ModelSerializer):
    class Meta:
        model = Companys
        fields = '__all__'

    #this is for user 
@api_view(['GET'])
def getuserdets(request):
    user_dets = User.objects.all()
    serializer = Userserializer(user_dets, many=True)
    return Response(serializer.data)
    
@api_view(["POST"])
def inputuserdata(request):
    data = request.data
    serializer = Userserializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                "message": "Item added successfully!"
            }
        )
    return Response(serializer.errors, status=400)

@api_view(["DELETE"])
def deleteuserdata(request, id):
    userdata = User.objects.get(id=id)
    userdata.delete()
    return Response(
        {
            "message": "user successfully deleted"
        }
    )

@api_view(["PUT"])
def updateuserdata(request, id):
    try:
        userdata = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=404)

    serializer = Userserializer(instance=userdata, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Item updated successfully!"})
    return Response(serializer.errors, status=400)



#user program end

#application begins
@api_view(['GET'])
def getapplication(request):
    application = Application.objects.all()
    serializer = Applicationserializer(application, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def inputapplication(request):
    data = request.data
    serializer = Applicationserializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                "message": "Item added successfully!"
            }
        )
    return Response(serializer.errors, status=400)

@api_view(["DELETE"])
def delete_application(request, id):
    try:
        application = Application.objects.get(id=id)
        application.delete()
        return Response({
            "message": "Application successfully deleted",
            "note": "Deleting an application may reduce your rating"
        })
    except Application.DoesNotExist:
        return Response({"error": "Application not found"}, status=404)


@api_view(["PUT"])
def updateapplication(request, id):
    application = Application.objects.get(id=id)
    serializer = Applicationserializer(instance=application, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                "message": "Item updated successfully!"
            }
        )
    return Response(serializer.errors, status=400)

from rest_framework.viewsets import ModelViewSet

class bookviewset(ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = Applicationserializer