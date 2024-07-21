from fastapi import FastAPI, Request, Response, status, HTTPException, Depends, Form, UploadFile, File,Header
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from fastapi.responses import HTMLResponse
from datetime import datetime
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import psycopg2
from psycopg2.extras import RealDictCursor
from time import time

from fastapi.middleware.cors import CORSMiddleware

import time,datetime
from starlette.responses import RedirectResponse






from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

while True:
    try:
        conn=psycopg2.connect(host='localhost',database='postgres',user='bhargav',password='YESHA1496',port='5432',cursor_factory=RealDictCursor)
        cursor=conn.cursor()
        print("database connection successful")
        break
    except Exception as error:
        print("database connection failed12")
        print(error)
        time.sleep(2)
        print("retrying")
        continue



bhargav=FastAPI()

@bhargav.get("/")
async def root():
    cursor.execute("""SELECT * FROM table123""")
    users=cursor.fetchall()
    return users