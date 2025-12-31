from django.db import models
from django.contrib.auth.models import User
# from PIL import Image
# from django.urls import reverse
from cloudinary.models import CloudinaryField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = CloudinaryField(
        'image')

    def __str__(self):
        return f'{self.user.username} Profile'

    # ✅ မှန်ကန်တဲ့ save method
    # def save(self, *args, **kwargs):
    #     # အရင်ဆုံး save လုပ်ပါ
    #     super().save(*args, **kwargs)
    #
    #     # Image resize လုပ်တာ (ဖိုင်ရှိမှသာ)
    #     try:
    #         if self.image and hasattr(self.image, 'path'):
    #             img = Image.open(self.image.path)
    #             if img.height > 300 or img.width > 300:
    #                 output_size = (300, 300)
    #                 img.thumbnail(output_size)
    #                 img.save(self.image.path)
    #     except (FileNotFoundError, IOError, AttributeError):
    #         # ဖိုင်မတွေ့ရင် pass
    #         pass

    # def save(self, *args, **kwargs):
    #     img = Image.open(self.image.path)
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
    #     super().save()

    # def get_absolute_url(self):
    #     return reverse('post-detail', kwargs={'pk': self.pk})

