from django.contrib import admin
from main import models

admin.site.register(models.Users)
admin.site.register(models.Questions)
admin.site.register(models.Answers)
admin.site.register(models.Tags)
# admin.site.register(models.QuestTag)


                #   <!-- {% for tag in quest %}
                #   {%if q.question|stringformat:'s' == quest.question|stringformat:'s' %}
                #   <a href="#">{{q.tag}}</a>
                #   {% endif %}

                # {% endfor %}
                #   {% for q in q_t %}
                #     {%if q.question|stringformat:'s' == quest.question|stringformat:'s' %}
                #     <a href="#">{{q.tag}}</a>
                #     {% endif %}
                #   {% endfor %} -->