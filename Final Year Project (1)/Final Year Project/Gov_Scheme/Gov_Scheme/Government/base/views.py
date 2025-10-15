from django.shortcuts import render
import pickle
import pandas as pd
from django.core.mail import EmailMessage
from django.http import HttpResponse
from sklearn.preprocessing import StandardScaler
global scaler
def home(request):
    return render(request, 'index.html')

def getPredictions(a,b,c,d,e,f,g,h,i):
    model = pickle.load(open('DT.pkl', 'rb'))
    new_data = {'fields.name': a,
            'fields.age': b,
            'fields.email': c,
            'fields.aadhar_no': d,
            'fields.ration_no': e,
            'fields.gender': f,
            'fields.caste': g,
            'fields.education': h,
            'fields.annual_income': i}
    new_df = pd.DataFrame([new_data])
    prediction = model.predict(new_df)
    return (prediction)

def result(request):
    a= str(request.GET['fields.name'])
    b= float(request.GET['fields.age'])
    c = str(request.GET['fields.email'])
    d = float(request.GET['fields.aadhar_no'])
    e = float(request.GET['fields.ration_no'])
    f = str(request.GET['fields.gender'])
    g= str(request.GET['fields.caste'])
    h= str(request.GET['fields.education'])
    i = float(request.GET['fields.annual_income'])
    result = getPredictions(a,b,c,d,e,f,g,h,i)
    if result[0]=='scheme_A':
        res= 'scheme_A'
        subject = 'GOVERNMENT_SCHEME'
        message = 'Moovalur Ramamirtham Ammaiyar Ninaivu Marriage Assistance Scheme'
        from_email = 'praveenjana6@gmail.com'  # Update with your email
        recipient_list = [c]  # Update with the recipient's email
        email=EmailMessage(subject, message, from_email, recipient_list)
        email.attach_file('upload/Marriage.docx')
        try:
        # Send the email
            email.send()
        except Exception as e:
         # Handle exceptions here, you can log the error or take appropriate action
            return HttpResponse(f"An error occurred: {e}", status=500)
    elif result[0]=='scheme_B':
        res= 'scheme_B'
        subject = 'GOVERNMENT_SCHEME'
        message = 'CHIEF MINISTER’S GIRL CHILD PROTECTION SCHEME'
        from_email = 'praveenjana6@gmail.com'  # Update with your email
        recipient_list = [c]  # Update with the recipient's email
        email=EmailMessage(subject, message, from_email, recipient_list)
        email.attach_file('upload/GIRL CHILD PROTECTION SCHEME.docx')
        try:
        # Send the email
            email.send()
        except Exception as e:
         # Handle exceptions here, you can log the error or take appropriate action
            return HttpResponse(f"An error occurred: {e}", status=500)
    elif result[0]=='scheme_C':
        res= 'scheme_C'
        subject = 'GOVERNMENT_SCHEME'
        message = 'Indira Gandhi National Widow Pension Scheme'
        from_email = 'praveenjana6@gmail.com'  # Update with your email
        recipient_list = [c]  # Update with the recipient's email
        email=EmailMessage(subject, message, from_email, recipient_list)
        email.attach_file('upload/Widow Pension.docx')
        try:
        # Send the email
            email.send()
        except Exception as e:
         # Handle exceptions here, you can log the error or take appropriate action
            return HttpResponse(f"An error occurred: {e}", status=500)
    elif result[0]=='scheme_D':
        res= 'scheme_D'
        subject = 'GOVERNMENT_SCHEME'
        message = 'National Means-Cum-Merit Scholarship Scheme'
        from_email = 'praveenjana6@gmail.com'  # Update with your email
        recipient_list = [c]  # Update with the recipient's email
        email=EmailMessage(subject, message, from_email, recipient_list)
        email.attach_file('upload\Merit Scholarship.docx')
        try:
        # Send the email
            email.send()
        except Exception as e:
         # Handle exceptions here, you can log the error or take appropriate action
            return HttpResponse(f"An error occurred: {e}", status=500)
    elif result[0]=='scheme_E':
        res= 'scheme_E'
        subject = 'GOVERNMENT_SCHEME'
        message = 'NSAP - Indira Gandhi National Old Age Pension Scheme'
        from_email = 'praveenjana6@gmail.com'  # Update with your email
        recipient_list = [c]  # Update with the recipient's email
        email=EmailMessage(subject, message, from_email, recipient_list)
        email.attach_file('upload/Old Age Pension.docx')
        try:
        # Send the email
            email.send()
        except Exception as e:
         # Handle exceptions here, you can log the error or take appropriate action
            return HttpResponse(f"An error occurred: {e}", status=500)
    else:
        res= 'No_Scheme'
        subject = 'GOVERNMENT_SCHEME'
        message = 'No_Scheme'
        from_email = 'praveenjana6@gmail.com'  # Update with your email
        recipient_list = [c]  # Update with the recipient's email
        email=EmailMessage(subject, message, from_email, recipient_list)
        try:
        # Send the email
            email.send()
        except Exception as e:
         # Handle exceptions here, you can log the error or take appropriate action
            return HttpResponse(f"An error occurred: {e}", status=500)

    return render(request, 'result.html', {'result': res})