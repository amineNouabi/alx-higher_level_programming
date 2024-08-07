#!/usr/bin/python3
"""

Script that prints the State object with
    the name passed as argument from the

"""

from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    louisiana = State(name="Louisiana")
    session.add(louisiana)
    state = session.query(State).filter_by(name="Louisiana").first()
    print(state.id)
    session.commit()
    session.close()
