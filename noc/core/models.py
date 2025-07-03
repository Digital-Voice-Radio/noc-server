from django.db import models

# Create your models here.

class ModeChoices(models.TextChoices):
    DMR = "DMR", "DMR"
    M17 = "M17", "M17"
    YSF = "YSF", "YSF"
    DST = "DST", "D-Star"
    ALL = "ALL", "AllStar"
    ECL = "ECL", "Echolink"
    IRL = "IRL", "IRLP"


class Server(models.Model):

    network_id = models.IntegerField()

    name = models.CharField(max_length=32)

    server_name = models.CharField(max_length=32, blank=True, null=True, default=None)
    hostname = models.CharField(max_length=84, blank=True, null=True, default=None)

    hotspot_port = models.IntegerField(blank=True, null=True, default=True)
    hotspot_pwd = models.CharField(max_length=18, blank=True, null=True, default=True)

    hotspot_allow = models.BooleanField(default=True)
    listed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Owner(models.Model):

    shortname = models.CharField(max_length=8)
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.shortname



class Talkgroup(models.Model):

    tgid = models.IntegerField()
    name = models.CharField(max_length=32)
    owner = models.ForeignKey(Owner, on_delete=models.SET_NULL, blank=True, null=True, default=None)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.tgid}'



class Bridge(models.Model):

    talkgroup = models.ForeignKey(Talkgroup, on_delete=models.CASCADE)

    mode = models.CharField(max_length=3, choices=ModeChoices)

    network = models.CharField(max_length=18, blank=True, null=True, default=None)
    target = models.CharField(max_length=12)

    description = models.CharField(max_length=64, blank=True, null=True, default=None)
    public = models.BooleanField(default=True)

    operator = models.ForeignKey(Owner, on_delete=models.SET_NULL, blank=True, null=True, default=None)


