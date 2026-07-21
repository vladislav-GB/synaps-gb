from dash import html

def Sidebar():
    return html.Div(
        [
            html.Div([
                
                # 1. Картинка 
                html.Img(
                    src='/assets/brain.png',
                    style={
                        'height': '54px',          
                        'width': 'auto',
                        'marginRight': '14px'      
                    }
                ),
                
                # 2. Текст 
                html.Div([
                    html.H1("SYNAPS", className="logo-text"),
                    html.H2("research platform", className="subtitle-text")
                ], style={
                    'display': 'flex', 
                    'flexDirection': 'column', 
                    'justifyContent': 'center' 
                })
                
            ], style={
                'display': 'flex',             
                'alignItems': 'center',      
                'marginBottom': '16px'         
            }),
            
            html.Hr(className="divider"),
            
            # Кнопки
            html.Button(["Dashboard"], className="nav-button active"), 
            html.Button(["Preprocessing"], className="nav-button"),
            html.Button(["Training"], className="nav-button"),
            html.Button(["Test"], className="nav-button"),
            html.Button(["Settings"], className="nav-button"),
        ],
        className="sidebar"
    )