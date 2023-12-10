from django.contrib import admin
from .models import Member
from .models import Post
from .models import Comment
from .models import Category



class MemberAdmin(admin.ModelAdmin):
    list_display = ("ID", "Username", "Email",)



class PostAdmin(admin.ModelAdmin):
    list_display = ("ID", "Title", "Content", "Category", "Date_Published")



class CommentAdmin(admin.ModelAdmin):
    list_display = ("ID", "PostID", "UserID", "Content", "Date_Posted")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("ID", "Name")

admin.site.register(Member,MemberAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category,CategoryAdmin)