from django.db import models
from authentication.models import User


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

class Proposal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="proposals")
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=PROPOSAL_STATUS, default='Draft')
    created_at = models.DateTimeField(auto_now_add=True)


class ProposalDetail(models.Model):
    proposal = models.OneToOneField(Proposal, on_delete=models.CASCADE,related_name="proposal_detail")
    road_name = models.CharField(max_length=200)
    sanctioned_amt = models.DecimalField(decimal_places=2,max_digits=10)
    road_length = models.DecimalField(decimal_places=2,max_digits=10)
    sanctioned_date = models.DateField()
    proposal_type = models.CharField(max_length=200)
    proposal_sub_type = models.CharField(max_length=200)
    estimated_amt = models.DecimalField(decimal_places=2,max_digits=10)
    verified_by_revenue_dept = models.BooleanField()
    reference_letter = models.FileField(upload_to='pdfs/')


class SupplierBasicDetail(models.Model):
    proposal = models.OneToOneField(Proposal, on_delete=models.CASCADE,related_name="supplier_basic_detail")
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    pincode = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    telephone = models.CharField(max_length=200)
    mob = models.CharField(max_length=200)
    tele_fax = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    web_addr = models.CharField(max_length=200)
    public_ltd = models.BooleanField()
    partnership = models.BooleanField()
    supplier_type = models.CharField(choices=SUPPLIER_TYPES,max_length=200)


class SupplierContactInfo(models.Model):
    proposal = models.OneToOneField(Proposal, on_delete=models.CASCADE,related_name="supplier_contact_info")
    contact_person = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    branch_office = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    pincode = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    telephone = models.CharField(max_length=200)
    mob = models.CharField(max_length=200)
    tele_fax = models.CharField(max_length=200)
    email = models.CharField(max_length=200)


class SupplierTaxDetail(models.Model):
    proposal = models.OneToOneField(Proposal, on_delete=models.CASCADE,related_name="supplier_tax_detail")
    gst_applicable = models.BooleanField()
    tds_applicable = models.BooleanField()
    tcs_applicable = models.BooleanField()
    
class SupplierRegDetail(models.Model):
    proposal = models.OneToOneField(Proposal, on_delete=models.CASCADE,related_name="supplier_reg_detail")
    pan_number = models.CharField(max_length=200)
    gst_number = models.CharField(max_length=200)
    tax_exemption = models.CharField(max_length=200)
    small_scale_reg = models.CharField(max_length=200)
    type_of_msme = models.CharField(max_length=200)
    msme_number = models.CharField(max_length=200)

class SupplierBankDetail(models.Model):
    proposal = models.OneToOneField(Proposal, on_delete=models.CASCADE,related_name="supplier_bank_detail")
    bank_name = models.CharField(max_length=200)
    branch = models.CharField(max_length=200)
    bank_code = models.CharField(max_length=200)
    ifsc_code = models.CharField(max_length=200)
    account_number = models.CharField(max_length=200)


class SupplierAnualTurnover(models.Model):
    proposal = models.OneToOneField(Proposal, on_delete=models.CASCADE,related_name="supplier_annual_to")

    first_fy = models.CharField(max_length=10)
    first_fy_to = models.DecimalField(decimal_places=2,max_digits=10)
    first_fy_doc = models.FileField(upload_to='pdfs/')

    second_fy = models.CharField(max_length=10)
    second_fy_to = models.DecimalField(decimal_places=2,max_digits=10)
    second_fy_doc = models.FileField(upload_to='pdfs/')

    third_fy = models.CharField(max_length=10)
    third_fy_to = models.DecimalField(decimal_places=2,max_digits=10)
    third_fy_doc = models.FileField(upload_to='pdfs/')


class SupplierDocuments(models.Model):
    proposal = models.OneToOneField(Proposal, on_delete=models.CASCADE,related_name="supplier_docs")
    gst_cert = models.FileField(upload_to='pdfs/')
    pancard = models.FileField(upload_to='pdfs/')
    cert_of_incorporation = models.FileField(upload_to='pdfs/')
    msme_cert = models.FileField(upload_to='pdfs/')
    director_aadharcard = models.FileField(upload_to='pdfs/')
    director_pancard = models.FileField(upload_to='pdfs/')
    cancelled_check = models.FileField(upload_to='pdfs/')
    neft_form = models.FileField(upload_to='pdfs/')






