import flet as ft

def FlexButton(text=None, icon=None, color=None, bgcolor=None, on_click=None, width=None, height=None, variant="primary", **kwargs):
    styles = {
        "primary": {"color": "white", "bgcolor": "blue700"},
        "secondary": {"color": "white", "bgcolor": "grey700"},
        "success": {"color": "white", "bgcolor": "green700"},
        "danger": {"color": "white", "bgcolor": "red700"},
        "outline": {"color": "blue700", "bgcolor": "transparent"},
    }
    
    selected_style = styles.get(variant, styles["primary"])

    # Using positional content to satisfy Flet 0.82.2 validation
    return ft.ElevatedButton(
        ft.Text(text) if text else None,
        icon=icon,
        color=color or selected_style["color"],
        bgcolor=bgcolor or selected_style["bgcolor"],
        on_click=on_click,
        width=width,
        height=height,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=8),
            padding=15,
        ) if variant != "outline" else ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=8),
            side=ft.BorderSide(1, "blue700"),
            padding=15,
        ),
        **kwargs
    )
