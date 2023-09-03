import psutil  #to get the CPU monitoring and memory
from flask import Flask, render_template #framework to create the app

app = Flask(__name__)

@app.route("/") #home path-/
def index():
    cpu_percent = psutil.cpu_percent() #cpu utilization
    mem_percent = psutil.virtual_memory().percent #memory usage
    Message = None
    if cpu_percent > 80 or mem_percent > 80:
        Message = "HIGH CPU OR MEMORY UTILIZATION,PLEASE SCALE UP "
    return render_template("index.html",cpu_percent=cpu_percent,mem_percent=mem_percent,message=Message)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    
