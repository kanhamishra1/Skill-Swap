from django.contrib import admin # Django’s admin module.
from django.contrib.auth.admin import UserAdmin  # Base admin class for Django’s default User model.
from .models import CustomUser  # Your custom user model (probably using AbstractBaseUser or AbstractUser).
from django.utils.translation import gettext_lazy as _  #Used for translation (for example, field section titles like "Personal info").

class CustomUserAdmin(UserAdmin): #customizing Django's admin to display my CustomUser fields in a cleaner way.
    model = CustomUser  # i am telling Django that this admin is for your CustomUser model
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')  #Adds filtering options (right side in Django admin) to easily find staff or active users.

    # search bar for finding users by name or email
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

    # Defines how fields are grouped on the user detail/edit page in Django admin

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )




#  This controls the layout when you add a new user via the admin panel.

    add_fieldsets = (
        (None, {
            'classes': ('wide',), #'wide' is a CSS class that makes the form stretch nicely in the admin UI.


            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
 #Registers your model with the Django admin so it appears there with your custom configuration
admin.site.register(CustomUser, CustomUserAdmin)
