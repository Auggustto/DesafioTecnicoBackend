from sqlalchemy import Integer, String, Column, Date, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.models.database.connect_database import Base

class Client(Base):
    __tablename__ = 'client'
    
    id = Column(Integer, primary_key=True)
    cpf = Column(String, unique=False)
    name = Column(String(40), nullable=False)
    email = Column(String(30), nullable=False)
    birthdate = Column(Date, nullable=False)
    gender = Column(String(10), nullable=False)
    monthlyIncome = Column(Float, nullable=False)
    id_client = Column(String, unique=True, nullable=False)
    
    plans = relationship("Plan", back_populates="client")
    rescues = relationship("Rescue", back_populates="client")
    
    
class Product(Base):
    __tablename__ = 'product'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    susep = Column(String, nullable=False)
    expirationDate = Column(Date, nullable=False)
    minValueInitialContribution = Column(Float, nullable=False)
    minValueExtraContribution = Column(Float, nullable=False)
    entryAge = Column(Integer, nullable=False)
    exitAge = Column(Integer, nullable=False)
    initialRescueWaitingPeriod = Column(Integer, nullable=False)
    timeBetweenRescues = Column(Integer, nullable=False)
    id_product = Column(String, nullable=False)
    
    plans = relationship("Plan", back_populates="product")
    


class Plan(Base):
    __tablename__ = 'plan'
    
    id = Column(Integer, primary_key=True, index=True)
    clientId = Column(Integer, ForeignKey('client.id'), nullable=False)  # Alterar para ForeignKey('client.id')
    productId = Column(Integer, ForeignKey('product.id'), nullable=False)  # Alterar para ForeignKey('product.id')
    contribution = Column(Float)
    contractingDate = Column(Date, nullable=False)
    retirementAge = Column(Integer, nullable=False)
    statusPlan = Column(Boolean, nullable=False)
    id_plan = Column(String, unique=True, nullable=False)
    
    client = relationship('Client', back_populates='plans')
    product = relationship('Product', back_populates='plans')
    extra_contributions = relationship('ExtraContribution', back_populates='plan')



class ExtraContribution(Base):
    __tablename__ = 'extra_contribution'
    
    id = Column(Integer, primary_key=True)
    clientId = Column(String, ForeignKey('client.id_client'), nullable=False)
    planId = Column(String, ForeignKey('plan.id_plan'), nullable=False)
    contributionValue = Column(Float, nullable=False)
    id_ExtraContribution = Column(String, nullable=False)
    
    plan = relationship('Plan', back_populates='extra_contributions')


class Rescue(Base):
    __tablename__ = 'rescue'
    
    id = Column(Integer, primary_key=True)
    planId = Column(String, ForeignKey('plan.id_plan'), nullable=False)
    clientId = Column(String, ForeignKey('client.id_client'), nullable=False)
    rescueValue = Column(Float, nullable=False)
    id_rescue = Column(String, nullable=False)
    
    client = relationship('Client', back_populates='rescues')
