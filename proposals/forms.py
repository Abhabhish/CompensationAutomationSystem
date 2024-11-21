from django import forms
from .models import (
    Proposal,
    ProposalDetail,
    SupplierBasicDetail,
    SupplierContactInfo,
    SupplierTaxDetail,
    SupplierRegDetail,
    SupplierBankDetail,
    SupplierAnualTurnover,
    SupplierDocuments,
)


SUPPLIER_TYPES = (
    ('Store & spares supplier','Store & spares supplier'),
    ('Auto spare supplier','Auto spare supplier'),
    ('TPP Spare supplier','TPP Sparesupplier'),
    ('Capital supplier','Capital supplier'),
    ('Contracts','Contracts'),
    ('Service Provider','Service Provider'),
    ('Related Party','Related Party'),
    ('Transporter','Transporter'),
    ('Raw Material Supplier','Raw Material Supplier'),
    ('Coal Supplier','Coal Supplier'),
    ('Packing material Supplier','Packing material Supplier'),
    ('Advertisement','Advertisement'),
    ('Rent','Rent'),
    ('Professional','Professional'),
    ('Any Other..','Any Other..')
)
BUSINESS_TYPES = (
    ('Manufacturer','Manufacturer'),
    ('Distributor / Dealer','Distributor / Dealer'),
    ('Authorised dealership (For traders)','Authorised dealership (For traders)')
)
PROPOSAL_STATUS = [
        ('Draft', 'Draft'),
        ('Submitted', 'Submitted'),
        ('Under Review', 'Under Review'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]

class ProposalForm(forms.ModelForm):
    title = forms.CharField(
        label="Proposal Title",
        widget=forms.TextInput(attrs={'class': 'form-control proposal-title'}),
    )
    class Meta:
        model = Proposal
        fields = ['title'] 


class ProposalDetailForm(forms.ModelForm):
    road_name = forms.CharField(
        label="Road Name",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    sanctioned_amt = forms.DecimalField(
        label="Sanctioned Amount",
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    road_length = forms.DecimalField(
        label="Road Length",
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    sanctioned_date = forms.DateField(
        label="Sanctioned Date",
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    proposal_type = forms.CharField(
        label="Proposal Type",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    proposal_sub_type = forms.CharField(
        label="Proposal Sub-Type",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    estimated_amt = forms.DecimalField(
        label="Estimated Amount",
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    verified_by_revenue_dept = forms.BooleanField(
        label="Verified by Revenue Department",
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    reference_letter = forms.FileField(
        label="Reference Letter",
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = ProposalDetail
        exclude = ['proposal']


class SupplierBasicDetailForm(forms.ModelForm):
    name = forms.CharField(
        label="Name",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    address = forms.CharField(
        label="Address",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    city = forms.CharField(
        label="City",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    state = forms.CharField(
        label="State",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    pincode = forms.CharField(
        label="Pincode",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    country = forms.CharField(
        label="Country",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    telephone = forms.CharField(
        label="Telephone",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    mob = forms.CharField(
        label="Mobile Number",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    tele_fax = forms.CharField(
        label="Telefax",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    web_addr = forms.CharField(
        label="Website Address",
        widget=forms.URLInput(attrs={'class': 'form-control'})
    )
    public_ltd = forms.BooleanField(
        label="Public Limited",
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    partnership = forms.BooleanField(
        label="Partnership",
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    supplier_type = forms.ChoiceField(
        label="Supplier Type",
        choices=SUPPLIER_TYPES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = SupplierBasicDetail
        exclude = ['proposal']


class SupplierContactInfoForm(forms.ModelForm):
    contact_person = forms.CharField(
        label="Contact Person",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    designation = forms.CharField(
        label="Designation",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    phone = forms.CharField(
        label="Phone",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    branch_office = forms.CharField(
        label="Branch Office",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    address = forms.CharField(
        label="Address",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    city = forms.CharField(
        label="City",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    state = forms.CharField(
        label="State",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    pincode = forms.CharField(
        label="Pincode",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    country = forms.CharField(
        label="Country",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    telephone = forms.CharField(
        label="Telephone",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    mob = forms.CharField(
        label="Mobile",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    tele_fax = forms.CharField(
        label="Telefax",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = SupplierContactInfo
        exclude = ['proposal']


class SupplierTaxDetailForm(forms.ModelForm):
    gst_applicable = forms.BooleanField(
        label="GST Applicable",
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    tds_applicable = forms.BooleanField(
        label="TDS Applicable",
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    tcs_applicable = forms.BooleanField(
        label="TCS Applicable",
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

    class Meta:
        model = SupplierTaxDetail
        exclude = ['proposal']


class SupplierRegDetailForm(forms.ModelForm):
    pan_number = forms.CharField(
        label="PAN Number",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    gst_number = forms.CharField(
        label="GST Number",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    tax_exemption = forms.CharField(
        label="Tax Exemption",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    small_scale_reg = forms.CharField(
        label="Small Scale Registration",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    type_of_msme = forms.CharField(
        label="Type of MSME",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    msme_number = forms.CharField(
        label="MSME Number",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = SupplierRegDetail
        exclude = ['proposal']


class SupplierBankDetailForm(forms.ModelForm):
    bank_name = forms.CharField(
        label="Bank Name",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    branch = forms.CharField(
        label="Branch",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    bank_code = forms.CharField(
        label="Bank Code",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    ifsc_code = forms.CharField(
        label="IFSC Code",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    account_number = forms.CharField(
        label="Account Number",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = SupplierBankDetail
        exclude = ['proposal']


class SupplierAnualTurnoverForm(forms.ModelForm):
    first_fy = forms.CharField(
        label="First Financial Year",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    first_fy_to = forms.DecimalField(
        label="Turnover for First Financial Year",
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    first_fy_doc = forms.FileField(
        label="Document for First Financial Year",
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )

    second_fy = forms.CharField(
        label="Second Financial Year",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    second_fy_to = forms.DecimalField(
        label="Turnover for Second Financial Year",
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    second_fy_doc = forms.FileField(
        label="Document for Second Financial Year",
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )

    third_fy = forms.CharField(
        label="Third Financial Year",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    third_fy_to = forms.DecimalField(
        label="Turnover for Third Financial Year",
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    third_fy_doc = forms.FileField(
        label="Document for Third Financial Year",
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = SupplierAnualTurnover
        exclude = ['proposal']


class SupplierDocumentsForm(forms.ModelForm):
    gst_cert = forms.FileField(
        label="GST Certificate",
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )
    pancard = forms.FileField(
        label="PAN Card",
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )
    cert_of_incorporation = forms.FileField(
        label="Certificate of Incorporation",
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )
    msme_cert = forms.FileField(
        label="MSME Certificate",
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )
    director_aadharcard = forms.FileField(
        label="Director Aadhar Card",
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )
    director_pancard = forms.FileField(
        label="Director PAN Card",
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )
    cancelled_check = forms.FileField(
        label="Cancelled Check",
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )
    neft_form = forms.FileField(
        label="NEFT Form",
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = SupplierDocuments
        exclude = ['proposal']
