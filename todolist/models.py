from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    todo = models.CharField(max_length=50, verbose_name='待办事项')
    flag = models.CharField(max_length=2, verbose_name='标记')
    # 没完成的flag=1
    priority = models.CharField(max_length=2, verbose_name='优先次序')
    pubtime = models.DateTimeField(auto_now_add=True, verbose_name='上传日期')

    def __str__(self):
        return u'%d %s %s' % (self.id, self.todo, self.flag)

    class Meta:
        ordering = ['priority', 'pubtime']



# CASCADE：删除作者信息一并删除作者名下的所有书的信息；级联删除。Django模拟SQL约束ON DELETE CASCADE的行为，并删除包含ForeignKey的对象。
# PROTECT：删除作者的信息时，采取保护机制，抛出错误：即不删除Books的内容；防止删除被引用的对象，通过引发 ProtectedError一个子类 django.db.IntegrityError。
# SET_NULL：只有当null=True才将关联的内容置空；设置ForeignKeynull; 这是唯一可能 null的True。
# SET_DEFAULT：设置为默认值；将ForeignKey其设置为其默认值; ForeignKey必须设置默认值 。
# SET( )：括号里可以是函数，设置为自己定义的东西；设置为ForeignKey传递给的值 SET()，或者如果传递了可调用对象，则调用它的结果。在大多数情况下，为了避免在导入models.py时执行查询，必须传递可调用对象：
# DO_NOTHING：字面的意思，啥也不干，你删除你的干我毛线关系
