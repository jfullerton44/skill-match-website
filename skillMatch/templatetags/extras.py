from django import template

register = template.Library()


@register.filter(name='common')
def common(user, other):
    count = 0
    for course in user.classes.all():
        if course in other.classes.all():
            count += 1
    return count


@register.filter(name='mutual')
def mutual(user, other):
    count = 0
    for friend in user.friends.all():
        if friend in other.friends.all():
            count += 1
    return count

