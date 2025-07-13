from django import template

register = template.Library()   # «Реестр» всех кастомных плюшек


@register.filter(name='addclass')  # <-- имя фильтра
def addclass(field, css):
    """
    Возвращает HTML инпут с доп. атрибутом class.

    Пример в шаблоне:
        {{ field|addclass:'form-control' }}
    """
    return field.as_widget(attrs={'class': css})
