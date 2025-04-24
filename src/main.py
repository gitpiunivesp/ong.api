from flask import Flask
from flask_cors import CORS

from src.models.empresa import Empresa
from src.models.usuario import Usuario
from src.models.colaborador import Colaborador
from src.models.animal import Animal
from src.models.interessado import Interessado
from src.models.tutor import Tutor
from src.models.agendamento import Agendamento

from src.blueprints.empresas_bp import empresa_bp
from src.blueprints.usuarios_bp import usuario_bp
from src.blueprints.colaboradores_bp import colaborador_bp
from src.blueprints.animais_bp import animal_bp
from src.blueprints.interessados_bp import interessado_bp
from src.blueprints.tutores_bp import tutor_bp
from src.blueprints.agendamentos_bp import agendamento_bp
from src.blueprints.auth_bp import auth_bp
from src.blueprints.relatorios_bp import relatorio_bp

from src.database import db

app = Flask(__name__)
CORS(app)

with app.app_context():
    if not db.is_connection_usable():
        db.connect()
    db.create_tables([Empresa, Usuario, Colaborador, Animal, Interessado, Tutor, Agendamento])

@app.teardown_appcontext
def close_db(exception=None):
    if db.is_connection_usable():
        db.close()

app.register_blueprint(empresa_bp)
app.register_blueprint(usuario_bp)
app.register_blueprint(colaborador_bp)
app.register_blueprint(animal_bp)
app.register_blueprint(interessado_bp)
app.register_blueprint(tutor_bp)
app.register_blueprint(agendamento_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(relatorio_bp)
