import dash
from dash import html
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc

from accordion import accordion_comp

dash._dash_renderer._set_react_version('18.2.0')

app = dash.Dash(__name__)

app.layout = dmc.MantineProvider(
    [
        dmc.AppShell(
            [
                dmc.AppShellHeader(
                    dmc.Container(
                        [
                            dmc.Grid([
                                dmc.GridCol(dmc.Title(
                                'Compartilha Dados',
                                order=1,
                                c='white',
                                pt='0.5em',
                            ), span=6),
                                dmc.GridCol('logo', span=6, style={'textAlign': "right"})
                        ], c='white')
                        ],
                        size='xl',
                    ),
                    style={
                        'background-color': '#11111A',
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
    app.run_server(debug=True)
