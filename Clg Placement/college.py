from flask import Flask,request,render_template,url_for
import joblib
import sklearn


app=Flask(__name__)
model=joblib.load(r"C:\Users\koush\OneDrive\Desktop\Moses k\Innomatics\Data\college_placement.joblib")

@app.route("/")
def f():
    return render_template("index.html")

@app.route("/home",methods=["GET","POST"])
def home():
    if request.method=='POST':
        var1=int(request.form["Gender"])
        var2=float(request.form["Age"])
        var3=float(request.form["Stream"])
        var4=float(request.form["Internships"])
        var5=float(request.form["CGPA"])
        var6=float(request.form["Hostel"])
        var7=int(request.form["Backlogs"])
        predict=model.predict([[var1,var2,var3,var4,var5,var6,var7]])
        return render_template('index.html',predict=predict)
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
