from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
import plotly.graph_objs as go
import sqlite3
from fastapi import Depends, Query


app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Connect to SQLite database
conn = sqlite3.connect("health_data.db")
cursor = conn.cursor()

# Create a table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS health_metrics (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        weight REAL,
        blood_pressure TEXT,
        heart_rate INTEGER
    )
''')
conn.commit()

@app.get("/")
async def read_root(request: Request):
    # Fetch health data from the database
    cursor.execute("SELECT * FROM health_metrics")
    rows = cursor.fetchall()

    # Format data for visualization
    health_data = {"id": [], "weight": [], "blood_pressure": [], "heart_rate": []}
    for row in rows:
        health_data["id"].append(row[0])  # Assuming id is the first column in the table
        health_data["weight"].append(row[1])
        health_data["blood_pressure"].append(row[2])
        health_data["heart_rate"].append(row[3])

    # Create a figure for each metric in health_data
    figures = []
    for metric, values in health_data.items():
        if metric == "id":  # Skip 'id' in the visualization
            continue
        fig = go.Figure(data=go.Scatter(x=list(range(len(values))), y=values, mode='lines+markers', name=metric))
        fig.update_layout(title=f'Trend of {metric}', xaxis_title='Time', yaxis_title=metric)
        figures.append(fig.to_html(full_html=False))

    return templates.TemplateResponse("index.html", {"request": request, "health_data": health_data, "figures": figures})


@app.post("/")
async def add_metric(
    weight: float = Form(...),
    blood_pressure: str = Form(...),
    heart_rate: int = Form(...),
):
    # Insert new data into the database
    cursor.execute("INSERT INTO health_metrics (weight, blood_pressure, heart_rate) VALUES (?, ?, ?)", (weight, blood_pressure, heart_rate))
    conn.commit()

    # Redirect to the root page with a success message
    return RedirectResponse("/", status_code=303)

@app.post("/delete")
async def delete_metric(row_id: int = Form(...), redirect: bool = Query(default=True)):
    # Delete data from the database based on the selected row
    cursor.execute("DELETE FROM health_metrics WHERE id=?", (row_id,))
    conn.commit()

    # Redirect to the root page with a success message or updated data
    if redirect:
        return RedirectResponse("/?deleted=true", status_code=303)
    else:
        return {"message": "Record deleted successfully."}

# ... (Other FastAPI code)

@app.on_event("shutdown")
def shutdown_event():
    # Close the SQLite database connection
    conn.close()
