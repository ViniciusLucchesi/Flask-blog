import click

from blog.posts import (
    get_all_posts,
    get_post_by_slug,
    new_post,
    update_post_by_slug
)


@click.group()
def post():
    """Manage blog posts."""


@post.command()
@click.option("--title")
@click.option("--content")
def new(title, content):
    """Creates a new post"""
    new = new_post(title, content)
    click.echo(f"New post {new} created!")


@post.command("list")
def _list():
    "Lists all published posts."
    for post in get_all_posts():
        click.echo(post)


@post.command()
@click.argument("slug")
def get(slug):
    """Get post by slug."""
    post = get_post_by_slug(slug)
    click.echo(post)


def configure(app):
    app.cli.add_command(post)
