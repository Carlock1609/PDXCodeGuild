# TESTING ALLAUTH QUERYING EXTRA_DATA

# from allauth.account.signals import user_signed_up
# from users.models import UserProfile


# @receiver(user_signed_up)
# def retrieve_social_data(request, user, **kwargs):
#     """Signal, that gets extra data from sociallogin and put it to profile."""
#     # get the profile where i want to store the extra_data
#     profile = UserProfile(user=user)
#     # in this signal I can retrieve the obj from SocialAccount
#     data = SocialAccount.objects.filter(user=user, provider='twitter')
#     # check if the user has signed up via social media
#     if data:
#         followers = data[0].get_avatar_url()
#         if picture:
#             # custom def to save the pic in the profile
#             save_image_from_url(model=profile, url=picture)
#         profile.save()