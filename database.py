from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

# PostgreSQL Database URL (Modify with your credentials)
DATABASE_URL = "postgresql://postgresql:mrunschakole@localhost:5432/allergen_db"

# Initialize database engine
engine = create_engine(DATABASE_URL, echo=True)

# Base model
Base = declarative_base()

# Allergen Detection Table
class AllergenDetection(Base):
    __tablename__ = "detections"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    filename = Column(String, nullable=False)
    detected_allergens = Column(String, nullable=False)

# Create tables
Base.metadata.create_all(engine)

# Create a session
SessionLocal = sessionmaker(bind=engine)

# Function to add a detection result
def save_detection(filename, allergens):
    session = SessionLocal()
    new_entry = AllergenDetection(filename=filename, detected_allergens=",".join(allergens))
    session.add(new_entry)
    session.commit()
    session.close()

# Function to retrieve all detection records
def get_all_detections():
    session = SessionLocal()
    detections = session.query(AllergenDetection).all()
    session.close()
    return detections