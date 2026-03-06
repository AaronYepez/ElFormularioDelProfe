import flet as ft

def main(page: ft.Page):
    page.title = "Ficha de registro de usuarios ;>"
    page.padding = 20
    page.theme_mode = ft.ThemeMode.LIGHT
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    nombre = ft.TextField(label="Nombre completo", width=400, text_align=ft.TextAlign.LEFT)
    correo = ft.TextField(label="Correo Electrónico", width=400, text_align=ft.TextAlign.LEFT)
    
    modalidad_pago = ft.RadioGroup(
        content=ft.Column([
            ft.Radio(value="Completo", label="Pago Completo"),
            ft.Radio(value="Cuotas", label="Pago por cuotas"),
        ]),
        value="Completo"
    )
    
    taller_interes = ft.Dropdown(
        width=400,
        label="Selecciona tu taller",
        options=[
            ft.dropdown.Option("Python para Principiantes"),
            ft.dropdown.Option("Flet Intermedio"),
            ft.dropdown.Option("Análisis de Datos con Pandas"),
        ],
    )
    
    check_portatil = ft.Checkbox(
        label="Requiere computadora portátil",
        value=False,
        fill_color=ft.Colors.GREEN
    )
    
    nivel_label = ft.Text("Nivel: 1")
    experiencia = ft.Slider(
        min=1, max=5, divisions=4, value=1,
        on_change=lambda e: (setattr(nivel_label, "value", f"Nivel: {int(e.control.value)}"), page.update())
    )
    
    resumen = ft.Text(size=16, color=ft.Colors.BLUE_900, weight=ft.FontWeight.W_500)

    def generar_ficha(e):
        necesita_pc = "Sí" if check_portatil.value else "No"
        
        resumen.value = (
            f"--- FICHA DEL PARTICIPANTE ---\n"
            f"Nombre: {nombre.value}\n"
            f"Email: {correo.value}\n"
            f"Taller: {taller_interes.value}\n"
            f"Pago: {modalidad_pago.value}\n"
            f"Requiere Portátil: {necesita_pc}\n"
            f"Nivel de Experiencia: {int(experiencia.value)}\n"
            f"-------------------------------"
        )
        page.update()

    page.add(
        ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text("Registro de Participantes", size=30, weight=ft.FontWeight.BOLD),
                nombre,
                correo,
                taller_interes,
                ft.Column([
                    ft.Text("Modalidad de pago:", weight=ft.FontWeight.BOLD),
                    modalidad_pago
                ], horizontal_alignment=ft.CrossAxisAlignment.START, width=400),
                ft.Container(check_portatil, width=400),
                ft.Column([
                    ft.Text("Nivel de experiencia:", weight=ft.FontWeight.BOLD),
                    experiencia,
                    nivel_label
                ], width=400),
                ft.ElevatedButton(
                    "Mostrar Ficha del Participante",
                    bgcolor=ft.Colors.GREEN_400,
                    color=ft.Colors.WHITE,
                    on_click=generar_ficha
                ),
                resumen
            ],
        )
    )

ft.app(target=main)
