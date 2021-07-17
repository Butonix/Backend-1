from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name


class Province(models.Model):
    name = models.CharField(max_length=255, unique=True)
    number = models.IntegerField(
        unique=True, validators=[MaxValueValidator(100), MinValueValidator(1)]
    )
    country = models.ForeignKey(
        "Country", on_delete=models.CASCADE, related_name="provinces"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-updated_at']
        verbose_name_plural = "Provinces"


class District(models.Model):
    name = models.CharField(max_length=255, unique=True)
    province = models.ForeignKey(
        "Province", on_delete=models.CASCADE, related_name="districts"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Municipality(models.Model):
    name = models.CharField(max_length=255, unique=False)
    district = models.ForeignKey(
        "District", on_delete=models.CASCADE, related_name="municipalities"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']
        verbose_name_plural = "Municipalities"
        unique_together = [["name", "district"]]

    def __str__(self):
        return self.name


class VDC(models.Model):
    name = models.CharField(max_length=255, unique=False)
    district = models.ForeignKey(
        "District", on_delete=models.CASCADE, related_name="vdcs"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']
        verbose_name_plural = "VDCs"
        unique_together = [["name", "district"]]

    def __str__(self):
        return self.name


class VDCWard(models.Model):
    name = models.CharField(max_length=255, unique=False)
    number = models.IntegerField(
        validators=[MaxValueValidator(60), MinValueValidator(1)]
    )
    vdc = models.ForeignKey("VDC", on_delete=models.CASCADE, related_name="vdc_wards")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']
        verbose_name_plural = "VDC Wards"
        unique_together = [["name", "vdc", "number"]]

    def __str__(self):
        return self.name


class MunicipalityWard(models.Model):
    name = models.CharField(max_length=255)
    number = models.IntegerField(
        validators=[MaxValueValidator(60), MinValueValidator(1)]
    )
    municipality = models.ForeignKey(
        "Municipality", on_delete=models.CASCADE, related_name="municipality_wards"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']
        verbose_name_plural = "Municipality Wards"
        unique_together = ["name", "municipality", "number"]

    def __str__(self):
        return self.name
