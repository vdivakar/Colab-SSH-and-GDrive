# Colab-SSH-and-GDrive
A convenient way to utilize Colab GPUs and save the progress from your local Terminal. SSH into Colab notebook with access to your google drive. 


## Steps
1. Create your free account at [ngrok](https://ngrok.com) and get the **authtoken.** This will be used in Step4.<br>
Should look like `$ ./ngrok authtoken ZT64bWYnXsdTAdfdassJej42auAQqKqZHn2Sh4g2sfAD`
2. Get the public key of your local machine. <br>
`$ ssh-keygen`<br>
`$ cat .ssh/id_rsa.pub`
3. Go to your colab notebook. Copy the content from template provided above (*ssh_colab.ipynb*).
4. Execute the colab notebook. Mount your Google Drive. When prompted, enter the authtoken obtained in Step1. Lastly, it will ask the public key of your local machine obtained in Step2.
5. Now you should get output something like `ssh root@0.tcp.ngrok.io -p 12**6`. The port will be different for your case. Go to your local machine and run this ssh command. **Done!**

<br>By default, you will be inside a temporary space and its content will be deleted once your Colab session ends. If you want to save your work, you should explicitly save your changes in the mounted google drive.
<br>Your Google Drive files will be present in `/content/gdrive/My Drive/` <br>


![Screenshot](https://github.com/vdivakar/Colab-SSH-and-GDrive/blob/master/Images/Terminal_img.png)

<br>

## Extra: 
### Steps for running a JupyterLab instance on top of it:<br>
1. Execute the following commands:<br>
```apt-get install tmux && pip install jupyter lab``` <br>
```tmux```<br>
`jupyter lab --ip 0.0.0.0 --port 56784`
2. Split the same terminal: <kbd>Ctrl</kbd>+<kbd>b</kbd> & <kbd>Shift</kbd>+<kbd>"</kbd>
3. Execute `ssh -R 80:localhost:56784 something@ssh.localhost.run` <br>
You should get an output like this:<br>
`Connect to http://something-caa4e22c.localhost.run or https://something-caa4e22c.localhost.run`
Connect to this url in your PC browser. Done!
<br>

![Screenshot](https://github.com/vdivakar/Colab-SSH-and-GDrive/blob/master/Images/Terminal_2.png)
<br>
![Screenshot](https://github.com/vdivakar/Colab-SSH-and-GDrive/blob/master/Images/Terminal_3.png)
<br>
![Screenshot](https://github.com/vdivakar/Colab-SSH-and-GDrive/blob/master/Images/Jupyter.png)
<br><br><br>
References:<br>
	1. https://imadelhanafi.com/posts/google_colal_server/<br>
	2. https://medium.com/@archie9211/guide-to-connect-to-google-colab-with-ssh-from-terminal-and-run-jupyter-lab-7ed60258368 <br>
