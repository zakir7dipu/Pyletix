import flet as ft

class Table(ft.DataTable):
    def __init__(self, columns, rows, border=None, border_radius=8, **kwargs):
        # Transform columns list of strings/controls into DataColumn objects
        data_columns = [
            ft.DataColumn(ft.Text(col, weight="bold") if isinstance(col, str) else col)
            for col in columns
        ]
        
        # Transform rows list of lists into DataRow objects
        data_rows = [
            ft.DataRow(cells=[ft.DataCell(ft.Text(str(cell)) if not isinstance(cell, ft.Control) else cell) for cell in row])
            for row in rows
        ]
        
        super().__init__(
            columns=data_columns,
            rows=data_rows,
            border=border or ft.border.all(1, "outlinevariant"),
            border_radius=border_radius,
            heading_row_color="surfacevariant",
            vertical_lines=ft.border.BorderSide(0.5, "outlinevariant"),
            horizontal_lines=ft.border.BorderSide(0.5, "outlinevariant"),
            **kwargs
        )
