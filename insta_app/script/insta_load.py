import instaloader


class InstaloaderUser:

    def __init__(self, user, L = instaloader.Instaloader()):
        self.user = instaloader.Profile.from_username(L.context, user)

    def get_username(self):
        return self.user

    def get_privated (self):
        return self.user.is_private

    def get_data_profile(self, L = instaloader.Instaloader()):
        #L.download_profile(self.user.username, profile_pic_only=True)
        data = {
            'username' : self.user.username,
            'biography' : self.user.biography,
            'full_name' : self.user.full_name,
            'followers' : self.user.followers,
            'external_url' : self.user.external_url,
            'profile_pic_url' : self.user.profile_pic_url,
            'mediacount' : self.user.mediacount,
            'igtvcount' : self.user.igtvcount,
            'post' : self.user.get_posts(),

        }
        return data
