from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class Usuario(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(20)) # 'jovem' ou 'tio'

    # --- DADOS COMUNS (JOVENS E TIOS) ---
    nome = db.Column(db.String(100))
    data_nascimento = db.Column(db.String(20))
    idade = db.Column(db.Integer)
    telefone = db.Column(db.String(20))
    endereco = db.Column(db.String(200))
    lideranca_atual = db.Column(db.String(200)) # Já serviu em cargo de liderança?
    vontade_lideranca = db.Column(db.String(10)) # Tem vontade de servir?
    toca_instrumento = db.Column(db.String(100)) # Toca algum instrumento?
    canta = db.Column(db.String(10)) # Você canta?
    quer_dar_palestra = db.Column(db.String(10)) # Gostaria de dar palestra?
    alergias = db.Column(db.Text) # Tem alergias?

    # --- CAMPOS EXCLUSIVOS: JOVENS ---
    ano_fez_segueme = db.Column(db.String(10))
    qual_segueme_fez = db.Column(db.String(100))
    onde_ja_trabalhou = db.Column(db.Text) # Qual segue me já trabalho? Os anos?
    equipes_que_trabalhou = db.Column(db.Text) # Qual equipe já trabalhou?
    ultima_equipe = db.Column(db.String(100)) # A última equipe que serviu?

    # --- CAMPOS EXCLUSIVOS: TIOS (CASADOS) ---
    nome_conjuge = db.Column(db.String(100))
    idade_conjuge = db.Column(db.Integer)
    endereco_conjuge = db.Column(db.String(200))
    telefone_conjuge = db.Column(db.String(20))
    tem_filhos = db.Column(db.String(10))
    qtd_filhos = db.Column(db.Integer)
    equipes_tios = db.Column(db.Text) # As equipes que trabalhou
    fez_ecc_ou_segueme = db.Column(db.String(100)) # Fez Ecc ou Segueme?
    meio_transporte = db.Column(db.String(100)) # Tem meio de transporte? Qual?