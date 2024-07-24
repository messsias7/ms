from flask import flask, jsonify, request

app = Flask (_name_)

usuarios = [
    {
     
      'id' : 1,
      'nome' : 'Boba Fett' ,
      'idade' : 41 
    },
    {
      'id' : 2,
       'nome' : 'Anakin Skywalker',
       'idade' : 35
    },
    {
        'id' : 3,
        'nome' : 'Darth Maul',
        'idade' : 30
    },
]
@app . route ('/usuarios', methods=['GET'])
def consultar_usuarios ():
    return jsonify (usuarios)
    
@app . route ('/usuarios', methods=['GET'])
def consultar_usuarios_por_id(id):
    for usuario in usuarios:
        if usuario.get ('id') == id:
            return jsonify (usuario)

@app . route ('/usuarios', methods=['POST'])   
def consultar_usuario():
      novo_usuario = request.get_json()   
      usuarios.append (novo_usuario)  
      return jsonify (usuarios)



app.run(port=8080,host='localhost',debug=true)