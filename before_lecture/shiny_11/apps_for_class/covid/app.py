from shiny import App, render, ui, reactive
import pandas as pd 
import matplotlib.pyplot as plt

app_ui = ui.page_fluid(
    ui.input_select(
        id='state', 
        label='Choose a state:',
        choices=["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
    ),
    ui.input_radio_buttons(
        id='data_type', 
        label='Choose data type:',
        choices=["Cases", "Deaths"], 
        selected="Cases"  # Optional: Set default selection
    ),
    ui.output_plot('ts'),
    ui.output_table("subsetted_data_table")
)

def server(input, output, session):
    @reactive.calc
    def full_data():
<<<<<<< HEAD
        return pd.read_csv("nyt_covid19_data.csv", parse_dates=['date'])
=======
        return pd.read_csv("covid/nyt_covid19_data.csv", parse_dates = ['date'])
>>>>>>> upstream/main

    @reactive.calc
    def subsetted_data():
        df = full_data()
        return df[df['state'] == input.state()]

    @render.table()
    def subsetted_data_table():
        return subsetted_data()

    @render.plot
    def ts():
        df = subsetted_data()
        fig, ax = plt.subplots(figsize=(3,6))
        if input.data_type() == "Cases":
            ax.plot(df['date'], df['cases'], label="Cases")
        else:
            ax.plot(df['date'], df['deaths'], label="Deaths")
        ax.tick_params(axis='x', rotation=45)
        ax.set_xlabel('Date')
        ax.set_ylabel(input.data_type())
        ax.set_title(f'COVID-19 {input.data_type().lower()} in {input.state()}')
        ax.legend()
        ax.set_yticklabels(['{:,}'.format(int(x)) for x in ax.get_yticks()])
        return fig

app = App(app_ui, server)
