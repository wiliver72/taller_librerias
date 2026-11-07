import flet as ft


class ContadorApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.valor = 0
        self.numero = ft.Text("0", size=64, weight=ft.FontWeight.BOLD)

    def actualizar(self):
        self.numero.value = str(self.valor)
        self.page.update()

    def incrementar(self, e):
        self.valor += 1
        self.actualizar()

    def disminuir(self, e):
        self.valor -= 1
        self.actualizar()

    def reiniciar(self, e):
        self.valor = 0
        self.actualizar()

    def construir(self):
        self.page.title = "Contador interactivo"
        self.page.theme_mode = ft.ThemeMode.DARK
        self.page.bgcolor = "#101827"
        self.page.padding = 30
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER

        tarjeta = ft.Container(
            width=420,
            padding=30,
            border_radius=20,
            bgcolor="#1E293B",
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
                controls=[
                    ft.Text("CONTADOR INTERACTIVO", size=22, weight=ft.FontWeight.BOLD),
                    ft.Text("Presiona un botón para cambiar el valor"),
                    self.numero,
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.IconButton(icon=ft.Icons.REMOVE, on_click=self.disminuir),
                            ft.Button("Incrementar", on_click=self.incrementar),
                        ],
                    ),
                    ft.OutlinedButton("Reiniciar", on_click=self.reiniciar),
                ],
            ),
        )
        self.page.add(tarjeta)


def main(page: ft.Page):
    app = ContadorApp(page)
    app.construir()


if __name__ == "__main__":
    ft.run(main)
