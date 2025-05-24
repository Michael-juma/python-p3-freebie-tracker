#!/usr/bin/env python3

# Script goes here!
from sqlalchemy.orm import sessionmaker
from models import engine, Company, Dev, Freebie

Session = sessionmaker(bind=engine)
session = Session()
# Add companies
c1 = Company(name="Google", founding_year=1998)
c2 = Company(name="Amazon", founding_year=1994)
session.add_all([c1, c2])

# Add devs
d1 = Dev(name="Alice")
d2 = Dev(name="Bob")
session.add_all([d1, d2])

# Add freebies
f1 = Freebie(item_name="T-shirt", value=20, company=c1, dev=d1)
f2 = Freebie(item_name="Mug", value=10, company=c2, dev=d2)
session.add_all([f1, f2])

session.commit()