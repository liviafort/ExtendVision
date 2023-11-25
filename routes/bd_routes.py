from flask import Blueprint, render_template, jsonify, request, redirect
from entitys.facade.FacadeField import FacadeField

facadeField = FacadeField()

#Rotas para banco de dados
app_bd = Blueprint('app_bd', __name__)


#CRUD FIELDS
@app_bd.route('/field/', methods=['GET'])
def get_field_by_id_route():
    field_id = request.args.get('field_id')
    field_name = request.args.get('field_name')

    if field_id:
        return facadeField.get_field_by_id(field_id)
    
    elif field_name:
        return facadeField.get_field_by_name(field_name)
    
    return facadeField.get_fields()


@app_bd.route('/field/', methods=['POST'])
def create_field_route():
    data = request.json
    required_fields = ['field']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Campos obrigatórios ausentes'}), 400
    new_field_id = facadeField.create_field(**data)

    return jsonify({'message': 'Novo Campo adicionado com sucesso', 'Field_id': new_field_id})


@app_bd.route('/field/<int:field_id>', methods=['PUT'])
def update_field_route(field_id):
    data = request.json
    required_fields = ['field']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Campos obrigatórios ausentes'}), 400
    new_field_id = facadeField.update_field(field_id,**data)

    return jsonify({'message': 'Campo atualizado com sucesso', 'Field_id': new_field_id})


@app_bd.route('/field/<int:field_id>', methods=['DELETE'])
def delete_field_route(field_id):
    field_del = facadeField.delete_field(field_id)
    return jsonify({'message': 'Campo Deletado', 'Campo': field_del})