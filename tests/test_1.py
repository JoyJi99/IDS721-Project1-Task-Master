from app import app
from flask import Flask, render_template, url_for, request, redirect

def test1():
    response = app.test_client().get("/")
    assert response.status_code == 200