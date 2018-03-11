from django import forms

from .models import Applicant

class RegistrationForm(forms.ModelForm):
    dob = forms.DateField(
        required=True, 
        input_formats=['%Y-%m-%d', '%d-%m-%Y', '%d/%m/%Y', '%d/%m/%y'],
        label='Date of Birth', 
        help_text='Format: DD/MM/YYYY')
    passport_exp_date = forms.DateField(
        required=False, 
        input_formats=['%Y-%m-%d', '%d-%m-%Y', '%d/%m/%Y', '%d/%m/%y'],
        label='Passport Expiry Date', 
        help_text='Format: DD/MM/YYYY')
    class Meta:
        model = Applicant
        fields = (
            'first_name',
            'middle_name', 
            'last_name', 
            'gender', 
            'dob',
            'email',
            'gender',
            'home_address',
            'phone_number',
            'country_of_residence',
            'occupation',
            'programme_of_study',
            'name_of_institution',
            'name_of_Guardian',
            'relationship_with_applicant',
            'contact_number_of_guardian',
            'hostel_required',
            'choice_of_accomodation',
            'special_need',
            'need',
            'shirt_size',
            'visa_required',
            'passport_number',
            'passport_exp_date',
            'category',
            'country_choice_one',
            'country_choice_two',
            'country_choice_three',
            'committee_choice',
            'previous_experience',
            'previous_role',
            'previous_committee',
            'point_of_contact',
            'referral_code'
    )