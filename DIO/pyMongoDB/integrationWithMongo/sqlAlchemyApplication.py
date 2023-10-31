import sqlalchemy
from sqlalchemy import Column, inspect, select
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy.orm import relationship
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

Base = declarative_base()


class User(Base):
    __tablename__ = "user_account"
    #atributos
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)

    address = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, fullname={self.fullname})"

class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    email_address = Column(String(30), nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)

    user = relationship("User", back_populates="address")

    def __repr__(self):
        return f"Address(id={self.id}, email_address={self.email_address})"


print(User.__tablename__)
print(Address.__tablename__)

# conexao com o banco de dados
engine = create_engine("sqlite://")

# criando as classes como tabelas no banco de dados
Base.metadata.create_all(engine)

# depreciado - será removido em futuro release
# print(engine.table_names())

# investiga o esquema do banco de dados
inspetor_engine = inspect(engine)
print(inspetor_engine.has_table("user_account"))
print(inspetor_engine.get_table_names())
print(inspetor_engine.default_schema_name)

with Session(engine) as session:
    juliana = User(
        name='juliana',
        fullname='juliana mascarenhas',
        address=[Address(email_address='julianam@email.com')]
    )

    sandy = User(
        name='sandy',
        fullname='sandy cardoso',
        address=[Address(email_address='sandy@email.br'),
                 Address(email_address='sandyc@email.org')]
    )

    patrick = User(name='patrick', fullname='patrick cardoso')

    # enviando para o BD (persistencia de dados)
    session.add_all([juliana, sandy, patrick])

    session.commit()

stmt = select(User).where(User.name.in_(['juliana', 'sandy']))
print('Recuperando usuarios a partir de condição de filtragem')
for user in session.scalars(stmt):
    print(user)

stmt_address = select(Address).where(Address.user_id.in_([2]))
print('\nRecuperando os endereços de email de sandy')
for address in session.scalars(stmt_address):
    print(address)


order_stmt = select(User).order_by(User.fullname.desc())
print("\nRecuperando info de maneira ordenada")
for result in session.scalars(order_stmt):
    print(result)

