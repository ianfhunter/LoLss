from django.db import models

class Screen(models.Model):
        page_id = models.CharField(max_length=5,default='')

        baron_timer = models.IntegerField(max_length=3, null=True,default=0)
        dragon_timer = models.IntegerField(max_length=3, null=True,default=0)

        top_blue_timer = models.IntegerField(max_length=3, null=True,default=0)
        top_red_timer = models.IntegerField(max_length=3, null=True,default=0)
        bottom_blue_timer = models.IntegerField(max_length=3, null=True,default=0)
        bottom_red_timer = models.IntegerField(max_length=3, null=True,default=0)

        top_inhib_tlane = models.IntegerField(max_length=3, null=True,default=0)
        top_inhib_mlane = models.IntegerField(max_length=3, null=True,default=0)
        top_inhib_blane = models.IntegerField(max_length=3, null=True,default=0)

        bottom_inhib_tlane = models.IntegerField(max_length=3, null=True,default=0)
        bottom_inhib_mlane = models.IntegerField(max_length=3, null=True,default=0)
        bottom_inhib_blane = models.IntegerField(max_length=3, null=True,default=0)
        
        drawing = models.CharField(max_length=30000,default='')    #30KB MAX

class Ward(models.Model):
        position_x = models.IntegerField(max_length=3, null=True)
        position_y = models.IntegerField(max_length=3, null=True)
        team = models.BooleanField(default=True)           #True = Ours, False = Theirs
        timer = models.IntegerField(max_length=3, null=True)
        screen = models.ForeignKey('Screen', null=True, blank=True, default=None)


        # ##Additional ones that could be included##
        # injured = BooleanField()
        # goals = models.IntegerField(max_length=2)
        # etc..