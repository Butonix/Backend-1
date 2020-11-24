from rest_framework import viewsets

from location import models, serializers


class CountryViewSet(viewsets.ModelViewSet):
    queryset = models.Country.objects.all()
    serializer_class = serializers.CountrySerializer
    # permission_classes = [permissions.IsAdminUser]


class ProvinceViewSet(viewsets.ModelViewSet):
    queryset = models.Province.objects.all()
    serializer_class = serializers.ProvinceSerializer
    # permission_classes = [permissions.IsAdminUser]


class DistrictViewSet(viewsets.ModelViewSet):
    queryset = models.District.objects.all()
    serializer_class = serializers.DistrictSerializer
    # permission_classes = [permissions.IsAdminUser]


class MunicipalityViewSet(viewsets.ModelViewSet):
    queryset = models.Municipality.objects.all()
    serializer_class = serializers.MunicipalitySerializer
    # permission_classes = [permissions.IsAdminUser]


class MunicipalityWardViewSet(viewsets.ModelViewSet):
    queryset = models.MunicipalityWard.objects.all()
    serializer_class = serializers.MunicipalityWardSerializer
    # permission_classes = [permissions.IsAdminUser]


class VDCViewSet(viewsets.ModelViewSet):
    queryset = models.VDC.objects.all()
    serializer_class = serializers.VDCSerializer
    # permission_classes = [permissions.IsAdminUser]


class VDCWardViewSet(viewsets.ModelViewSet):
    queryset = models.VDCWard.objects.all()
    serializer_class = serializers.VDCWardSerializer
    # permission_classes = [permissions.IsAdminUser]
