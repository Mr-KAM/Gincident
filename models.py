from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float, Enum, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Referents(Base):
    __tablename__ = 'referents'
    id = Column(Integer, primary_key=True)
    nom = Column(String, nullable=False)
    prenom = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    telephone = Column(String)
    mot_de_passe = Column(String, nullable=False)
    role = Column(Enum('admin', 'user', name='role_enum'), nullable=False, default='user')

class Incidents(Base):
    __tablename__ = 'incidents'
    id = Column(Integer, primary_key=True)
    type_incident = Column(String, nullable=False)
    date_incident = Column(Date, nullable=False)
    niveau_risque = Column(Integer, nullable=False)
    localisation = Column(String)
    resume = Column(String)
    identifie_par = Column(Integer, ForeignKey('referents.id'))

class Actions(Base):
    __tablename__ = 'actions'
    id = Column(Integer, primary_key=True)
    intitule = Column(String, nullable=False)
    responsable_referent = Column(Integer, ForeignKey('referents.id'))
    date_creation = Column(Date, nullable=False)
    date_limite = Column(Date, nullable=False)
    etat = Column(Enum('Neutre', 'Urgent', name='etat_enum'), default='Neutre')
    incident_id = Column(Integer, ForeignKey('incidents.id'))

# Database setup
DATABASE_URL = "sqlite:///app.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base.metadata.create_all(bind=engine)
