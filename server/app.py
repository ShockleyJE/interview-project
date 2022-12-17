from flask import Flask, request, Response, jsonify
import pyodbc

app = Flask(__name__)

