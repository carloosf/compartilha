import dash
from dash import html
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc

from accordion import accordion_comp

dash._dash_renderer._set_react_version('18.2.0')

app = dash.Dash(__name__)
server = app.server

app.layout = dmc.MantineProvider(
    [
        dmc.AppShell(
            [
                dmc.AppShellHeader(
                    dmc.Container(
                        [
                            dmc.Grid(
                                [
                                    dmc.GridCol(
                                        dmc.Title(
                                            'Compartilha SEPLAG - Edição Dados',
                                            order=1,
                                        ),
                                        span=10,
                                    ),
                                    dmc.GridCol(
                                        dmc.Flex(
                                            dmc.Image(src='https://i.ibb.co/3m6D2y0/logo2023-cinzaclaro.png', style={'width': '12em'}), 
                                            justify='flex-end'),
                                        span=2,
                                    ),
                                ],
                                c='white'
                            )
                        ],
                        size='xl', py='0.7em'
                        # py='2.5em',
                    ),
                    style={
                        'background-color': '#11111A'
                    },
                ),
                dmc.AppShellMain([dmc.Container([accordion_comp], size='xl')]),
                dmc.AppShellFooter(['footer']),
            ],
            header={'height': 70},
            p='xl',
        )
    ],
    theme={'headings': {'fontFamily': 'Roboto, sans-serif'}},
    # theme={'headings': {'fontFamily': 'Roboto, sans-serif'}},
)

if __name__ == '__main__':
    app.run_server(host="0.0.0.0", port=8000)
