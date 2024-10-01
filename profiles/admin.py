from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from profiles.models import Profile


class ProfileInline(admin.StackedInline):
    """
    Inline admin for the Profile model, allowing profile data to be edited
    on the same page as the User model in the admin panel.
    """
    model = Profile
    can_delete = False


class CustomUserAdmin(UserAdmin):
    """
    Customizes the UserAdmin to include ProfileInline and display
    the user's role in the list view.
    """
    inlines = (ProfileInline,)
    list_display = ['username', 'email', 'is_staff', 'get_role']


    # Displays the 'role' field from the Profile model in the admin list view.
    def get_role(self, instance):
        return instance.profile.role
    get_role.short_description = 'Role'


# Unregister the default User admin and register the customized one.
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
