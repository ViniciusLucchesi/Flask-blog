<div align='center'>

<div style='background: indigo; color: #fff; border-radius: 8px;'>

# Flask Blog

</div>

Este projeto é quase idêntico ao que o professor Camalionte fez em sala de aula.

[Installations](#building-setuppy) - [Running](#running-flask-app) - [Secret_Key](#generating-secret-key) -  

</br>
</br>

</div>

### Building setup.py

```bash
pip install -e .
```

Certifique-se de estar no diretório raíz

</br>


### Running flask app

```bash
export FLASK_APP=blog.app:create_app
```

```bash
flask run
```

</br>


### Generating secret key

```bash
python -c "import secrets; print(secrets.token_hex())"
```

</br>


### Exercício

- [x] Criar uma rota para apagar um post passando o slug
- [x] Refatorar a criação do slug utilizando **slugify**
- [x] Antes de inserir/alterar, verificar se:
     - [x] Slug já existe;
     - [x] Slug conflita com alguma rota;
