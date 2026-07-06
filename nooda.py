import flet as ft
import requests
import random

API_KEY = "live_GLpmHYbTWHYl2sHrlK3DgdQXXMstLDWfvnIKveUwRgT2b3HzuFcA5O7cfyxgE8rS"
URL = "https://api.thecatapi.com/v1/images/search"

comforting_messages = [
    "بصي القطة الكيوت دي مخصوص عشانك يا ندى.. اضحكي بقا",
    "متخليش زعل يطفي عيونك يا ندى.. افتكري إنك دايماً قوية",
    "الدنيا بتبقى أحلى لما بتضحكي يا ندى.. فكي التكشيرة",
    "خدي بريك دقيقة وبصي الكائن ده جاي يواسيكي إزاي يا ندى"
]

def main(page: ft.Page):
    page.title = "nooda"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0

    page.window_width = 450
    page.window_height = 680
    page.window_resizable = True
    page.window_min_width = 350
    page.window_min_height = 500

    def on_resize(e):
        new_width = min(max(page.width - 60, 280), 420)
        main_card.width = new_width
        page.update()

    page.on_resize = on_resize

    def get_cat_image():
        headers = {"x-api-key": API_KEY}
        try:
            unique_url = f"{URL}?t={random.randint(1,100000)}"
            response = requests.get(unique_url, headers=headers, timeout=5)
            if response.status_code == 200:
                data = response.json()
                return data[0]['url']
        except Exception:
            return None
        return None

    def on_click(e):
        loading_progress.visible = True
        loading_text.visible = True
        comforting_header.visible = False
        action_button.text = "بجيبلك قطة كيوت يا ندى..."
        action_button.disabled = True
        action_button.bgcolor = "#8A5A4A"
        page.update()

        img_url = get_cat_image()

        if img_url:
            cat_image.src = img_url
            cat_image.visible = True
            error_text.visible = False
            comforting_header.value = random.choice(comforting_messages)
            comforting_header.visible = True
        else:
            error_text.visible = True
            cat_image.visible = False

        loading_progress.visible = False
        loading_text.visible = False
        action_button.text = "جربي مرة تانية يا ندى"
        action_button.disabled = False
        action_button.bgcolor = "#E8573F"
        page.update()

    comforting_header = ft.Text(
        value="",
        size=17,
        weight=ft.FontWeight.W_600,
        color="#FFF3E0",
        text_align=ft.TextAlign.CENTER,
        no_wrap=False,
        visible=False
    )

    cat_image = ft.Image(
        src="https://via.placeholder.com/350x350.png?text=Waiting+for+Joy...🌸",
        width=350,
        height=350,
        fit=ft.ImageFit.COVER,
        border_radius=ft.border_radius.all(25),
        visible=False
    )

    image_frame = ft.Container(
        content=cat_image,
        padding=0,
        border_radius=25,
        shadow=ft.BoxShadow(
            blur_radius=15,
            color="#40FF6F3C",
            offset=ft.Offset(0, 10)
        )
    )

    loading_progress = ft.ProgressBar(
        width=300,
        color="#FF8C42",
        bgcolor="#30FFE0C2",
        visible=False
    )
    loading_text = ft.Text("جاري تحضير جرعة السعادة...", size=12, color="#FFD9B3", visible=False)

    error_text = ft.Text(
        "مفيش نت يا ندى.. السحر محتاج إنترنت عشان يشتغل",
        color="#FF7A59",
        size=14,
        visible=False,
        text_align=ft.TextAlign.CENTER
    )

    action_button = ft.ElevatedButton(
        text="دوسي هنا وحالاً هتفرحي يا ندى",
        style=ft.ButtonStyle(
            color="white",
            bgcolor="#E8573F",
            padding=ft.padding.all(22),
            shape=ft.RoundedRectangleBorder(radius=15),
            animation_duration=300,
            elevation={"hovered": 10, "": 5},
        ),
        on_click=on_click
    )

    main_card = ft.Container(
        content=ft.Column(
            controls=[
                comforting_header,
                ft.Divider(height=15, color="transparent"),
                image_frame,
                ft.Divider(height=15, color="transparent"),
                ft.Column(
                    controls=[
                        loading_progress,
                        loading_text,
                        error_text,
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Divider(height=20, color="transparent"),
                action_button,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        padding=30,
        bgcolor="#662A1712",
        border_radius=30,
        shadow=ft.BoxShadow(
            blur_radius=20,
            color="#40120A05",
            offset=ft.Offset(0, 10)
        ),
        width=400,
    )

    grid_colors = [
        ["#2B1A3D", "#4A2545", "#6B2D4D", "#8C3A4A"],
        ["#3D2050", "#7A3350", "#C24545", "#E8573F"],
        ["#5A2A55", "#B03A4E", "#E8703F", "#F4A261"],
        ["#3D2050", "#8C3A4A", "#E8573F", "#F4C27A"],
    ]

    grid_rows = []
    for row_colors in grid_colors:
        row_cells = [
            ft.Container(bgcolor=color, expand=True)
            for color in row_colors
        ]
        grid_rows.append(ft.Row(controls=row_cells, expand=True, spacing=0))

    background_grid = ft.Column(controls=grid_rows, expand=True, spacing=0)

    background = ft.Stack(
        controls=[
            background_grid,
            ft.Container(
                content=ft.Row(
                    controls=[main_card],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                alignment=ft.alignment.center,
                expand=True,
            ),
        ],
        expand=True,
    )

    page.add(background)

ft.app(target=main, assets_dir="assets")
