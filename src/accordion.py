import dash_mantine_components as dmc
from dash import html
from topicos import lista_de_topicos

def create_accordion_label(label, image, description):
    return dmc.AccordionControl(
        dmc.Group(
            [
                dmc.Avatar(
                    src=image, 
                    radius="xl", 
                    size="xl", 
                    # style={"zoom": "150%"}
                ),
                html.Div(
                    [
                        dmc.Title(label, order=2),
                        dmc.Text(
                            description, 
                            size="xl", 
                            fw=400, 
                            c="dimmed", 
                            style={"zoom": "120%"}
                        ),
                    ]
                ),
            ]
        )
    )


def create_accordion_content(content):
    return dmc.AccordionPanel(dmc.Text(content, size="xl"))


accordion_comp = dmc.Accordion(
    chevronPosition="right",
    variant="contained",
    children=[
        dmc.AccordionItem(
            [
                create_accordion_label(
                    character["label"], character["image"], character["description"]
                ),
                create_accordion_content(character["content"]),
            ],
            value=character["id"],
        )
        for character in lista_de_topicos
    ],
)