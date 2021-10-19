from core.erros import ExceptionMessageBuilder
from users.models import User

class UserService:
  def verify_user(email):
    user = User.objects.db_manager('erp').filter(email = email)

    if user:
      raise ExceptionMessageBuilder(status_code=400, message={ 'error': 'Email já cadastrado' })