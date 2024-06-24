#!/usr/bin/python3
"""

Script that lists all states with a name containing the letter a from the database

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
    state = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id)
    if state is None:
        print("Nothing")
    for row in state:
        print("{}: {}".format(row.id, row.name))
    session.close()
