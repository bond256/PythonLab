from django.db import models

class Link(models.Model):
    link_name = models.CharField(max_length=50,verbose_name='Название ссылки')
    success_text = models.CharField(max_length=100, verbose_name='Текст после перехода')
    counter = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return '{} [{}]'.format(self.link_name, self.counter)

    def add_visit(self):
        self.counter += 1
