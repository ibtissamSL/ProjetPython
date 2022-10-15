import plotly.graph_objects as go

fig = go.Figure()

'''fig.add_trace(
    go.Bar(
        x=["-35.3", "-15.9", "-15.8", "-15.6", "-11.1",
           "-9.6", "-9.2", "-3.5", "-1.9", "-0.9",
           "1.0", "1.4", "1.7", "2.0", "2.8", "6.2",
           "8.1", "8.5", "8.5", "8.6", "11.4", "12.5",
           "13.3", "13.7", "14.4", "17.5", "17.7",
           "18.9", "25.1", "28.9", "41.4"],
        y=["Designers, musicians, artists, etc.",
           "Secretaries and administrative assistants",
           "Waiters and servers", "Archivists, curators, and librarians",
           "Sales and related", "Childcare workers, home car workers, etc.",
           "Food preparation occupations", "Janitors, maids, etc.",
           "Healthcare technicians, assistants. and aides",
           "Counselors, social and religious workers",
           "Physical, life and social scientists", "Construction",
           "Factory assembly workers", "Machinists, repairmen, etc.",
           "Media and communications workers", "Teachers",
           "Mechanics, repairmen, etc.", "Financial analysts and advisers",
           "Farming, fishing and forestry workers",
           "Truck drivers, heavy equipment operator, etc.", "Accountants and auditors",
           "Human resources, management analysts, etc.", "Managers",
           "Lawyers and judges", "Engineers, architects and surveyors",
           "Nurses", "Legal support workers",
           "Computer programmers and system admin.", "Police officers and firefighters",
           "Chief executives", "Doctors, dentists and surgeons"],
        marker=go.bar.Marker(
            color="rgb(253, 240, 54)",
            line=dict(color="rgb(0, 0, 0)",
                      width=2)
        ),
        orientation="h",
    )
)'''

'''# Add image
fig.add_layout_image(
    dict(
        source="https://raw.githubusercontent.com/cldougl/plot_images/add_r_img/vox.png",
        xref="paper", yref="paper",
        x=1, y=1.05,
        sizex=0.2, sizey=0.2,
        xanchor="right", yanchor="bottom"
    )
)'''

# Add image
fig.add_layout_image(
    dict(
        source="https://raw.githubusercontent.com/cldougl/plot_images/add_r_img/vox.png",
       #xref="paper", yref="paper",
        #x=1, y=1.05,
        #sizex=0.2, sizey=0.2,
        xanchor="right", yanchor="bottom"
    )
)



# update layout properties
fig.update_layout(
    autosize=False,
    height=800,
    width=700,
    bargap=0.15,
    bargroupgap=0.1,
    barmode="stack",
    hovermode="x",
    margin=dict(r=20, l=300, b=75, t=125),
    title=("Moving Up, Moving Down<br>" +
           "<i>Percentile change in income between childhood and adulthood</i>"),
)

fig.show()