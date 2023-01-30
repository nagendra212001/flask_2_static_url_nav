from flask import Flask,render_template

FAI=Flask(__name__)

@FAI.route('/hai')
def hai():
    return render_template('hai.html')

@FAI.route('/pic')
def pic():
    return render_template('image.html')

if __name__=='__main__':
    FAI.run(debug=True)