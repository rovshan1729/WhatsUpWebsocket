from django.contrib import admin
from  .models import Message, ChatRoom


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('message',)

@admin.register(ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ('name',)