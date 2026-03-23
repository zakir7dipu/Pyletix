import flet as ft
from core.controller import BaseController
from app.models.Post import Post
from core.auth.auth_service import Auth
from core.utils.date_util import DateUtil

class PostController(BaseController):
    def index(self, request):
        posts = Post.query().with_('user').get()
        
        post_controls = []
        for post in posts:
            post_controls.append(
                ft.ListTile(
                    title=ft.Text(post.title),
                    subtitle=ft.Text(f"By {post.user.name} • {DateUtil.human_readable(post.created_at)}"),
                    trailing=ft.IconButton("delete", on_click=lambda _: self.delete(post.id))
                )
            )
            
        return self.render([
            ft.Text("Community Posts", size=30),
            ft.Column(post_controls),
            ft.FloatingActionButton(icon="add", on_click=lambda _: self.page.go("/posts/create"))
        ], title="Posts")

    def create(self, request):
        self.title_input = ft.TextField(label="Post Title")
        self.content_input = ft.TextField(label="Content", multiline=True)
        
        return self.render([
            ft.Text("Create New Post", size=30),
            self.title_input,
            self.content_input,
            ft.ElevatedButton("Publish", on_click=self.store)
        ], title="Create Post")

    def store(self, e):
        user = Auth.user(self.page)
        Post.create(
            user_id=user.id,
            title=self.title_input.value,
            content=self.content_input.value
        )
        self.page.go("/posts")

    def delete(self, post_id):
        post = Post.find(post_id)
        if post:
            post.delete()
        self.page.go("/posts")
