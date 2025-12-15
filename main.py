from flask import Flask,render_template,request
app=Flask(__name__,template_folder="templates",static_folder="static",static_url_path="/")

#defining the route for main page
@app.route("/",methods=["GET","POST"])
def length():
    if request.method=="GET":
        return render_template("index.html")
    if request.method=="POST":
        # All length units converted to meters (base unit) for easy and scalable conversion
        length_factors = {"mm": 0.001,
                            "cm": 0.01,
                            "m": 1,
                            "km": 1000,
                            "inch": 0.0254,
                            "foot": 0.3048,
                            "yard": 0.9144,
                            "mile": 1609.34}
        length=int(request.form.get("length"))
        from_unit=request.form["from"]
        to_unit=request.form["to"]
        # Using meter as the base unit allows conversion between any two units
        # with a single formula: value * from_factor / to_factor
        result=f"{length*length_factors[from_unit]/length_factors[to_unit]} {to_unit}"
        return render_template("result.html",result=result)
#defining the route for weight conversion page
@app.route("/weight-conversion",methods=["GET","POST"])
def weight():
    if request.method=="GET":
        return render_template("weight.html")
    
@app.route("/temperature-conversion",methods=["GET","POST"])
def temp():
    if request.method=="GET":
        return render_template("temp.html")


if __name__=="__main__":
    app.run(debug=True)