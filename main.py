from flask import (Flask, render_template, request, make_response)
from models.user import User
from models.invoice import Invoice
import bootstrap
app = Flask('app')
@app.route('/')
def index():
    # return "success"
    bootstrap.initialize()
    user = User.select().where(
    User.email=="john@doe.com"
    ).get()
    invoice = Invoice.select().where(
      Invoice.user_email == user.email
    ).get()
    total = invoice.design_fee + invoice.hosting_fee + invoice.developer_fee + invoice.domain_fee
    return render_template("invoice.html", user=user, invoice=invoice, total=total)

@app.route('/invoice/generate', methods=['POST','GET'])
def generate():
  invoice = dict(request.form.items())
  total = (int(invoice.get('design_fee'))+
          int(invoice.get('hosting_fee'))+
          int(invoice.get('developer_fee'))+
          int(invoice.get('domain_fee'))
          )
  return render_template('user_generated_invoice.html',     total=total,invoice=invoice)




@app.route('/invoiced', methods=['POST','GET'])
def invoice():
    
   
    invoices = Invoice.select()
    return render_template("invoiced.html", invoices=invoices)




    

@app.route('/invoice/new')
def new_invoice():
  return render_template("invoice_form.html")
    



if __name__== '__main__':
  app.run(host='0.0.0.0',port = 8080) 