from flask import (
    Flask,
    abort,
    request,
    url_for,
    redirect,
    Blueprint,
    render_template,
    session,
)
from blog.posts import (
    new_post,
    get_all_posts,
    get_post_by_slug,
    delete_post_by_slug,
    update_post_by_slug,
)

bp = Blueprint('post', __name__, template_folder='templates')


@bp.route('/')
def index():
    posts = get_all_posts()
    return render_template('index.html.j2', posts=posts)


@bp.route('/<slug>')
def detail(slug):
    post = get_post_by_slug(slug)
    if not post:
        return abort(404, f'Post "{slug}" not found.')
    return render_template('post.html.j2', post=post)


@bp.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        slug = new_post(title, content)
        
        data = {
            'title': 'New Post:',
            'test': '/new'
        }
        return redirect(url_for('post.detail', slug=slug['slug'], data=data))
    return render_template('form.html.j2')


@bp.route('/delete/<slug>')
def delete(slug):
    was_deleted = delete_post_by_slug(slug)
    if not was_deleted:
        return {'error': f'Não foi possível deletar o post "{slug}"'}
    return redirect(url_for('post.index'))


@bp.route('/update/<slug>')
def update(slug):
    post = get_post_by_slug(slug)
    return render_template()


def configure(app: Flask):
    app.register_blueprint(bp)