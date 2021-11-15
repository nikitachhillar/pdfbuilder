from django import forms

class Details(forms.Form):
    id=forms.IntegerField(label='Id', required=True)
    sname=forms.CharField(label='Seller Name', required=True)
    sphone=forms.IntegerField(label='Seller Phone', required=True)
    saddress=forms.CharField(label='Seller Address', required=True)
    cname=forms.CharField(label='Customer Name', required=True)
    cphone=forms.IntegerField(label='Customer Phone', required=True)
    caddress=forms.CharField(label='Customer Address', required=True)
    item1=forms.CharField(label='Item 1', required=True)
    quantity1=forms.CharField(label='Quantity 1', required=True)
    price1=forms.CharField(label='Price 1', required=True)
    item2=forms.CharField(label='Item 2', required=True)
    quantity2=forms.CharField(label='Quantity 2', required=True)
    price2=forms.CharField(label='Price 2', required=True)
    date=forms.DateField(label='Today\'s Date', required=True)
    
