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
    states = session.query(State).filter(State.name == (argv[4],))
    if states is None:
        print("Not found")
    else:
        print(states[0].id)
    session.close()
