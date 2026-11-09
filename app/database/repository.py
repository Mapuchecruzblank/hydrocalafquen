from app.database.models import Inmersion, engine
from sqlalchemy.orm import sessionmaker

SessionLocal = sessionmaker(bind=engine)


def registrar_inmersion(
    profundidad_max: float,
    tiempo_apnea: int,
    temperatura_agua: float | None = None,
    ubicacion: str = "Lago Calafquén",
    notas: str | None = None,
    equipo_id: int | None = None,
) -> Inmersion:
    session = SessionLocal()
    try:
        inmersion = Inmersion(
            profundidad_max=profundidad_max,
            tiempo_apnea=tiempo_apnea,
            temperatura_agua=temperatura_agua,
            ubicacion=ubicacion,
            notas=notas,
            equipo_id=equipo_id,
        )
        session.add(inmersion)
        session.commit()
        session.refresh(inmersion)
        return inmersion
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
    
    
def listar_inmersiones() -> list[Inmersion]:
    with SessionLocal() as session:
        return (
            session.query(Inmersion)
            .order_by(Inmersion.id.desc())
            .all()
        )