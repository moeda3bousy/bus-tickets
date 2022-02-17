from django.db import models
from creditcards.models import CardNumberField , CardExpiryField , SecurityCodeField
import datetime
#from django.utils.translation import ugettext_lazy as _
#from django.db.models.signals import post_save
class Ride(models.Model):
  destination = [
  ('Cairo','Cairo'),]
  destination2 = [
  ('Aswan','Aswan'),
  ('Alexandria','Alexandria'),
  ('Hurghada','Hurghada'),
   ('North coast','North coast'),
  ('Dahab','Dahab'),
  ('Sharm El-Sheikh','Sharm El-Sheikh'),
  ]
  from1 = models.CharField( max_length=20 ,verbose_name=("From"),choices=destination,null='True')
  to = models.CharField( max_length=20 ,verbose_name=("To"),choices=destination2,null='True')
  date = models.DateField(verbose_name=("Date"),default=datetime.datetime.now,) 
  time = models.TimeField(verbose_name=("Time"),default=datetime.datetime.now)
  number= models.IntegerField(null='True',verbose_name=("Receipt Number"))
  Active= models.BooleanField(null='true', default='False')
  Seats= models.IntegerField(default='0')
  card_number = CardNumberField(max_length=19, verbose_name=("Card Number"),null=True,blank=True)
  expiry_date = CardExpiryField(verbose_name=("Expiry Date"),null='True')
  security_code = SecurityCodeField(verbose_name=("Security Code"),null='True')
  
  class Meta:
        verbose_name = ("Ride")
        verbose_name_plural = ("Rides")
  def __str__(self):
        return self.to
  
class Available(models.Model):
   destination1 = [
   ('Cairo','Cairo'),]
   destination3 = [
  ('Aswan','Aswan'),
  ('Alexandria','Alexandria'),
  ('Hurghada','Hurghada'),
   ('North coast','North coast'),
  ('Dahab','Dahab'),
  ('Sharm El-Sheikh','Sharm El-Sheikh'),
  ]
   image = models.ImageField(upload_to='photos',null=True,blank=True)
   from2 = models.CharField( max_length=20 ,verbose_name=("from "),choices=destination1,null='True')
   to2 = models.CharField( max_length=20 ,verbose_name=("to "),choices=destination3,null='True')
   Price = models.IntegerField(null=True)
   date2 = models.DateField(verbose_name=("Date"),default=datetime.datetime.now)
   time2 = models.TimeField(verbose_name=("Time"),default=datetime.datetime.now)
  
   class Meta:
          verbose_name = ("available")
          verbose_name_plural = ("availables")
  
   def __str__(self):
          return self.to2
    
class Thanks(models.Model):
      image = models.ImageField(upload_to='photos',null=True,blank=True)
      def __str__(self):
          return self.image
      
      
