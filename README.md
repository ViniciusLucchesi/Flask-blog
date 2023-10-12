## Flask Blog

### Running flask app

```bash
export FLASK_APP=blog.app:create_app
```

```bash
flask run
```

### Building setup.py

```bash
pip install -e .
```

Certifique-se de estar no diretório raíz


### Generating secret key

```bash
python -c "import secrets; print(secrets.token_hex())"
```


### Exercício

- [x] Criar uma rota para apagar um post passando o slug
- [x] Refatorar a criação do slug utilizando **slugify**
- [x] Antes de inserir/alterar, verificar se:
     - [x] Slug já existe;
     - [x] Slug conflita com alguma rota;
