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
        length=float(request.form.get("length"))
        from_unit=request.form["from"]
        to_unit=request.form["to"]
        # Using meter as the base unit allows conversion between any two units
        # with a single formula: value * from_factor / to_factor
        result=length*length_factors[from_unit]/length_factors[to_unit]
        return render_template("index.html",result=result,unit=to_unit)
#defining the route for weight conversion page
@app.route("/weight-conversion",methods=["GET","POST"])
def weight():
    if request.method=="GET":
        return render_template("weight.html")
    if request.method=="POST":
        # All length units converted to gram (base unit) for easy and scalable conversion
        weight_factors = {"mg": 0.001,      
                        "g": 1,         
                        "kg": 1000,       
                        "oz": 28.3495,    
                        "lb": 453.592}

        weight=float(request.form.get("weight"))
        from_unit=request.form["from"]
        to_unit=request.form["to"]
        # Using gram as the base unit allows conversion between any two units
        # with a single formula: value * from_factor / to_factor
        result=weight*weight_factors[from_unit]/weight_factors[to_unit]
        return render_template("weight.html",result=result,unit=to_unit)
    
@app.route("/temperature-conversion",methods=["GET","POST"])
def temp():
    if request.method=="GET":
        return render_template("temp.html")
    if request.method=="POST":
        temp=request.form.get("temp")
        from_unit=request.form["from"]
        to_unit=request.form["to"]
        if from_unit==to_unit:
            result=temp
            return render_template("temp.html",result=result,unit=to_unit)
        
        #Converting to base Temp Celcius first
        if from_unit=="C":
            c=temp
        elif from_unit=="F":
            c=(temp-32)*5/9
        elif from_unit=="K":
            c=temp-273.15
       

        # Convert from Celsius to target unit
        if to_unit=="C":
            result=c
        elif to_unit == "F":
            result=(c * 9/5) + 32
        elif to_unit == "K":
            result=c + 273.15
        return render_template("temp.html",result=result,unit=to_unit)

if __name__=="__main__":
    app.run(debug=True)