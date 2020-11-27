#!/usr/bin/env python
# coding: utf-8
import os, sys
from flask import Flask, request,  Response, render_template
from srgan import path_to_img, img_to_img
import tensorflow as tf
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


app = Flask(__name__, template_folder="./templates/")

# Main page
@app.route('/')
def index():
	return render_template('index.html')

@app.route("/healthz", methods=["GET"])
def healthCheck():
   return "", 200

@app.route('/nst_post', methods=['GET','POST'])
def nst_post():
	if request.method == 'POST':
		# Reference Image
		refer_img = request.form['refer_img']
		refer_img_path = 'static/images/'+str(refer_img)

		# User Image (target image)
		user_img_name = request.files['user_img']
		user_img = Image.open(request.files['user_img'])
        
        	# Reformed Reference Image
		ref_transfer_img = path_to_img(refer_img_path)
        
		# Reformed User Image 
		user_transfer_img = img_to_img(user_img)

	return render_template('nst_post.html', 
					refer_img=refer_img_path, user_img=user_img, ref_transfer_img=ref_transfer_img, user_transfer_img=user_transfer_img)

if __name__ == '__main__':
   app.run(host='0.0.0.0', port='80', debug=True)
