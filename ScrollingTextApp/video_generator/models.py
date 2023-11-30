from django.db import models
from django.core.validators import validate_comma_separated_integer_list

class Prompt(models.Model):
    """Model of a user's prompt"""
    STR_MAX_LEN = 20

    prompt_id = models.AutoField(primary_key=True)
    text = models.TextField(help_text="User's input")
    font_size = models.IntegerField(help_text='Font size')
    duration = models.IntegerField(help_text='In seconds')
    direction = models.CharField(max_length=5, help_text='Can be "left" or "right"')

    frame_size = models.CharField(validators=[validate_comma_separated_integer_list],
                                  max_length=10, help_text='In pixels')

    background_color = models.CharField(validators=[validate_comma_separated_integer_list],
                                        max_length=15, help_text='In rgb')

    text_color = models.CharField(validators=[validate_comma_separated_integer_list],
                                  max_length=15, help_text='In rgb')


    def __str__(self):
        if len(self.text) > self.STR_MAX_LEN:
            return f'{self.prompt_id}. {self.text[:self.STR_MAX_LEN]}...'
        else:
            return f'{self.prompt_id}. {self.text}'
