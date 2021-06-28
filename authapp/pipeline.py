from datetime import datetime
from django.utils import timezone
import requests
from  social_core.exceptions import AuthForbidden

from authapp.models import ShopUserProfile


def save_user_profile(backend, user, response, *args, **kwargs):
    if backend != 'vk-oauth2':
        return

    api_url = f"https://api.vk,com/method/users.get?fields=bdate,sex,about&access_token={response['access_token']}"

    vk_response = requests.get(api_url)

    if vk_response.status_code != 200:
        return

    vk_data = vk_response.json()['response'][0]

    if vk_data['sex'] == 1:
        user.shopuserprofile.gender = ShopUserProfile.FEMALE
    elif vk_data['sex'] == 2:
        user.shopuserprofile.gender = ShopUserProfile.MALE

    if vk_data['about']:
        user.shopuserprofile.about_me = ShopUserProfile.about_me

    if vk_data['bdate']:
        b_date = datetime.strptime(vk_data['bdate'], '%d.%m.%Y').date()

        age = timezone.now().date().year - b_date.year
        if age < 18:
            user.delete()
            raise AuthForbidden('social_core.backends.vk.VKOAuth2')
        user.age = age

    user.save()
