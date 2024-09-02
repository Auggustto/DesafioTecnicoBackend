from email_validator import validate_email, EmailUndeliverableError

def validation_cpf(cpf):
    
    if len(cpf)< 11 or len(cpf) > 11:
        return True
    
def validation_email(email):
    try:
        validate_email(email)
        return False
    except EmailUndeliverableError:
        return True