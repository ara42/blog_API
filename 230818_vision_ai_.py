# -*- coding: utf-8 -*-
"""230818 vision ai .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1w86hzJtHyHFJf_jq7NByV7mcxBxqH984
"""

!pip install google-cloud-vision

from google.cloud import vision
import io
import os
import requests
import re

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'd.json'

def str_filter(text):
    html_spch = ['&quot;','&amp;','&lt;','&gt;','&apos;',
             '&nbsp;','&iexcl;','&cent;','&pound;',
             '&curren;','&yen;','&brvbar;','&sect;',
             '&uml;','&copy;','&ordf;','&laquo;','&not;',
             '&shy;','&reg;','&macr;','&deg;','&plusmn;',
             '&sup2;','&sup3;','&acute;','&micro;','&para;',
             '&middot;','&cedil;','&sup1;','&ordm;','&raquo;',
             '&frac14;','&frac12;','&frac34;','&iquest;']
    html_tag = ['<b>','\n','</b>','<b/>','<a>','</a>','<a/>',
            '<br>','</br>','<br/>','<p>','</p>','<p/>',
            '<strong>','</strong>','<strong/>']
    html_spch_tag = html_spch + html_tag
    or_exp = '|'.join(html_spch_tag)
    text = re.sub(or_exp," ",text)
    text1= re.sub(r'[^\w\s]',' ',text)
    text2= re.sub(r"^\s+|\ㄴ+$","",text1) # 양측 공백 제거
    return text2

def image_text(img_path):
  # Initialize the client
  client = vision.ImageAnnotatorClient()
  # Load the image
  image_link=img_path

  image_response = requests.get(image_link)
  image_content = image_response.content
  image = vision.Image(content=image_content)

  # Perform text detection
  response = client.text_detection(image=image)
  texts = response.text_annotations

  img_text= str(texts[0].description)

  return (img_text)

