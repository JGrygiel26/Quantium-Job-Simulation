from app import app
import dash.html as html

def test_header():
    header = app.layout.children[0].children[0]
    assert isinstance(header, html.H1)

def test_visualisation():
    graph = app.layout.children[1]
    assert graph._type == "Graph"

def test_region_picker():
    region_picker = app.layout.children[0].children[1]
    assert region_picker._type == "RadioItems"