from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

swimming = True
watersports = True
wading = False

@auth.route('/coastline')
def coastline():
    return render_template("home.html")

@auth.route('/Specific_Beach_Information')
def login():
    return render_template("Specific Beach information.html")

@auth.route('/General_Beach_Information', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            flash('Account created!', category='success')
    return render_template("General Beach information.html")

@auth.route('/Beach1')
def Beach1():
    swimming = False
    watersports = False
    wading = False
    return render_template("Beach1.html", swimming=swimming, watersports = watersports, wading=wading)

@auth.route('/Beach2')
def Beach2():
    return render_template("Beach2.html", swimming=swimming, watersports = watersports, wading=wading)

@auth.route('/Beach3')
def Beach3():
    return render_template("Beach3.html", swimming=swimming, watersports = watersports, wading=wading)

@auth.route('/Beach4')
def Beach4():
    return render_template("Beach4.html", swimming=swimming, watersports = watersports, wading=wading)

@auth.route('/Beach5')
def Beach5():
    return render_template("Beach5.html", swimming=swimming, watersports = watersports, wading=wading)

@auth.route('/Beach6')
def Beach6():
    return render_template("Beach6.html", swimming=swimming, watersports = watersports, wading=wading)

@auth.route('/Beach7')
def Beach7():
    return render_template("Beach7.html", swimming=swimming, watersports = watersports, wading=wading)

@auth.route('/Beach8')
def Beach8():
    return render_template("Beach8.html", swimming=swimming, watersports = watersports, wading=wading)

@auth.route('/Beach9')
def Beach9():
    return render_template("Beach9.html", swimming=swimming, watersports = watersports, wading=wading)

@auth.route('/Beach10')
def Beach10():
    return render_template("Beach10.html", swimming=swimming, watersports = watersports, wading=wading)