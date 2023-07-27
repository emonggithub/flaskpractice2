# Import necessary modules from Flask.

from flask import Flask,render_template,request,redirect,url_for

## Create the Flask application.

app=Flask(__name__)


# Define two routes for displaying success and failure messages with the score. 
# These routes will be accessed when the URL is "/success/int:score" and "/fail/int:score", respectively.

@app.route('/success/<int:score>') # /success is the url while <int:score> is the parameter
def success(score):
    return "The person has passed and the score is "+str(score)

@app.route('/fail/<int:score>')  # /fail is the url
def fail(score):
    return "The person has failed and the score is "+str(score)


@app.route('/calculate', methods=['POST', 'GET'])
def calculate():
    if request.method == 'GET':
        return render_template('calculate.html')  # Renders an HTML form for input
    else:
        # Extracting the marks from the submitted form
        maths = float(request.form['maths'])
        science = float(request.form['science'])
        history = float(request.form['history'])

        # Calculating the average marks
        average_marks = (maths + science + history) / 3
    

        # Determining the result based on average_marks
        result=""
        if average_marks >= 50:
            result = "success"
        else:
            result = "fail"

        # Redirecting to the appropriate route ("/success/<score>" or "/fail/<score>") based on the result
        return redirect(url_for(result,score=average_marks))
    

if __name__=='__main__':
    app.run(debug=True)
       

# Note: The route "/calculate" serves both GET and POST requests.
#  For GET requests, it renders an HTML form named "calculate.html" where users can input their marks.
#  For POST requests (when the form is submitted), it calculates the average marks and redirects the user to either the "/success" or "/fail" route depending on the result.

# The HTML template "calculate.html" is expected to have form fields for "maths," "science," and "history," which users can fill in and submit.


'''
1. /success/<int:score>: This route is used to display a success message along with the calculated score when the average marks are greater than or equal to 50.

2. /fail/<int:score>: This route is used to display a failure message along with the calculated score when the average marks are less than 50.

3. /calculate: This route handles both GET and POST requests. For GET requests, it renders the 'calculate.html' template, which contains a form for inputting marks in maths, science, and history. For POST requests (when the form is submitted), it calculates the average marks and then redirects the user to either the /success/<score> or /fail/<score> route based on the calculated result.

The determination of success or failure is done correctly by checking whether the average_marks are greater than or equal to 50, and the result is stored in the result variable.

The usage of redirect(url_for(result, score=average_marks)) is also correct to redirect to the appropriate route based on the result. The url_for function generates the URL for the specified route (success or fail) with the corresponding score as a parameter.

The if __name__=='__main__': block ensures that the app runs when executed directly, and it sets the debug=True option, which is useful during development for debugging purposes.
'''