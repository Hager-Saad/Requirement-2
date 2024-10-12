from flask import Flask,render_template,request
Req2=Flask(__name__)
#Route 1 : Home Page
@Req2.route('/')
def Form():
    return render_template('Form.html')
#Route 2 : Submit Form 
@Req2.route('/Submit',methods=['POST'])  
def submit():
    #get the form name from the form 
    Name=request.form['Name']
    Age=request.form['Age']
    #pass this data to result page
    return render_template('result.html',Name=Name,Age=Age)
if __name__=='__main__':
    Req2.run()

