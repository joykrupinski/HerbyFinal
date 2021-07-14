import pandas as pd
pd.set_option('max_rows',20)
import plotly.express as px
import plotly.io as pio
pio.renderers.default = "browser"
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc


#the following code was written following the tutorial "Create Interactive Dashboard in Python from scratch | 
#Vizualization | DASH | PLOTLY" by Data Science with Raghav  (https://www.youtube.com/watch?v=Y5-Rmdcd6MQ&t=370s)
#The code documentation for the tutorial can be found on this git repo https://github.com/raaga500/YTshared/blob/master/V5_CovidDashboard-World.ipynb

#read in Data
DATA_URL = 'https://raw.githubusercontent.com/joykrupinski/HerbyFinal/main/test.csv'
data_sensors_ts = pd.read_csv(DATA_URL)

#get data in correct shape - (dependent on selected window in slider)
def process_data(data,sensor='Temperature',window=3):
    conf_ts = data
    conf_ts_sensor = conf_ts[conf_ts['Sensor']==sensor]
    final_dataset = conf_ts_sensor.T[1:]
    df = pd.DataFrame(final_dataset)
    #reverse data frame to take last values
    df =  df.iloc[::-1]
    df = df.iloc[:window]
    df =  df.iloc[::-1]
    return df

#get recommended range for sensors
def get_sensor_total(sensor='Temperature'):
    if(sensor=='Temperature'): 
        return "18C - 25C"
    elif(sensor=='Moisture'): 
        return "250 - 500"
    elif(sensor=='TDS'): 
        return  "400 - 800"
    elif(sensor=='Light'): 
        return "500 - 1000"
    elif(sensor=='Humidity'): 
        return "30 - 70"
    else:
        return "Error"

#get last value for each sensor
def get_sensor_value(df,sensor='Temperature'):
    return float(df[df['Sensor']==sensor].iloc[:,-1].round(1))

#creating graph from processed data (dependent on selected window in slider)
def fig_sensor_trend(sensor='Temperature',window=3):
    df = process_data(data=data_sensors_ts,sensor=sensor,window=window)
    df.head(10)
    if window==1:
        yaxis_title = "Value for {}".format(sensor)
        fig = px.scatter(df, y= df.columns ,x= df.index, title='Here\'s how your {} levels have been doing over time...'.format(sensor),height=600,color_discrete_sequence =['#0B3B17'])
    else:
        yaxis_title = "Value over the last {} days".format(window) 
        fig = px.line(df, y= df.columns ,x= df.index, title='Here\'s how your {} levels have been doing over time...'.format(sensor),height=600,color_discrete_sequence =['#0B3B17'])
    fig.update_layout(title_x=0.5,plot_bgcolor='#e2e9e2',paper_bgcolor='#e2e9e2',xaxis_title="Date",yaxis_title=yaxis_title)
    return fig

#basic layout - provided theme by dash components
external_stylesheets = [dbc.themes.LUMEN]

#meta information
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = 'Herby'

#layout and generating blocks of website
colors = {
    'background': '#1C1C1C',
    'bodyColor': '#e2e9e2',
    'text': '#F8FCF1'
}
#header style
def get_page_heading_style():
    return {'backgroundColor': '#869182'}

#header - title
def get_page_heading_title():
    return html.H1(children='HI I\'M HERBY',
                                        style={
                                            'margin-top': '20px',
                                            'textAlign': 'center',
                                            'fontSize':'250%',
                                            'color': colors['text']
                                    })
#header - subtitle 
def get_page_heading_subtitle():
    return html.Div(children='I can help you watch your plants grow, no matter where you are!',
                                         style={
                                                'textAlign':'center',
                                                'fontSize':'150%',
                                                'margin-bottom': '15px',
                                                'color':colors['text']
                                         })
#sub header 
def get_sub_page_heading():
    return html.Div(children='Here\'s how your plants are doing today. Don\'t forget to make sure you keep them within their recommended values.',
                                         style={
                                                'margin-top': '20px',
                                                'textAlign':'center',
                                                'fontSize':'100%',
                                                'margin-bottom': '15px'
                                         })

