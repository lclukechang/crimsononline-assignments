from polls.models import Poll, Choice
from django.contrib import admin

class ChoiceInLine(admin.TabularInline):
  model = Choice
  extra = 3

class PollAdmin(admin.ModelAdmin):
  list_display = ('question','pub_date', 'was_published_recently')
  fieldsets = [
  (None,{'fields':['pub_date']}), 
  ('Date Information', {'fields':['question'], 'classes': ['collapse']}),
  ]
  inlines= [ChoiceInLine]
  list_filter = ['pub_date']
  search_fields = ['question']
  date_hierarchy = 'pub_date'


admin.site.register(Poll, PollAdmin)
