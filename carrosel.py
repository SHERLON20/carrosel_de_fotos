import flet as ft
def main(page:ft.Page):
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.bgcolor=ft.colors.BLACK
    def expande_image(e):
        for c in carrosel.controls:
            c.col=1
        e.control.col= carrosel.columns - len(carrosel.controls)+1
        carrosel.update()
    carrosel=ft.ResponsiveRow(
        columns=12,
        controls=[
            ft.Container(
                col=1,
                image_src=f'https://picsum.photos/250/300?{num}',
                image_fit=ft.ImageFit.COVER,
                border_radius=ft.border_radius.all(3),
                on_click=expande_image
            )for num in range(10,18)
        ],spacing=2,
    )
    carrosel.controls[0].col=12 - len(carrosel.controls)+1
    layout=ft.Container(
        width=600,
        height=200,
        shadow=ft.BoxShadow(blur_radius=500,color=ft.colors.CYAN),
        border_radius=ft.border_radius.all(10),
        bgcolor=ft.colors.CYAN,
        content=carrosel
    )
    page.add(layout)

if __name__=="__main__":
    ft.app(target=main)
