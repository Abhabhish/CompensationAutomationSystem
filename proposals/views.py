from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Proposal
from .forms import (
    ProposalForm,
    ProposalDetailForm,
    SupplierBasicDetailForm,
    SupplierContactInfoForm,
    SupplierTaxDetailForm,
    SupplierRegDetailForm,
    SupplierBankDetailForm,
    SupplierAnualTurnoverForm,
    SupplierDocumentsForm
)

# Create a new proposal
def create_proposal(request):
    if request.method == "POST":
        form = ProposalForm(request.POST)
        if form.is_valid():
            proposal = form.save(commit=False)
            proposal.user = request.user  # Set current user
            proposal.save()
            return redirect('edit_proposal', proposal_id=proposal.id, section='proposal')
    else:
        form = ProposalForm()
    return render(request, "proposals/create_proposal.html", {'form': form})

# Edit a specific section of the proposal
def edit_proposal(request, proposal_id, section):
    proposal = get_object_or_404(Proposal, id=proposal_id, user=request.user)

    forms = {
        "proposal": ProposalForm(instance=proposal),
        "details": ProposalDetailForm(instance=proposal.proposal_detail),
        "supplier_basic": SupplierBasicDetailForm(instance=proposal.supplier_basic_detail),
        "supplier_contact": SupplierContactInfoForm(instance=proposal.supplier_contact_info),
        "supplier_tax": SupplierTaxDetailForm(instance=proposal.supplier_tax_detail),
        "supplier_reg": SupplierRegDetailForm(instance=proposal.supplier_reg_detail),
        "supplier_bank": SupplierBankDetailForm(instance=proposal.supplier_bank_detail),
        "supplier_turnover": SupplierAnualTurnoverForm(instance=proposal.supplier_annual_to),
        "supplier_docs": SupplierDocumentsForm(instance=proposal.supplier_docs),
    }

    if section not in forms:
        return JsonResponse({"status": "error", "message": "Invalid section"}, status=400)

    form = forms[section]
    
    if request.method == "POST":
        form = forms[section](request.POST, request.FILES, instance=proposal)
        if form.is_valid():
            form.save()  # Save the form
            return JsonResponse({"status": "success", "message": f"{section.capitalize()} section updated successfully"})
        else:
            return JsonResponse({"status": "error", "message": "Validation failed"}, status=400)

    return render(request, "proposals/edit_proposal_section.html", {
        'form': form,
        'section': section,
        'proposal': proposal
    })

