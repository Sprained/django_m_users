from core.erros import ExceptionMessageBuilder
from users.models import User

class UserService:
  def verify_user(self, email):
    user = User.objects.db_manager('erp').filter(email = email)

    if user:
      raise ExceptionMessageBuilder(status_code=400, message={ 'error': 'Email já cadastrado' })

  def exist_user(self, id):
    user = User.objects.db_manager('erp').filter(id = id).get()

    if not user:
      raise ExceptionMessageBuilder(status_code=404, message={ 'error': 'Usuário não encontrado' })
    return user
