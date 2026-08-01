from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(
    title="LevLake",
    version="0.1.0",
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")


HOME_DATA = {
    "reservations": [
        {
            "family": "Mimi & KJ",
            "start_date": "Friday, August 14",
            "end_date": "Sunday, August 16",
            "status": "Open to family",
            "detail": "2 bedrooms available",
            "color": "mom-dad",
        },
        {
            "family": "Smith's Family",
            "start_date": "Friday, September 4",
            "end_date": "Monday, September 7",
            "status": "Planning started",
            "detail": "8 family members",
            "color": "smith-family",
        },
    ],
    "calendars": [
        {
            "month": "August",
            "year": 2026,
            "weeks": [
                [None, None, None, None, None, None, 1],
                [2, 3, 4, 5, 6, 7, 8],
                [9, 10, 11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20, 21, 22],
                [23, 24, 25, 26, 27, 28, 29],
                [30, 31, None, None, None, None, None],
            ],
            "occupied": {
                14: "mom-dad",
                15: "mom-dad",
                16: "mom-dad",
            },
        },
        {
            "month": "September",
            "year": 2026,
            "weeks": [
                [None, None, 1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10, 11, 12],
                [13, 14, 15, 16, 17, 18, 19],
                [20, 21, 22, 23, 24, 25, 26],
                [27, 28, 29, 30, None, None, None],
            ],
            "occupied": {
                4: "smith-family",
                5: "smith-family",
                6: "smith-family",
                7: "smith-family",
            },
        },
    ],
    "lake_brief": {
        "eyebrow": "Lake Brief",
        "title": "Labor Day Weekend",
        "summary": (
            "Eight family members are planning to be at the lake from "
            "Friday, September 4 through Monday, September 7. Saturday dinner "
            "is nearly covered, though someone still needs to bring ice. "
            "Calm conditions Saturday morning should make it the best time "
            "to get out on the water."
        ),
        
        "cards": [
            {
                "icon": "ice",
                "title": "Ice",
                "detail": "Still needed for the weekend",
                "action": "I’ll bring it",
                "url": "#",
            },
            {
                "icon": "boat",
                "title": "Best boating",
                "detail": "Saturday before noon",
                "action": "View forecast",
                "url": "#",
            },
            {
                "icon": "meal",
                "title": "Saturday dinner",
                "detail": "Brisket and sides",
                "action": "View meal plan",
                "url": "#",
            },
        ],
    },
}


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "title": "Levenson Lake",
            **HOME_DATA,
        },
    )