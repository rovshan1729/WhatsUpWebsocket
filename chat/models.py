from django.db import models 
from utils.models import BaseModel
from django.contrib.auth import get_user_model

User = get_user_model()

class ChatRoom(BaseModel):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    

class Message(BaseModel):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)

    message = models.TextField()

    def __str__(self):
        return self.message
    


