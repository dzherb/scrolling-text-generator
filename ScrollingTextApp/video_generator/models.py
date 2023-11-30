from django.db import models

class Prompt(models.Model):
    prompt_id = models.AutoField(primary_key=True)
    text = models.TextField(help_text="User's input")
    def __str__(self):
        if len(self.text) > 10:
            return f'{self.prompt_id}. {self.text[:10]}...'
        else:
            return f'{self.prompt_id}. {self.text}'
