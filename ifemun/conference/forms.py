from django import forms

from .models import Applicant

class RegistrationForm(forms.ModelForm):

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
            'postal_address', 
            'home_address',
            'phone_number',
            'country_of_residence',
            'occupation',
            'postal_address', 
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
            'visa_exp_date',
            'category',
            'country_choice_one',
            'country_choice_two',
            'country_choice_three',
            'committee_choice',
            'previous_experience',
            'previous_role',
            'previous_committee',
            'point_of_contact',
    )