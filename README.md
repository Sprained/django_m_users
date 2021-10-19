Simples projeto para aplicar os principais conceitos do Django.

**Criando o ambiente virtual**
* Instalar o venv  
  `$ pip install virtualenv`  
  
* Iniciar o venv  
  `$ virtualenv venv`  
  `$ source venv/bin/activate`  

**Preparando o ambiente virtual**  
* Instalar os requisitos do projeto  
  `$ pip install -r requirements.txt`
 
**.env**    
- Basta criar um arquivo `.env` na raiz do projeto e preencher com:  
-   ENGINE = ''
    DATABASE = ''
    USER_DATABASE = ''
    PASS = ''
    HOST = ''
    PORT = ''

**Para criar super user para acessar o portal admin**
- `python manage.py createsuperuser`

**Por ultimo, rodar sempre que der pull ou mudar algo nos models**  
- `$ python manage.py makemigrations`  
- `$ python manage.py migrate`

**Para adicionar uma nova dependencia, rode:**
- `pip install <-dependency->`
- `pip freeze >> requirements.txt`