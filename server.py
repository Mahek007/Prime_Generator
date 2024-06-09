from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, Float, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import time
from prime_generator import PrimeGenerator

app = FastAPI()

# Configure CORS (optional)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database setup
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class PrimeRequest(Base):
    __tablename__ = "prime_requests"
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    start = Column(Integer)
    end = Column(Integer)
    strategy = Column(String)
    time_elapsed = Column(Float)
    prime_count = Column(Integer)

Base.metadata.create_all(bind=engine)

class PrimeRequestModel(BaseModel):
    start: int
    end: int
    strategy: str

class PrimeResponseModel(BaseModel):
    primes: List[int]
    time_elapsed: float
    prime_count: int

prime_gen = PrimeGenerator()

@app.post("/generate_primes", response_model=PrimeResponseModel)
def generate_primes(request: PrimeRequestModel):
    start_time = time.time()

    if request.strategy == 'sieve':
        primes = prime_gen.sieve_of_eratosthenes(request.start, request.end)
    elif request.strategy == 'trial':
        primes = prime_gen.trial_division(request.start, request.end)
    else:
        raise HTTPException(status_code=400, detail="Invalid strategy")

    end_time = time.time()
    time_elapsed = end_time - start_time
    prime_count = len(primes)

    # Save the request to the database
    db = SessionLocal()
    prime_request = PrimeRequest(
        start=request.start,
        end=request.end,
        strategy=request.strategy,
        time_elapsed=time_elapsed,
        prime_count=prime_count
    )
    db.add(prime_request)
    db.commit()
    db.refresh(prime_request)
    db.close()

    return PrimeResponseModel(
        primes=primes,
        time_elapsed=time_elapsed,
        prime_count=prime_count
    )
