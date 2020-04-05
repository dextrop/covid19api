from django.db import models

class Scrapping(models.Model):
    id = models.AutoField(primary_key=True)
    data         = models.CharField(max_length=5000, default="")
    updated         = models.DateTimeField(auto_now=True)


    def is_authenticated(self):
        """
        Always return True. This is a way to tell if the user has been
        authenticated in templates.
        """
        return True

    def save(self, *args, **kwargs):
        return super(Scrapping, self).save(*args, **kwargs)

    def __unicode__(self):
        return str(self.id)

    class Meta:
        db_table = 'scrapping'
        app_label = 'src'