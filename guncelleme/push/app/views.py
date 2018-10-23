from flask import Flask, session, Response,  request
from app import app
import os

class Project:
  def __init__(self, projNo, git_url, targetdir, targeturl):
    self.project = projNo
    if type(projNo) is not int:
      return None
    self.git = git_url
    self.url = targeturl
    self.target = targetdir
    self.tmpdir = "/tmp/push_%d" % projNo
    
  def clear_temp(self):
    os.system("rm -rf %s" % self.tmpdir)
    os.system("mkdir -p %s" % self.tmpdir)
    

  def getcontent(self):
    os.system("cd %s; git clone %s " % (self.tmpdir, self.git))
    
  def build(self, build_type="html" ):
    self.clear_temp()
    self.getcontent()
    projdir = "%s/%s" % (self.tmpdir, self.git.split("/")[-1])
    os.system("cd %s ; make %s" % (projdir, build_type))
    os.system("rm -rf %s_old" % self.target)
    os.system("mv %s %s_old" % (self.target, self.target))
    print("mkdir -p %s/_static" % self.target)
    os.system("mkdir -p %s/_static" % self.target)
    os.system("cp -r %s/_build/html/* %s" % (projdir, self.target))
  
    
projects =  { 
  1: Project(1,"https://github.com/ilkermanap/pyqt", "/var/www/blog/pyqt", "https://blog.manap.se/pyqt")

}

@app.route("/update/<int:project_no>", methods=['GET','POST'])
def update_project(project_no):
  project = projects[project_no]
  project.build()
  return "ok"

@app.route('/', methods=['GET','POST'])
def home():
  s = ""
  for i in projects.values():
    s += "<br><a href=%s>%s</a>\n" % (i.url)

  return '''
    <!doctype html>
    <title>Blog Sayfalari</title>
    <h1>Blog Sayfalari</h1>
    %s
  </html>''' %s

  

  
