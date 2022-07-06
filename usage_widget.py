# %%
import pandas as pd
import ipyvuetify as v

USAGE_FILE = "data/usage.json"


# %%
usage_df = pd.read_json(USAGE_FILE).set_index("id")
usage_names = list(usage_df.index)


class Usage(v.Container):
    def __init__(self):
        self.usage_title = v.Subheader(children=["Usage"])

        self.usage_select = v.Select(
            label="Usage Profile", v_model="", items=usage_names
        )
        self.usage_select.on_event("change", self.usage_change)

        self.usage_card = v.Card(
            loading=False,
            elevation=0,
            children=[
                v.Row(children=[self.usage_title]),
                v.Row(
                    children=[
                        v.Col(
                            cols=7,
                            children=[self.usage_select],
                        )
                    ]
                ),
            ],
        )
        super().__init__(children=[self.usage_card])

    def usage_change(self, widget, *args):
        self.usage_card.loading = True
        self.file = usage_df.loc[self.usage_select.v_model]["file"]
        # self.usage_profile = pd.read_excel(self.file).set_index("TagesNr.")
        # self.next_btn.disabled = False
        self.usage_card.loading = False


u = Usage()
u

# %%