import dash_html_components as html

def SideBar():
    return html.Div([
        html.Img(src="assets/hase_logo.jpg",
                width="100px", height="100px",
                className="rounded-circle"),
        html.H3("AllenTango"),
        html.P("纸上得来终觉浅，绝知此事要躬行")
    ], className="text-white text-center mt-5")