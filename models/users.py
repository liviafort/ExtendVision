from database.bd import User, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()


def get_user_by_id(user_id):
    user = session.query(User).filter_by(id=user_id).first()
    return user


def create_user(registration, password, name, title, gender, birth_date, type):
    new_user = User(
        registration=registration,
        password=password,
        name=name,
        title=title,
        gender=gender,
        birth_date=birth_date,
        type=type
    )

    session.add(new_user)
    session.commit()
    return new_user.id

if __name__ == '__main__':
    pass