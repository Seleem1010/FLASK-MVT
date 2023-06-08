import base64
from flask import Flask, request, redirect, url_for, render_template, Markup
from Flask_Mvt.models import Post,Category
from Flask_Mvt.posts.postblueprints import post_blueprint
from Flask_Mvt.models import  db


##list posts
@post_blueprint.route("/", endpoint='posts_index')
def get_posts():
    posts = Post.query.all()
    return render_template("posts/index.html", posts=posts)

#create post
@post_blueprint.route("/posts/create", methods=["GET", "POST"], endpoint="posts_create")
def create_post():
    
    categories = Category.query.all()
    if request.method=="POST":
        image = request.files.get("image").read() if request.files.get("image") else None
        if image:
            image = base64.b64encode(image)
        
        post = Post(title=request.form["title"], body=request.form["body"], image=image , category_id=request.form["category_id"])
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('MVT.posts_index'))
    return render_template("posts/create.html" , categories=categories)

#view post
@post_blueprint.route("/posts/<int:id>", endpoint="posts_view")
def get_post(id):
    post = Post.get_view_url(id)
    return render_template("posts/view.html", post=post)

#delete post
@post_blueprint.route("/posts/<int:id>/delete", endpoint="posts_delete")
def delete_post(id):
    post = Post.get_delete_url(id)
    post.delete_post()
    return redirect(url_for('MVT.posts_index'))

#edit post
@post_blueprint.route("/posts/<int:id>/edit", methods=["GET", "POST"], endpoint="posts_edit")
def edit_post(id):
    post = Post.query.get_or_404(id)
    if request.method=="POST":
        post.title=request.form["title"]
        post.body=request.form["body"]
        image = request.files.get("image").read() if request.files.get("image") else None
        if image:
            image = base64.b64encode(image)
        post.image=image
        post.category_id=request.form["category_id"]
        db.session.commit()
        return redirect(url_for('MVT.posts_index'))
    return render_template("posts/edit.html",post=post)

