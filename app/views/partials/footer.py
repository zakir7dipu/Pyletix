import flet as ft

def Footer():
    return ft.Container(
        content=ft.Row([
            ft.Text("© 2026 Pyletix Framework", size=12, color="secondary"),
            ft.Row([
                ft.TextButton("Documentation", style=ft.ButtonStyle(color="blue700")),
                ft.TextButton("Support", style=ft.ButtonStyle(color="blue700")),
            ])
        ], alignment="spaceBetween"),
        padding=20,
        border=ft.border.only(top=ft.border.BorderSide(0.5, "outlinevariant")),
    )
