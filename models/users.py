from database.bd import User, engine
from sqlalchemy.orm import sessionmaker
from flask import jsonify

Session = sessionmaker(bind=engine)
session = Session()


def get_user_by_id(user_id):
    user = session.query(User).filter_by(id=user_id).first()
    user_dict = user.__dict__
    user_dict.pop('_sa_instance_state', None)
    return jsonify(user_dict)

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

def update_user(user_id, registration, password, name, title, gender, birth_date, type):
    session.query(User).filter(User.id==user_id).update({"registration": registration,
        "password": password,
        "name": name,
        "title": title,
        "gender": gender,
        "birth_date": birth_date,
        "type": type})
    session.commit()

def delete_user(user_id):
    session.query(User).filter(User.id==user_id).delete()
    session.commit()
    return str(user_id)

if __name__ == '__main__':
    pass