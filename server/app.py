from flask import Flask, request, Response, jsonify
import pyodbc

app = Flask(__name__)

"""
Stand up our api endpoints
"""
from server.ex_endpoints import api_get_tables