#footer
def get_page_footer_head_title():
    return html.H1(children='Want to know more? Here\'s how you can build your own HERBY at home. Visit our git repo for all the code documentation you\'ll need.',
                                        style={
                                                'margin-top': '20px',
                                                'textAlign': 'center',
                                                'fontSize':'150%',
                                                'color': colors['text']
                                    })

#footer - contact details 
def get_page_pre_footer_subtitle():
    return html.H1(children='https://github.com/joykrupinski/HerbyFinal',
                                        style={
                                                'margin-top': '20px',
                                                'textAlign': 'center',
                                                'fontSize':'110%',
                                                'color': colors['text']
                                    })

#footer - contact details 
def get_page_footer_subtitle():
    return html.H1(children='This is our team: Laura, You-Jin, Arsenius, Seif, Sebastian, Tessa, Zehra, Ella, Joy. If you need more info, message us on joy.krupinski@campus.tu-berlin.de!',
                                        style={
                                                'margin-top': '20px',
                                                'textAlign': 'center',
                                                'fontSize':'120%',
                                                'margin-bottom': '20px',
                                                'color': colors['text']
                                    })


#Header - complete
def generate_page_header():
    main_header =  dbc.Row(
                            [
                                dbc.Col(get_page_heading_title(),md=12)
                            ],
                            align="center",
                            style=get_page_heading_style()
                        )
    subtitle_header = dbc.Row(
                            [
                                dbc.Col(get_page_heading_subtitle(),md=12)
                            ],
                            align="center",
                            style=get_page_heading_style()
                        )
    header = (main_header,subtitle_header)
    return header


#Footer - complete 
def generate_page_footer():
    main_footer =  dbc.Row(
                            [
                                dbc.Col(get_page_footer_head_title(),md=12)
                            ],
                            align="center",
                            style=get_page_heading_style()
                        )
    pre_subtitle_footer = dbc.Row(
                            [
                                dbc.Col(get_page_pre_footer_subtitle(),md=12)
                            ],
                            align="center",
                            style=get_page_heading_style()
                        )
    subtitle_footer = dbc.Row(
                            [
                                dbc.Col(get_page_footer_subtitle(),md=12)
                            ],
                            align="center",
                            style=get_page_heading_style()
                        )
    footer = (main_footer,pre_subtitle_footer,subtitle_footer,)
    return footer

#get sensors for drop down menu
def get_sensor_list():
    return data_sensors_ts['Sensor'].unique() 

#create dropdown menu
def create_dropdown_list(sensor_list):
    dropdown_list = []
    for sensor in sorted(sensor_list):
        tmp_dict = {'label':sensor, 'value':sensor}
        dropdown_list.append(tmp_dict)
    return dropdown_list

#drop down menu layout 
def get_sensor_dropdown(id):
    return html.Div([
                        html.Label('Want to take a closer look at those values?'),
                        dcc.Dropdown(id='my-id'+str(id),
                            options=create_dropdown_list(get_sensor_list()),
                            value='Temperature'
                        ),
                        html.Div(id='my-div'+str(id),style={'textAlign':'center'})
                    ])

#generate graph
def graph1():
    return dcc.Graph(id='graph1',figure=fig_sensor_trend('Temperature')) 

#generate cards with last value of sensor and range
def generate_card_content(card_header,card_value,overall_value):
    card_head_style = {'textAlign':'center','fontSize':'200%'}
    card_body_style = {'textAlign':'center','fontSize':'200%'}
    card_header = dbc.CardHeader(card_header,style=card_head_style)
    card_body = dbc.CardBody(
        [
            html.H5(f"{float(card_value):,}", className="card-title",style=card_body_style),
            html.P(
                "Optimal Range:", overall_value,className="card-text",style={'textAlign':'center'}
            ),
            html.P(
                overall_value, className="card-text",style={'textAlign':'center'}
            ),
        ]
    )
    card = [card_header,card_body]
    return card

