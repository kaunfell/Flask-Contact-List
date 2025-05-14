from flask import Flask, redirect, url_for, render_template, request


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", content="testing")


# example list showing on the page
contact_list = [["name1", "lastname1",1111, "email1@email.e"], ["name2",  "lastname2",2222, "email2@email.e"]]


# contacts page func that takes the params from the form 
@app.route("/contacts", methods=["POST", "GET"])
def contacts():
    if request.method == "POST":
        name = request.form["name"]
        lname = request.form["lname"]
        num = request.form["num"]
        email = request.form["email"]
        contact_list.append([name, lname, num, email])
        return redirect(url_for("contacts"))
    else:
        return render_template("contacts.html", contacts=contact_list)

# deletes the contacts
@app.route("/delete/<int:index>")
def delete_contact(index):
        if 0 <= index < len(contact_list):
            contact_list.pop(index)
        return redirect(url_for("contacts"))








if __name__ == '__main__':
    app.run(debug=True)
