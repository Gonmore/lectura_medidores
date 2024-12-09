from django.core.exceptions import ValidationError

#Aqui los validadores personalizados
def validar_nombre(value):
    if len(value) < 5: 
        raise ValidationError(f'El nombre debe tener al menos 5 letras. Actual: {len(value)}')

def validar_metodo(value):
    allowed_values = ["serial", "tcp", "hdlc"] 
    if value.lower() not in allowed_values: 
        raise ValidationError(f'{value} no es un valor válido. Debe ser uno de: {", ".join(allowed_values)}')