#color red/ green depending on value 
def color_condition(sensor, card_value):
    if(sensor == 'Temperature'):
        if(card_value <= 25 and card_value >= 18):
            color = "success"
        else:
            color = "danger"

    if(sensor == 'Moisture'):
        if(card_value <= 500 and card_value >= 250):
            color = "success"
        else:
            color = "danger"

    if(sensor == 'Light'):
        if(card_value >= 500):
            color = "success"
        else:
            color = "danger"

    if(sensor == 'TDS'):
        if(card_value <= 800 and card_value >=400):
            color = "success"
        else:
            color = "danger"

    if(sensor == 'Humidity'):
        if(card_value <= 70 and card_value >= 30):
            color = "success"
        else:
            color = "danger"

    return color

#create cards and call value functions
def generate_cards(sensor='Temperature'):
    cards = html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(dbc.Card(generate_card_content("Temperature",get_sensor_value(data_sensors_ts,'Temperature'),get_sensor_total('Temperature')), color = color_condition('Temperature',get_sensor_value(data_sensors_ts,'Temperature')), inverse=True),md=dict(size=2,offset=1)),
                    dbc.Col(dbc.Card(generate_card_content("Moisture",get_sensor_value(data_sensors_ts,'Moisture'),get_sensor_total('Moisture')), color = color_condition('Moisture',get_sensor_value(data_sensors_ts,'Moisture')), inverse=True),md=dict(size=2)),
                    dbc.Col(dbc.Card(generate_card_content("Light",get_sensor_value(data_sensors_ts,'Light'),get_sensor_total('Light')), color = color_condition('Light',get_sensor_value(data_sensors_ts,'Light')), inverse=True),md=dict(size=2)),
                    dbc.Col(dbc.Card(generate_card_content("Nutrients",get_sensor_value(data_sensors_ts,'TDS'),get_sensor_total('TDS')), color = color_condition('TDS',get_sensor_value(data_sensors_ts,'TDS')), inverse=True),md=dict(size=2)),
                    dbc.Col(dbc.Card(generate_card_content("Humidity",get_sensor_value(data_sensors_ts,'Humidity'),get_sensor_total('Humidity')), color = color_condition('Humidity',get_sensor_value(data_sensors_ts,'Humidity')), inverse=True),md=dict(size=2)),
                ],
                className="mb-5",
            ),
        ],id='card1'
    )
    return cards

#create slider - window for process data and generating graph 
def get_slider():
    return html.Div([  
                        dcc.Slider(
                            id='my-slider',
                            min=1,
                            max=31,
                            step=None,
                            marks={
                                1: 'just 1 day',
                                3: '3 days',
                                5: '5 days',
                                7: 'one week',
                                30: 'a whole month!'
                            },
                            value=3,
                        ),
                        html.Div([html.Label('Slide here to see how your plants have been doing to over time!')],id='my-div'+str(id),style={'textAlign':'center'})
                    ])

#general layout of page 
def generate_layout():
    page_header = generate_page_header()
    page_footer = generate_page_footer()
    layout = dbc.Container(
        [
            page_header[0],
            page_header[1],
            get_sub_page_heading(),
            generate_cards(),
            dbc.Row(
                [
                    dbc.Col(get_sensor_dropdown(id=1),md=dict(size=4,offset=4))                    
                ]
            
            ),
            dbc.Row(
                [                
                    
                    dbc.Col(graph1(),md=dict(size=6,offset=3))
        
                ],
                align="center",

            ),
            dbc.Row(
                [
                    dbc.Col(get_slider(),md=dict(size=8,offset=2))                    
                ]
            
            ),
            html.Hr(),
            page_footer[0],
            page_footer[1],
            page_footer[2],
        ],fluid=True,style={'backgroundColor': colors['bodyColor']}
    )
    return layout


app.layout = generate_layout()

#callbacks for updating information
@app.callback(
    [Output(component_id='graph1',component_property='figure'), #line chart
    Output(component_id='card1',component_property='children')], #overall card numbers
    [Input(component_id='my-id1',component_property='value'), #dropdown
     Input(component_id='my-slider',component_property='value')] #slider
)
def update_output_div(input_value1,input_value2):
    return fig_sensor_trend(input_value1,input_value2),generate_cards(input_value1)

app.run_server(host= '0.0.0.0',debug=True)