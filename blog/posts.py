from datetime import datetime
from slugify import slugify
from blog.database import mongo



def get_all_posts(published: bool = True) -> list:
    posts = mongo.db.posts.find({"published": published})
    return posts.sort("date")


def get_post_by_slug(slug: str) -> dict:
    """
    Exemplo:
        get -> /Novidades%20do%20Flask%202023
        return -> /novidades-do-flask-2023
    """
    post = mongo.db.posts.find_one({"slug": slug})
    return post


def update_post_by_slug(slug: str, data: dict) -> dict:
    try:
        id = mongo.db.posts.find_one_and_update({"slug": slug}, {'$set': data})
        return {'success': f'ID {id} created successfully!'}
    except Exception as error:
        return {"error": f'Update error: {error}'}


def new_post(title: str, content: str, published: bool = True) -> dict:
    valid_slug, slug = generate_new_slug(title)
    match valid_slug:
        case True:
            try:
                new_id = mongo.db.posts.insert_one({
                    "title": title, 
                    "content": content, 
                    "published": published, 
                    "slug": slug, 
                    "date": datetime.now()
                })
                return {"slug": slug, "new_id": new_id}
            except Exception as error:
                return {'error': f'Insert error: {error}'}

        case False:
            return {"error": f'Slug {slug} already in use.'}
    

def generate_new_slug(title: str) -> (bool, str):
    """
    Generate a new slug based on the title.

    RETURN:
        (True, slug) -> Slug is valid.\n
        (False, slug) -> Slug is not valid because it is already in use.
    """
    slug = slugify(title)
    existent_slug = mongo.db.posts.find_one({"slug": slug})
    if existent_slug:
        return (False, slug)
    return (True, slug)


def delete_post_by_slug(slug: str) -> bool:
    """
    Delete a post based on the slug provided

    ARGS:
        slug -> Slug of the post to be deleted.
    
    RETURN:
        True -> Successfully deleted
        False -> Error during deletion
    """
    try:
        id = mongo.db.posts.find_one_and_delete({"slug": slug})
        return True
    except Exception as error:
        return False
