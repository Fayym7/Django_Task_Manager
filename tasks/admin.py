from django.contrib import admin
from .models import Task, OAuthKey, GoogleOAuthKey, UserInvitation
from django.core.mail import send_mail
from django.utils.html import format_html
from django.urls import reverse

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed', 'user', 'created_date')
    search_fields = ('title', 'description')


@admin.register(OAuthKey)
class OAuthKeyAdmin(admin.ModelAdmin):
    list_display = ('client_id', 'created_at')
    search_fields = ('client_id',)


@admin.register(GoogleOAuthKey)
class GoogleOAuthKeyAdmin(admin.ModelAdmin):
    list_display = ('name', 'client_id', 'created_at', 'updated_at')
    search_fields = ('name', 'client_id')


@admin.register(UserInvitation)
class UserInvitationAdmin(admin.ModelAdmin):
    list_display = ('email', 'token', 'is_used', 'created_at')
    actions = ['send_invitation_email']

    def send_invitation_email(self, request, queryset):
        for invitation in queryset:
            if not invitation.is_used:
                registration_url = request.build_absolute_uri(
                    reverse('register_with_token', args=[invitation.token])
                )
                send_mail(
                    "You're Invited to Join!",
                    f'Please use the following link to register: {registration_url}',
                    'admin@yourdomain.com',  # Replace with your email
                    [invitation.email],
                )
                self.message_user(request, f'Invitation sent to {invitation.email}')
            else:
                self.message_user(request, f'Invitation for {invitation.email} already used', level='warning')

    send_invitation_email.short_description = "Send invitation email"
