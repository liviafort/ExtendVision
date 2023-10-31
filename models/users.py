from database.bd import User, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()


def get_user_by_id(user_id):
    user = session.query(User).filter_by(id=user_id).first()
    return user


if __name__ == '__main__':
    pass