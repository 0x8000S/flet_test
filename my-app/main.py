from pydoc import visiblename
from tabnanny import check

import flet as ft
from flet_core import Radio


def main(page: ft.Page):
    txt_edit = ft.TextField(value="", keyboard_type=ft.KeyboardType.NUMBER, hint_text="请输入费用")
    res = ft.Text("小费:0.0", size=40)
    foft = ft.Switch("四舍五入")
    choose = ft.RadioGroup(content=ft.Column(
        [
        Radio("令人惊叹的(24%)", value="amz"),
        Radio("不错(20%)", value="good"),
        Radio("还行(16%)", value="ok")
    ],
        spacing=0
    ))
    choose.value = "amz"
    def on_ckic(e):
        res.color = "black"
        resz = 0
        tx = txt_edit.value
        if tx == "":
            res.value = "小费:0.0"
            page.update()
            return 0
        try:
            tx = float(tx)
        except ValueError:
            res.value = "请检查你输入的东西!"
            res.color = "red"
            page.update()
            return -1
        match choose.value:
            case "amz":
                resz = tx*0.24
            case "good":
                resz = tx*0.2
            case "ok":
                resz = tx*0.16

        if foft.value:
            resz = round(resz)
        res.value = str(resz)

        page.update()

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(
                        title=ft.Text("小费计算"),
                        actions=[ft.IconButton(ft.icons.MENU, on_click=lambda _: page.go("/about"))]
                    ),
                    txt_edit,
                    choose,
                    foft,
                    ft.FilledButton("计算", on_click=on_ckic),
                    res
                ],
            ),
        ),
        if page.route == "/about":
            page.views.append(
                ft.View(
                    "/about",
                    [
                        ft.AppBar(
                            leading=ft.IconButton(ft.icons.KEYBOARD_BACKSPACE, on_click=lambda _: page.go("/")),
                            title=ft.Text("关于")
                        ),
                        ft.Image(
                            src=f"https://flet.qiannianlu.com/img/logo.svg",
                        ),
                        ft.Text("本项目由Python使用Flet库编写,如你所见这就是此框架的Logo.",
                                text_align=ft.TextAlign.CENTER,
                                size=20
                                )
                    ]
                )
            ),
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(main, view=ft.AppView.WEB_BROWSER)
