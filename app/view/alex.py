# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 11:59:26 2019

@author: Shadow
"""

<html lang='en'>
<head>
  <meta charset='utf-8'>
  <link rel="shortcut icon" href="data:image/x-icon;," type="image/x-icon"> 

  <link rel='stylesheet' href='../static/style.css'>
  <script src='../static/client.js'></script>
</head>
<body>
<div>
  <div class='center'>
    <div class='title'>Classify Bear Images 🐻</div>
    <p>
      Use images of <strong>teddy</strong> bears, <strong>black</strong> bears, <strong>grizzly</strong> bears, or
      all three!
    </p>
    <div class='content'>
      <div class='no-display'>
        <input id='file-input'
               class='no-display'
               type='file'
               name='file'
               accept='image/*'
               onchange='showPicked(this)'>
      </div>
      <button class='choose-file-button' type='button' onclick='showPicker()'>Select Image</button>
      <div class='upload-label'>
        <label id='upload-label'>No file chosen</label>
      </div>
      <div>
        <img id='image-picked' class='no-display' alt='Chosen Image' height='200'>
      </div>
      <div class='analyze'>
        <button id='analyze-button' class='analyze-button' type='button' onclick='analyze()'>Analyze</button>
      </div>
      <div class='result-label'>
        <label id='result-label'></label>
      </div>
    </div>
  </div>
</div>
</body>
</html>
