from django.db import models

class Screen(models.Model):
        baron_timer = models.IntegerField(max_length=3, null=True)
        dragon_timer = models.IntegerField(max_length=3, null=True)

        top_blue_timer = models.IntegerField(max_length=3, null=True)
        top_red_timer = models.IntegerField(max_length=3, null=True)
        bottom_blue_timer = models.IntegerField(max_length=3, null=True)
        bottom_red_timer = models.IntegerField(max_length=3, null=True)

        top_inhib_tlane = models.IntegerField(max_length=3, null=True)
        top_inhib_mlane = models.IntegerField(max_length=3, null=True)
        top_inhib_blane = models.IntegerField(max_length=3, null=True)

        bottom_inhib_tlane = models.IntegerField(max_length=3, null=True)
        bottom_inhib_mlane = models.IntegerField(max_length=3, null=True)
        bottom_inhib_blane = models.IntegerField(max_length=3, null=True)
        
        wards = models.ForeignKey('Ward', null=True, blank=True, default=None)

class Ward(models.Model):
        position_x = models.IntegerField(max_length=3, null=True)
        position_y = models.IntegerField(max_length=3, null=True)
        team = models.BooleanField(default=True)           #True = Ours, False = Theirs
        timer = models.IntegerField(max_length=3, null=True)


        # ##Additional ones that could be included##
        # injured = BooleanField()
        # goals = models.IntegerField(max_length=2)
        # etc..