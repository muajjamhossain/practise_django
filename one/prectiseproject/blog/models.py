from django.db import models

# class Category(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name


class Post(models.Model):
    cate_type = (
        ('National', 'National'),
        ('Politics', 'Politics'),
        ('Sports', 'Sports'),
    )

    title = models.CharField(max_length=200)
    content = models.TextField()
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=cate_type, default='Sports')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
