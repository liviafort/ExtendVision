from database.bd import User

#---------------------------------#
#Função que retorna usuário por ID#
#---------------------------------#
def get_user_by_id(user_id):
    user = session.query(User).filter_by(id=user_id).first()
    return user
