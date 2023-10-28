from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey

#Primeiro passo: antes de rodar esse código é criar o databse na sua máquina com o nome 'extendvision'
#Segundo passo: o db_uri é a rota do database no seu computador, caso seja diferente apenas mude a rota da váriavel
db_uri = "mysql://root:root@localhost/extendvision"
engine = create_engine(db_uri)

#Declaração das classes ligadas as tabelas do database
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    registration = Column(String(50), nullable=False)
    password = Column(String(8), nullable=False)
    name = Column(String(50), nullable=False)
    title = Column(String(50), nullable=False)
    gender = Column(String(30), nullable=False)
    birth_date = Column(Date, nullable=False)
    type = Column(String(50), nullable=False)

class Field(Base):
    __tablename__ = 'field'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    field = Column(String(50), nullable=False)

class Project(Base):
    __tablename__ = 'project'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_professor = Column(Integer, ForeignKey('users.id'), nullable=False)
    id_field = Column(Integer, ForeignKey('field.id'), nullable=False)
    title = Column(String(50), nullable=False)
    theme = Column(String(50), nullable=False)
    description = Column(String(50), nullable=False)
    begin_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    register_begin = Column(Date, nullable=False)
    register_end = Column(Date, nullable=False)
    workload = Column(Integer, nullable=False)
    available_spots = Column(Integer, nullable=False)
    scholarship = Column(Integer, nullable=False)
    
    professor = relationship('User', foreign_keys=[id_professor])
    field_rel = relationship('Field', foreign_keys=[id_field])

class ProjectStudents(Base):
    __tablename__ = 'project_students'
    
    id_project = Column(Integer, ForeignKey('project.id'), nullable=False, primary_key=True )
    id_user = Column(Integer, ForeignKey('users.id'), nullable=False, primary_key=True)
    
    project = relationship('Project', foreign_keys=[id_project])
    user = relationship('User', foreign_keys=[id_user])

Base.metadata.create_all(engine)
