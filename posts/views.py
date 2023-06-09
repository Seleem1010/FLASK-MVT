# import base64
from flask import Flask, request, redirect, url_for, render_template, Markup
from Flask_Mvt.models import Post,Category
from Flask_Mvt.posts.postblueprints import post_blueprint
from Flask_Mvt.models import  db
import uuid , os


##list posts
@post_blueprint.route("/", endpoint='posts_index')
def get_posts():
    posts = Post.query.all()
    return render_template("posts/index.html", posts=posts)

#create post
@post_blueprint.route("/posts/create", methods=["GET", "POST"], endpoint="posts_create")
def create_post():
    categories = Category.query.all()
    if request.method == "POST":
        image = request.files.get("image")
        if image:
            # generate a unique filename for the uploaded image
            filename = str(uuid.uuid4()) + os.path.splitext(image.filename)[1]
            # save the image to the static/uploads directory
            image.save(os.path.join("static/uploads", filename))
            # store the filename in the Post object
            image_href = os.path.join("uploads", filename)
        else:
            image_href = None
        
        post = Post(
            title=request.form["title"],
            body=request.form["body"],
            image=image_href,
            category_id=request.form["category_id"]
        )
        db.session.add(post)
        db.session.commit()
        return redirect(url_for("MVT.posts_index"))
    return render_template("posts/create.html", categories=categories)

#view post
@post_blueprint.route("/posts/<int:id>", endpoint="posts_view")
def get_post(id):
    post = Post.get_specific_object(id)
    category = Category.query.get(post.category_id)
    return render_template("posts/view.html", post=post , category=category)

#delete post
@post_blueprint.route("/posts/<int:id>/delete", endpoint="posts_delete")
def delete_post(id):
    post = Post.get_specific_object(id)
    post.delete_post()
    return redirect(url_for('MVT.posts_index'))

#edit post
@post_blueprint.route("/posts/<int:id>/edit", methods=["GET", "POST"], endpoint="posts_edit")
def edit_post(id):
    post = Post.get_specific_object(id)
    categorys =  Category.query.all()
    if request.method=="POST":
        post.title=request.form["title"]
        post.body=request.form["body"]
        image = request.files.get("image")
        if image:
            # generate a unique filename for the uploaded image
            filename = str(uuid.uuid4()) + os.path.splitext(image.filename)[1]
            # save the image to the static/uploads directory
            image.save(os.path.join("static/uploads", filename))
            # store the filename in the Post object
            image_href = os.path.join("uploads", filename)
        else:
            image_href = post.image  # use the existing image if a new one was not uploaded
        post.image=image_href
        post.category_id=request.form["category_id"]
        db.session.commit()
        return redirect(url_for('MVT.posts_index'))
    return render_template("posts/edit.html",post=post ,categorys=categorys)

