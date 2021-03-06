from django.db import models
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField


GENDER_CHOICES = (
    ('F', 'Female'),
    ('M', 'Male'),
)

ACCOMODATION_CHOICES = (
    ('2P', 'Two Persons'),
    ('3P', 'Three Persons'),
    ('4P', 'Four Persons'),
)

CATEGORY_CHOICES = (
    ('DEL', 'Delegate'),
    ('OFF', 'Official'),
    ('OBS', 'Observer'),
    ('AMB', 'Campus Ambassador'),
)

PREV_CATEGORY_CHOICES = (
    ('DEL', 'Delegate'),
    ('OFF', 'Official'),
    ('OBS', 'Observer'),
)

SHIRT_CHOICES = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('XL', 'Extra Large'),
    ('XXL', 'Extra Extra Large'),
)

POC_CHOICES = (
    ('S', 'Social Media'),
    ('W', 'Website'),
    ('OBS', 'Observer'),
    ('FOR', 'Friend / Relative'),
    ('AMB', 'Campus Ambassador'),
    ('OTH', 'Others'),
)

BINARY_CHOICES = (
    ('Y', 'Yes'),
    ('N', 'No')
)

COMMITTEE_CHOICES = (
    ('UNSC', 'United Nations Security Council'),
    ('DISEC', 'GA1 DISEC'),
    ('UNCHR' ,'United Nations Commission for Human Right'),
    ('ECOFIN', 'GA3 ECOFIN'),
    ('IOC' ,'International Olympic Committee'),
    ('WHO', 'World Health Organization'),
    ('UNESCO', 'United Nations Educational, Scientific and Cultural Organization')
)

class Applicant(models.Model):
    # author = models.ForeignKey('settings.AUTH_USER_MODEL')
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField(
        verbose_name='Date of Birth',
        help_text='Format: DD/MM/YYYY'
    )
    email = models.EmailField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    home_address = models.CharField(max_length=100)
    phone_number = PhoneNumberField(help_text='Enter in international number format')
    country_of_residence = CountryField()
    occupation = models.CharField(max_length=50)
    programme_of_study = models.CharField(max_length=100)
    name_of_institution = models.CharField(max_length=100)
    name_of_Guardian = models.CharField(
        max_length=100, 
        verbose_name='Name of Guardian/Emergency Contact Person'
        )
    relationship_with_applicant = models.CharField(max_length=50)
    contact_number_of_guardian = PhoneNumberField(
        verbose_name='Contact Number of Guardian',
        help_text='Enter in international number format'
        )
    hostel_required = models.CharField(
        verbose_name='Do you require Accomodation?',
        max_length=1,
        choices=BINARY_CHOICES
    )
    choice_of_accomodation = models.CharField(max_length=2, choices=ACCOMODATION_CHOICES, blank=True)
    special_need = models.CharField(
        verbose_name='Do you have a physical/Dietary Need?',
        max_length=1,
        choices=BINARY_CHOICES
    )
    need = models.CharField(
        verbose_name='If yes, specify',
        max_length=50,
        blank=True
    )
    shirt_size = models.CharField(
        verbose_name='Size of Shirt',
        max_length=3, 
        choices=SHIRT_CHOICES
    )
    visa_required = models.CharField(
        verbose_name='Do you require visa to enter Nigeria?',
        max_length=1,
        choices=BINARY_CHOICES
    )
    passport_number = models.CharField(
        max_length=100,
        help_text='If yes, please state your passport number',
        blank=True 
    )
    passport_exp_date = models.DateField(
        verbose_name='Passport Expiry Date',
        help_text='Format: DD/MM/YYYY',
        blank=True,
        null =True
    )
    category = models.CharField(
        verbose_name='Registration Category',
        max_length=3, 
        choices=CATEGORY_CHOICES,
        help_text='Select your category'    
    )
    country_choice_one = CountryField(
        verbose_name='Country of Choice',
        help_text='First most preferred'
    )
    country_choice_two = CountryField(
        verbose_name='Country of Choice',
        help_text='Second most preferred'
    )
    country_choice_three = CountryField(
        verbose_name='Country of Choice',
        help_text='Third most preferred'
    )
    committee_choice = models.CharField(
        max_length=8, 
        verbose_name='Committee of Choice',
        choices=COMMITTEE_CHOICES,
        help_text='Kindly check the "Committees" page for details'
    )
    previous_experience = models.CharField(
        verbose_name='Previous MUN Experience',
        help_text='Do you have any previous Model UN conference experience?',
        max_length=1,
        choices=BINARY_CHOICES
    )
    previous_role = models.CharField(
        verbose_name='Previous Role',
        max_length=3, 
        choices=PREV_CATEGORY_CHOICES, 
        help_text='If yes, please what was your role?',
        blank=True)
    previous_committee = models.CharField(
        verbose_name='Previous Committee',
        max_length=70,
        help_text='Which committee did you participate either as a delegate/official?',
        blank=True
    )
    point_of_contact = models.CharField(
        max_length=3, 
        choices=POC_CHOICES,
        help_text='How did you hear about IFE Model UN conference 2018?')
    referral_code = models.CharField(
        max_length=50,
        help_text='Please enter your referral code? (If referred by a Campus Ambassador )',
        blank=True
    )
    



    def __str__(self):
        return self.first_name + " " + self.last_name