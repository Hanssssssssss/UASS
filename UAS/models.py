from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class tb_sepeda_motor(Base):
    __tablename__ = 'tb_sepeda_motor'
    sepeda_motor: Mapped[str] = mapped_column(primary_key=True)
    cc: Mapped[int] = mapped_column()
    harga: Mapped[int] = mapped_column()
    speed: Mapped[int] = mapped_column()
    berat: Mapped[int] = mapped_column()
    kapasitas_tangki_bensin: Mapped[int] = mapped_column()
    
    def __repr__(self) -> str:
        return f"tb_sepeda_motor(sepeda_motor={self.sepeda_motor!r}, cc={self.cc!r})"