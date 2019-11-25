
from django.apps import apps
import json

Ad = apps.get_model('blog', 'Ad')

with open('ads.json') as f:
    x = json.load(f)

for key, value in x.items():
    print(key)
    print(value)
    values = value.split(';')
    is_ad_exists = Ad.objects.filter(ad_id=key).count() > 0
    if is_ad_exists:
        continue
    new_ad = Ad.objects.create(ad_image=values[5], ad_price=values[3], ad_category=values[2], ad_title=values[4], ad_id=key, ad_id_link=values[1])
    new_ad.save()
