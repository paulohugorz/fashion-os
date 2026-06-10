from sqlalchemy import Column, Integer, String, Float, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base


class Colecao(Base):
    __tablename__ = "colecoes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    descricao = Column(Text)
    status = Column(String, default="planejamento")
    criado_em = Column(DateTime(timezone=True), server_default=func.now())

    pecas = relationship("Peca", back_populates="colecao")


class Peca(Base):
    __tablename__ = "pecas"

    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String, unique=True, nullable=False, index=True)
    nome = Column(String, nullable=False)
    colecao_id = Column(Integer, ForeignKey("colecoes.id"))
    status = Column(String, default="ideia")
    prioridade = Column(String, default="media")
    tecido = Column(String)
    custo_estimado = Column(Float)
    preco_sugerido = Column(Float)
    observacoes = Column(Text)
    prompt_croqui = Column(Text)
    prompt_foto = Column(Text)
    criado_em = Column(DateTime(timezone=True), server_default=func.now())

    colecao = relationship("Colecao", back_populates="pecas")
    ficha_tecnica = relationship("FichaTecnica", back_populates="peca", uselist=False)


class FichaTecnica(Base):
    __tablename__ = "fichas_tecnicas"

    id = Column(Integer, primary_key=True, index=True)
    peca_id = Column(Integer, ForeignKey("pecas.id"), unique=True)
    descricao_tecnica = Column(Text)
    materiais = Column(Text)
    construcao = Column(Text)
    medidas = Column(Text)
    qualidade = Column(Text)
    criado_em = Column(DateTime(timezone=True), server_default=func.now())

    peca = relationship("Peca", back_populates="ficha_tecnica")
