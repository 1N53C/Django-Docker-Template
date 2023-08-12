# /models/cve.py

from django.db import models


class Cve(models.Model):
    vendor = models.CharField(max_length=50)
    product = models.CharField(max_length=50)
    version_num = models.CharField(max_length=50)
    cve_id = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    cvss_score = models.CharField(max_length=50, blank=True, null=True)
    access_vector = models.CharField(max_length=50, blank=True, null=True)
    confidentiality_impact = models.CharField(max_length=50, blank=True, null=True)
    integrity_impact = models.CharField(max_length=50, blank=True, null=True)
    availability_impact = models.CharField(max_length=50, blank=True, null=True)
    base_severity = models.CharField(max_length=50, blank=True, null=True)
