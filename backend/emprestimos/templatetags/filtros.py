from django import template


register = template.Library()

@register.filter(name="duracao")
def duracao(valor1, valor2):
    return (valor1 - valor2).days