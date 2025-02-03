import random
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _

class Loan(models.Model):
    class LoanType(models.TextChoices):
        HOME_LOAN = 'Home Loan', _('Home Loan')
        PREGNANCY_LOAN = 'Pregnancy Loan', _('Pregnancy Loan')
        OTHER_LOAN = 'Other Loan', _('Other Loan')

    loan_type = models.CharField(
        max_length=255,
        choices=LoanType.choices,
        verbose_name=_('Loan Type')
    )
    name = models.CharField(max_length=255, verbose_name=_('Loan Name'))
    interest_rate = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name=_('Interest Rate'),
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    max_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_('Maximum Amount')
    )
    min_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_('Minimum Amount')
    )
    max_tenure = models.PositiveIntegerField(verbose_name=_('Maximum Tenure (Months)'))
    min_tenure = models.PositiveIntegerField(verbose_name=_('Minimum Tenure (Months)'))

    class Meta:
        verbose_name = _('Loan')
        verbose_name_plural = _('Loans')

    def __str__(self):
        return self.name


class Office(models.Model):
    class PositionCategory(models.TextChoices):
        DARBANDI = 'Darbandi', _('Darbandi')
        KAAJ = 'Kaaj', _('Kaaj')

    duration = models.DurationField(verbose_name=_('Duration'))
    office_name = models.CharField(max_length=255, verbose_name=_('Office Name'))
    position = models.CharField(max_length=255, verbose_name=_('Position'))
    position_category = models.CharField(
        max_length=255,
        choices=PositionCategory.choices,
        verbose_name=_('Position Category')
    )

    class Meta:
        verbose_name = _('Office')
        verbose_name_plural = _('Offices')

    def __str__(self):
        return self.office_name


class Awards(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Award Name'))
    description = models.TextField(verbose_name=_('Description'))
    file = models.FileField(
        upload_to='awards/%Y/%m/%d/',
        null=True,
        blank=True,
        verbose_name=_('Award File')
    )

    class Meta:
        verbose_name = _('Award')
        verbose_name_plural = _('Awards')

    def __str__(self):
        return self.name


class Punishments(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Punishment Name'))
    description = models.TextField(verbose_name=_('Description'))
    file = models.FileField(
        upload_to='punishments/%Y/%m/%d/',
        null=True,
        blank=True,
        verbose_name=_('Punishment File')
    )

    class Meta:
        verbose_name = _('Punishment')
        verbose_name_plural = _('Punishments')

    def __str__(self):
        return self.name


class Education(models.Model):
    class EducationLevel(models.TextChoices):
        SLC = 'SLC', _('SLC')
        PLUS_TWO = '+2', _('+2')
        BACHELOR = 'Bachelor', _('Bachelor')
        MASTER = 'Master', _('Master')
        PHD = 'PhD', _('PhD')

    education_level = models.CharField(
        max_length=255,
        choices=EducationLevel.choices,
        verbose_name=_('Education Level')
    )
    institution = models.CharField(max_length=255, verbose_name=_('Institution'))
    board = models.CharField(max_length=255, verbose_name=_('Board'))
    percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name=_('Percentage'),
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    year = models.PositiveIntegerField(verbose_name=_('Year'))
    certificate = models.FileField(
        upload_to='education/certificates/%Y/%m/%d/',
        null=True,
        blank=True,
        verbose_name=_('Certificate')
    )
    marksheets = models.FileField(
        upload_to='education/marksheets/%Y/%m/%d/',
        null=True,
        blank=True,
        verbose_name=_('Marksheets')
    )

    class Meta:
        verbose_name = _('Education')
        verbose_name_plural = _('Educations')

    def __str__(self):
        return self.institution


class Department(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Department Name'))
    description = models.TextField(verbose_name=_('Description'))

    class Meta:
        verbose_name = _('Department')
        verbose_name_plural = _('Departments')

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    class EmployeeType(models.TextChoices):
        PERMANENT = 'Permanent', _('Permanent')
        CONTRACT = 'Contract', _('Contract')
        TEMPORARY = 'Temporary', _('Temporary')

    class Province(models.TextChoices):
        PROVINCE_1 = 'Koshi', _('Koshi')
        PROVINCE_2 = 'Madhesh', _('Madhesh')
        PROVINCE_3 = 'Bagmati', _('Bagmati')
        PROVINCE_4 = 'Gandaki', _('Gandaki')
        PROVINCE_5 = 'Lumbini', _('Lumbini')
        PROVINCE_6 = 'Karnali', _('Karnali')
        PROVINCE_7 = 'Sudurpaschim', _('Sudurpaschim')

    class Bank(models.TextChoices):
        NEPAL_BANK = 'Nepal Bank Ltd.', _('Nepal Bank Ltd.')
        AGRICULTURE_BANK = 'Agriculture Development Bank Ltd.', _('Agriculture Development Bank Ltd.')
        NABIL_BANK = 'Nabil Bank Ltd.', _('Nabil Bank Ltd.')
        NEPAL_INVESTMENT_BANK = 'Nepal Investment Bank Ltd.', _('Nepal Investment Bank Ltd.')
        STANDARD_CHARTERED = 'Standard Chartered Bank Nepal Ltd.', _('Standard Chartered Bank Nepal Ltd.')
        HIMALAYAN_BANK = 'Himalayan Bank Ltd.', _('Himalayan Bank Ltd.')
        NEPAL_SBI_BANK = 'Nepal SBI Bank Ltd.', _('Nepal SBI Bank Ltd.')
        EVEREST_BANK = 'Everest Bank Ltd.', _('Everest Bank Ltd.')
        NIC_ASIA_BANK = 'NIC ASIA Bank Ltd.', _('NIC ASIA Bank Ltd.')
        MACHHAPUCHCHHRE_BANK = 'Machhapuchchhre Bank Ltd.', _('Machhapuchchhre Bank Ltd.')
        KUMARI_BANK = 'Kumari Bank Ltd.', _('Kumari Bank Ltd.')
        LAXMI_BANK = 'Laxmi Bank Ltd.', _('Laxmi Bank Ltd.')
        SIDDHARTHA_BANK = 'Siddhartha Bank Ltd.', _('Siddhartha Bank Ltd.')
        GLOBAL_IME_BANK = 'Global IME Bank Ltd.', _('Global IME Bank Ltd.')
        CITIZENS_BANK = 'Citizens Bank International Ltd.', _('Citizens Bank International Ltd.')
        PRIME_BANK = 'Prime Commercial Bank Ltd.', _('Prime Commercial Bank Ltd.')
        NMB_BANK = 'NMB Bank Ltd.', _('NMB Bank Ltd.')
        PRABHU_BANK = 'Prabhu Bank Ltd.', _('Prabhu Bank Ltd.')
        SANIMA_BANK = 'Sanima Bank Ltd.', _('Sanima Bank Ltd.')
        MAHALAXMI_BANK = 'Mahalaxmi Bikas Bank Ltd.', _('Mahalaxmi Bikas Bank Ltd.')
        NARAYANI_BANK = 'Narayani Development Bank Ltd.', _('Narayani Development Bank Ltd.')
        KARNALI_BANK = 'Karnali Development Bank Ltd.', _('Karnali Development Bank Ltd.')
        SHANGRILLA_BANK = 'Shangrila Development Bank Ltd.', _('Shangrila Development Bank Ltd.')
        EXCEL_BANK = 'Excel Development Bank Ltd.', _('Excel Development Bank Ltd.')
        MITERI_BANK = 'Miteri Development Bank Ltd.', _('Miteri Development Bank Ltd.')
        MUKTINATH_BANK = 'Muktinath Bikas Bank Ltd.', _('Muktinath Bikas Bank Ltd.')
        GARIMA_BANK = 'Garima Bikas Bank Ltd.', _('Garima Bikas Bank Ltd.')
        KAMANA_BANK = 'Kamana Sewa Bikas Bank Ltd.', _('Kamana Sewa Bikas Bank Ltd.')
        CORPORATE_BANK = 'Corporate Development Bank Ltd.', _('Corporate Development Bank Ltd.')
        JYOTI_BANK = 'Jyoti Bikas Bank Ltd.', _('Jyoti Bikas Bank Ltd.')
        SHINE_RESUNGA_BANK = 'Shine Resunga Development Bank Ltd.', _('Shine Resunga Development Bank Ltd.')
        LUMBINI_BANK = 'Lumbini Bikas Bank Ltd.', _('Lumbini Bikas Bank Ltd.')
        SINDHU_BANK = 'Sindhu Bikas Bank Ltd.', _('Sindhu Bikas Bank Ltd.')
        SALAPA_BANK = 'Salapa Bikas Bank Ltd.', _('Salapa Bikas Bank Ltd.')
        SAPTAKOSHI_BANK = 'Saptakoshi Development Bank Ltd.', _('Saptakoshi Development Bank Ltd.')
        GREEN_BANK = 'Green Development Bank Ltd.', _('Green Development Bank Ltd.')
        NEPAL_FINANCE = 'Nepal Finance Ltd.', _('Nepal Finance Ltd.')
        NEPAL_SHARE_MARKETS = 'Nepal Share Markets and Finance Ltd.', _('Nepal Share Markets and Finance Ltd.')
        GURKHAS_FINANCE = 'Gurkhas Finance Ltd.', _('Gurkhas Finance Ltd.')
        GOODWILL_FINANCE = 'Goodwill Finance Ltd.', _('Goodwill Finance Ltd.')
        SHREE_INVESTMENT = 'Shree Investment & Finance Co.', _('Shree Investment & Finance Co.')
        BEST_FINANCE = 'Best Finance Ltd.', _('Best Finance Ltd.')
        CAPITAL_MERCHANT_BANKING = 'Capital Merchant Banking & Finance Ltd.', _('Capital Merchant Banking & Finance Ltd.')
        CENTRAL_FINANCE = 'Central Finance Ltd.', _('Central Finance Ltd.')
        GUHESHWORI_MERCHANT_BANKING = 'Guheshwori Merchant Banking & Finance Ltd.', _('Guheshwori Merchant Banking & Finance Ltd.')
        ICFC_FINANCE = 'ICFC Finance Ltd.', _('ICFC Finance Ltd.')
        JANAKI_FINANCE = 'Janaki Finance Co. Ltd.', _('Janaki Finance Co. Ltd.')
        MANJUSHREE_FINANCE = 'Manjushree Finance Ltd.', _('Manjushree Finance Ltd.')
        MULTIPURPOSE_FINANCE = 'Multipurpose Finance Co. Ltd.', _('Multipurpose Finance Co. Ltd.')
        POKHARA_FINANCE = 'Pokhara Finance Ltd.', _('Pokhara Finance Ltd.')
        PROGRESSIVE_FINANCE = 'Progressive Finance Ltd.', _('Progressive Finance Ltd.')
        RELIANCE_FINANCE = 'Reliance Finance Ltd.', _('Reliance Finance Ltd.')
        SAMRIDDHI_FINANCE = 'Samriddhi Finance Co. Ltd.', _('Samriddhi Finance Co. Ltd.')
        NEPAL_BANGLADESH_BANK = 'Nepal Bangladesh Bank Ltd.', _('Nepal Bangladesh Bank Ltd.')
        NEPAL_CREDIT_COMMERCE = 'Nepal Credit and Commerce Bank Ltd.', _('Nepal Credit and Commerce Bank Ltd.')
        NEPAL_RASTRA_BANK = 'Nepal Rastra Bank', _('Nepal Rastra Bank')
        NEPAL_GRAMEEN_BIKAS = 'Nepal Grameen Bikas Bank Ltd.', _('Nepal Grameen Bikas Bank Ltd.')
        NEPAL_INFRASTRUCTURE = 'Nepal Infrastructure Bank Ltd. (NIFRA)', _('Nepal Infrastructure Bank Ltd. (NIFRA)')

    # Permanent Address
    perm_state = models.CharField(
        max_length=255,
        choices=Province.choices,
        verbose_name=_('Permanent State')
    )
    perm_district = models.CharField(max_length=255, verbose_name=_('Permanent District'))
    perm_municipality = models.CharField(max_length=255, verbose_name=_('Permanent Municipality'))
    perm_ward_no = models.CharField(max_length=255, verbose_name=_('Permanent Ward No.'))

    # Temporary Address
    temp_state = models.CharField(
        max_length=255,
        choices=Province.choices,
        verbose_name=_('Temporary State')
    )
    temp_district = models.CharField(max_length=255, verbose_name=_('Temporary District'))
    temp_municipality = models.CharField(max_length=255, verbose_name=_('Temporary Municipality'))
    temp_ward_no = models.CharField(max_length=255, verbose_name=_('Temporary Ward No.'))

    # Citizenship Details
    citizenship_id = models.CharField(
        max_length=255,
        unique=True,
        verbose_name=_('Citizenship ID')
    )
    citizenship_date_of_issue = models.DateField(
        null=True,
        blank=True,
        verbose_name=_('Citizenship Date of Issue')
    )
    citizenship_district = models.CharField(
        max_length=255,
        verbose_name=_('Citizenship District')
    )
    citizenship_front_image = models.ImageField(
        upload_to='citizenship/front/%Y/%m/%d/',
        null=True,
        blank=True,
        verbose_name=_('Citizenship Front Image')
    )
    citizenship_back_image = models.ImageField(
        upload_to='citizenship/back/%Y/%m/%d/',
        null=True,
        blank=True,
        verbose_name=_('Citizenship Back Image')
    )

    # Personal Details
    hire_date = models.DateField(null=True, blank=True)
    recess_date = models.DateField(null=True, blank=True)
    father_name = models.CharField(max_length=255, verbose_name=_('Father Name'))
    mother_name = models.CharField(max_length=255, verbose_name=_('Mother Name'))
    grand_father_name = models.CharField(max_length=255, verbose_name=_('Grand Father Name'))
    home_number = models.CharField(max_length=255, verbose_name=_('Home Number'))
    phone_number = models.CharField(max_length=255, verbose_name=_('Phone Number'))
    mobile_number = models.CharField(max_length=255, verbose_name=_('Mobile Number'))
    date_joined = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Date Joined'),
        null=True,
        blank=True
    )
    recess_date = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name=_('Recess Date')
    )
    position = models.CharField(max_length=255, verbose_name=_('Position'))
    position_category = models.CharField(
        max_length=255,
        choices=Office.PositionCategory.choices,
        verbose_name=_('Position Category')
    )

    # Employee Details
    employee_id = models.CharField(
        max_length=255,
        unique=True,
        verbose_name=_('Employee ID')
    )
    employee_type = models.CharField(
        max_length=255,
        choices=EmployeeType.choices,
        verbose_name=_('Employee Type')
    )
    na_la_kos_no = models.CharField(max_length=255, verbose_name=_('Na La Kos No.'))
    accumulation_fund_no = models.CharField(
        max_length=255,
        verbose_name=_('Accumulation Fund No.')
    )
    bank_account_no = models.CharField(
        max_length=255,
        verbose_name=_('Bank Account No.')
    )
    bank_name = models.CharField(
        max_length=255,
        choices=Bank.choices,
        verbose_name=_('Bank Name')
    )

    # Relationships
    awards = models.OneToOneField(
        Awards,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='user_awards',
        verbose_name=_('Awards')
    )
    punishments = models.OneToOneField(
        Punishments,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='user_punishments',
        verbose_name=_('Punishments')
    )
    loan = models.OneToOneField(
        Loan,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='user_loans',
        verbose_name=_('Loan')
    )
    education = models.OneToOneField(
        Education,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='user_education',
        verbose_name=_('Education')
    )
    office = models.OneToOneField(
        Office,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='user_office',
        verbose_name=_('Office')
    )

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.username
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    groups = models.ManyToManyField(Group, related_name="customuser_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="customuser_permissions", blank=True)

    # Dynamic district and municipality choices based on the state
    def get_district_choices(state):
        # Province data with respective districts
        province_data = {
            "Koshi": ["Jhapa", "Morang", "Sunsari", "Bhojpur", "Ilam", "Khotang", "Okhaldhunga", "Panchthar", "Sankhuwasabha", "Solukhumbu", "Taplejung", "Terhathum", "Udayapur"],
            "Madhesh": ["Saptari", "Dhanusha", "Mahottari", "Sarlahi", "Siraha", "Bara", "Parsa", "Rautahat", "Chhathapol"],
            "Bagmati": ["Kathmandu", "Bhaktapur", "Lalitpur", "Kavrepalanchok", "Nuwakot", "Rasuwa", "Sindhuli", "Sindhupalchok", "Chitwan", "Makawanpur", "Bhaktapur", "Nawalparasi", "Tanahu"],
            "Gandaki": ["Kaski", "Parbat", "Tanahun", "Gorkha", "Lamjung", "Manang", "Mustang", "Syangja", "Nawalparasi", "Syangja"],
            "Lumbini": ["Rupandehi", "Kapilvastu", "Palpa", "Nawalparasi", "Arghakhanchi", "Rukum", "Salyan", "Dang", "Banke", "Bardiya"],
            "Karnali": ["Surkhet", "Dailekh", "Jajarkot", "Jumla", "Kalikot", "Mugu", "Humla", "Dolpa", "Rukum", "Salyan"],
            "Sudurpaschim": ["Kanchanpur", "Baitadi", "Darchula", "Achham", "Kailali", "Bajura", "Bajhang", "Dadeldhura", "Doti", "Dadeldhura"]
        }
        return province_data.get(state, [])

    def get_municipality_choices(state, district):
        # Expanded data for municipalities (to be filled with your data)
        district_municipality_data = {
           # Koshi Province (Province 1)
            "Bhojpur": [
                "Bhojpur Municipality", "Shadananda Municipality",
                "Hatuwagadhi Rural Municipality", "Aamchowk Rural Municipality",
                "Arun Rural Municipality", "Pauwadungma Rural Municipality",
                "Ramprasad Rai Rural Municipality", "Salpasilichho Rural Municipality",
                "Tyamke Maiyum Rural Municipality"
            ],
            "Dhankuta": [
                "Dhankuta Municipality", "Pakhribas Municipality",
                "Mahalaxmi Municipality", "Chhathar Jorpati Rural Municipality",
                "Shahidbhumi Rural Municipality", "Sangurigadhi Rural Municipality"
            ],
            "Ilam": [
                "Ilam Municipality", "Deumai Municipality", "Mai Municipality",
                "Suryodaya Municipality", "Fakfokthum Rural Municipality",
                "Chulachuli Rural Municipality", "Mangsebung Rural Municipality",
                "Maijogmai Rural Municipality", "Rong Rural Municipality",
                "Sandakpur Rural Municipality"
            ],
            "Jhapa": [
                "Bhadrapur Municipality", "Birtamod Municipality", "Damak Municipality",
                "Mechinagar Municipality", "Kankai Municipality", "Shivasatakshi Municipality",
                "Arjundhara Municipality", "Buddhashanti Rural Municipality",
                "Barhadashi Rural Municipality", "Gauriganj Rural Municipality",
                "Gauradaha Municipality", "Haldibari Rural Municipality",
                "Jhapa Rural Municipality", "Kamal Rural Municipality"
            ],
            "Khotang": [
                "Diktel Rupakot Majhuwagadhi Municipality", "Halesi Tuwachung Municipality",
                "Aiselukharka Rural Municipality", "Barahapokhari Rural Municipality",
                "Diprung Chuichumma Rural Municipality", "Jantedhunga Rural Municipality",
                "Khotehang Rural Municipality", "Lamidanda Rural Municipality",
                "Rawabesi Rural Municipality", "Sakela Rural Municipality"
            ],
            "Morang": [
                "Biratnagar Metropolitan City", "Sundar Haraicha Municipality",
                "Belbari Municipality", "Pathari Sanischare Municipality",
                "Rangeli Municipality", "Letang Municipality",
                "Ratuwamai Municipality", "Urlabari Municipality",
                "Katahari Rural Municipality", "Kerabari Rural Municipality",
                "Gramthan Rural Municipality", "Miklajung Rural Municipality",
                "Budhiganga Rural Municipality", "Dhanpalthan Rural Municipality"
            ],
            "Okhaldhunga": [
                "Siddhicharan Municipality", "Molung Rural Municipality",
                "Champadevi Rural Municipality", "Khijidemba Rural Municipality",
                "Likhu Rural Municipality", "Manebhanjyang Rural Municipality",
                "Chisankhugadhi Rural Municipality"
            ],
            "Panchthar": [
                "Phidim Municipality", "Hilihang Rural Municipality",
                "Kummayak Rural Municipality", "Miklajung Rural Municipality",
                "Tumbewa Rural Municipality", "Yangwarak Rural Municipality",
                "Falelung Rural Municipality"
            ],
            "Sankhuwasabha": [
                "Khandbari Municipality", "Dharan Sub-Metropolitan City",
                "Chainpur Municipality", "Madi Municipality",
                "Makalu Rural Municipality", "Bhotkhola Rural Municipality",
                "Chichila Rural Municipality", "Silichong Rural Municipality",
                "Sabhapokhari Rural Municipality"
            ],
            "Solukhumbu": [
                "Solu Dudhkunda Municipality", "Khumbu Pasang Lhamu Rural Municipality",
                "Necha Salyan Rural Municipality", "Mahakulung Rural Municipality",
                "Likhupike Rural Municipality", "Thulung Dudhkoshi Rural Municipality",
                "Mapya Dudhkoshi Rural Municipality"
            ],
            "Sunsari": [
                "Dharan Sub-Metropolitan City", "Itahari Sub-Metropolitan City",
                "Inaruwa Municipality", "Duhabi Municipality",
                "Ramnagar Bhulke Municipality", "Harinagara Rural Municipality",
                "Dewanganj Rural Municipality", "Koshi Rural Municipality",
                "Barju Rural Municipality", "Gadhi Rural Municipality",
                "Bhokraha Narsingh Rural Municipality"
            ],
            "Taplejung": [
                "Phungling Municipality", "Aathrai Tribeni Rural Municipality",
                "Maiwakhola Rural Municipality", "Mikwa Khola Rural Municipality",
                "Meringden Rural Municipality", "Phaktanglung Rural Municipality",
                "Sidingwa Rural Municipality", "Sirijunga Rural Municipality",
                "Pathivara Yangwarak Rural Municipality"
            ],
            "Terhathum": [
                "Myanglung Municipality", "Laligurans Municipality",
                "Chhathar Rural Municipality", "Menchayam Rural Municipality",
                "Phedap Rural Municipality", "Aathrai Rural Municipality"
            ],
            "Udayapur": [
                "Triyuga Municipality", "Katari Municipality", "Chaudandigadhi Municipality",
                "Belaka Municipality", "Udayapurgadhi Rural Municipality",
                "Tapli Rural Municipality", "Rautamai Rural Municipality",
                "Limchungbung Rural Municipality"
            ],
                
            # Madhesh Province (Province 2)
            "Bara": [
                "Kalaiya Sub-Metropolitan City", "Jeetpur Simara Sub-Metropolitan City",
                "Kolhabi Municipality", "Nijgadh Municipality", "Mahagadhimai Municipality",
                "Simraungadh Municipality", "Pacharauta Municipality", "Adarsh Kotwal Rural Municipality",
                "Baragadhi Rural Municipality", "Devtal Rural Municipality", "Feta Rural Municipality",
                "Karaiyamai Rural Municipality", "Parwanipur Rural Municipality", "Prasauni Rural Municipality",
                "Suwarna Rural Municipality"
            ],
            "Dhanusha": [
                "Janakpurdham Sub-Metropolitan City", "Chhireshwarnath Municipality",
                "Dhanusadham Municipality", "Ganeshman Charnath Municipality",
                "Kamala Municipality", "Mithila Municipality", "Mithila Bihari Municipality",
                "Nagarain Municipality", "Sahidnagar Municipality", "Bateshwar Rural Municipality",
                "Bideha Rural Municipality", "Janaknandini Rural Municipality",
                "Laxminiya Rural Municipality", "Mukhiyapatti Musarmiya Rural Municipality",
                "Sabaila Municipality", "Hansapur Municipality", "Aurahi Rural Municipality"
            ],
            "Mahottari": [
                "Jaleshwar Municipality", "Bardibas Municipality", "Gaushala Municipality",
                "Loharpatti Municipality", "Matihani Municipality", "Balwa Municipality",
                "Ramgopalpur Municipality", "Manara Shiswa Municipality", "Sonama Rural Municipality",
                "Ekdara Rural Municipality", "Samsi Rural Municipality", "Mahottari Rural Municipality",
                "Pipra Rural Municipality"
            ],
            "Parsa": [
                "Birgunj Metropolitan City", "Bahudarmai Municipality", "Parsagadhi Municipality",
                "Pokhariya Municipality", "Bindabasini Rural Municipality", "Chhipaharmai Rural Municipality",
                "Dhobini Rural Municipality", "Jagarnathpur Rural Municipality",
                "Kalikamai Rural Municipality", "Paterwa Sugauli Rural Municipality",
                "Sakhuwa Prasauni Rural Municipality", "Thori Rural Municipality"
            ],
            "Rautahat": [
                "Gaur Municipality", "Chandrapur Municipality", "Garuda Municipality",
                "Gadhimai Municipality", "Baudhimai Municipality", "Brindaban Municipality",
                "Gujara Municipality", "Katahariya Municipality", "Dewahi Gonahi Municipality",
                "Phatuwa Bijayapur Municipality", "Paroha Municipality", "Rajpur Municipality",
                "Ishnath Municipality", "Durga Bhagwati Rural Municipality",
                "Madhav Narayan Rural Municipality", "Maulapur Municipality", "Yamunamai Rural Municipality"
            ],
            "Saptari": [
                "Rajbiraj Municipality", "Bodebarsain Municipality", "Dakneshwori Municipality",
                "Hanumannagar Kankalini Municipality", "Kanchanrup Municipality",
                "Khadak Municipality", "Saptakoshi Municipality", "Shambhunath Municipality",
                "Agnisair Krishna Savaran Rural Municipality", "Bishnupur Rural Municipality",
                "Chhinnamasta Rural Municipality", "Mahadeva Rural Municipality",
                "Rupani Rural Municipality", "Surunga Municipality", "Tilathi Koiladi Rural Municipality",
                "Tirhut Rural Municipality"
            ],
            "Sarlahi": [
                "Malangwa Municipality", "Haripur Municipality", "Harion Municipality",
                "Bagmati Municipality", "Balara Municipality", "Barahathawa Municipality",
                "Chandranagar Rural Municipality", "Godaita Municipality", "Ishworpur Municipality",
                "Kabilasi Municipality", "Kaudena Rural Municipality", "Lalbandi Municipality",
                "Parsa Rural Municipality", "Ramnagar Rural Municipality", "Bishnu Rural Municipality",
                "Basbariya Rural Municipality"
            ],
            "Siraha": [
                "Siraha Municipality", "Lahan Municipality", "Golbazar Municipality",
                "Dhangadhimai Municipality", "Mirchaiya Municipality", "Kalyanpur Municipality",
                "Bhagawanpur Rural Municipality", "Aurahi Rural Municipality",
                "Bariyarpatti Rural Municipality", "Bishnupur Rural Municipality",
                "Laxmipur Patari Rural Municipality", "Naraha Rural Municipality",
                "Sakhuwanankarkatti Rural Municipality", "Sukhipur Municipality",
                "Arnama Rural Municipality"
            ],
            
            # Bagmati Province (Province 3)
            "Bhaktapur": [
                "Bhaktapur Municipality", "Changunarayan Municipality",
                "Madhyapur Thimi Municipality", "Suryabinayak Municipality"
            ],
            "Chitwan": [
                "Bharatpur Metropolitan City", "Ratnanagar Municipality",
                "Khairahani Municipality", "Madi Municipality",
                "Rapti Municipality", "Kalika Municipality", "Ichchhakamana Rural Municipality"
            ],
            "Dhading": [
                "Nilkantha Municipality", "Dhunibesi Municipality",
                "Gajuri Rural Municipality", "Galchhi Rural Municipality",
                "Jwalamukhi Rural Municipality", "Khaniyabas Rural Municipality",
                "Netrawati Dabjong Rural Municipality", "Rubi Valley Rural Municipality",
                "Siddhalek Rural Municipality", "Thakre Rural Municipality",
                "Tripurasundari Rural Municipality"
            ],
            "Dolakha": [
                "Bhimeshwar Municipality", "Jiri Municipality",
                "Baiteshwor Rural Municipality", "Bigu Rural Municipality",
                "Gaurishankar Rural Municipality", "Kalinchowk Rural Municipality",
                "Melung Rural Municipality", "Shailung Rural Municipality",
                "Tamakoshi Rural Municipality"
            ],
            "Kathmandu": [
                "Kathmandu Metropolitan City", "Kageshwari-Manohara Municipality",
                "Kirtipur Municipality", "Chandragiri Municipality",
                "Gokarneshwar Municipality", "Nagarjun Municipality",
                "Shankharapur Municipality", "Tarakeshwar Municipality",
                "Tokha Municipality", "Budhanilkantha Municipality"
            ],
            "Kavrepalanchok": [
                "Banepa Municipality", "Dhulikhel Municipality",
                "Panauti Municipality", "Panchkhal Municipality",
                "Mandandeupur Municipality", "Namobuddha Municipality",
                "Bhumlu Rural Municipality", "Chaurideurali Rural Municipality",
                "Khanikhola Rural Municipality", "Mahabharat Rural Municipality",
                "Roshi Rural Municipality", "Temal Rural Municipality"
            ],
            "Lalitpur": [
                "Lalitpur Metropolitan City", "Godawari Municipality",
                "Mahalaxmi Municipality", "Konjyosom Rural Municipality",
                "Bagmati Rural Municipality"
            ],
            "Makwanpur": [
                "Hetauda Sub-Metropolitan City", "Thaha Municipality",
                "Bakaiya Rural Municipality", "Bhimphedi Rural Municipality",
                "Indrasarowar Rural Municipality", "Kailash Rural Municipality",
                "Makawanpurgadhi Rural Municipality", "Manahari Rural Municipality",
                "Raksirang Rural Municipality"
            ],
            "Nuwakot": [
                "Bidur Municipality", "Belkotgadhi Municipality",
                "Kakani Rural Municipality", "Kispang Rural Municipality",
                "Likhu Rural Municipality", "Meghang Rural Municipality",
                "Panchakanya Rural Municipality", "Shivapuri Rural Municipality",
                "Suryagadhi Rural Municipality", "Tadi Rural Municipality",
                "Tarkeshwar Rural Municipality"
            ],
            "Ramechhap": [
                "Manthali Municipality", "Ramechhap Municipality",
                "Doramba Rural Municipality", "Gokulganga Rural Municipality",
                "Khadadevi Rural Municipality", "Likhu Tamakoshi Rural Municipality",
                "Umakunda Rural Municipality", "Sunapati Rural Municipality"
            ],
            "Rasuwa": [
                "Kalika Rural Municipality", "Gosaikunda Rural Municipality",
                "Naukunda Rural Municipality", "Aamachhodingmo Rural Municipality"
            ],
            "Sindhuli": [
                "Kamalamai Municipality", "Dudhauli Municipality",
                "Golanjor Rural Municipality", "Hariharpurgadhi Rural Municipality",
                "Marin Rural Municipality", "Phikkal Rural Municipality",
                "Sunkoshi Rural Municipality", "Tinpatan Rural Municipality"
            ],
            "Sindhupalchok": [
                "Chautara Sangachowkgadi Municipality", "Bahrabise Municipality",
                "Melamchi Municipality", "Balefi Rural Municipality",
                "Bhotekoshi Rural Municipality", "Helambu Rural Municipality",
                "Indrawati Rural Municipality", "Jugal Rural Municipality",
                "Lisankhupakhar Rural Municipality", "Panchpokhari Thangpal Rural Municipality",
                "Sunkoshi Rural Municipality", "Tripurasundari Rural Municipality"
            ],
            # Gandaki Province (Province 4)
            "Baglung": [
                "Baglung Municipality", "Jaimini Municipality",
                "Bareng Rural Municipality", "Dhorpatan Rural Municipality",
                "Galkot Rural Municipality", "Kanthekhola Rural Municipality",
                "Nisikhola Rural Municipality", "Tamankhola Rural Municipality"
            ],
            "Gorkha": [
                "Gorkha Municipality", "Palungtar Municipality",
                "Ajirkot Rural Municipality", "Aarughat Rural Municipality",
                "Barpak Sulikot Rural Municipality", "Bhimsen Thapa Rural Municipality",
                "Chumanuwri Rural Municipality", "Dharche Rural Municipality",
                "Gandaki Rural Municipality", "Shahid Lakhan Rural Municipality",
                "Siranchowk Rural Municipality", "Tsum Nubri Rural Municipality"
            ],
            "Kaski": [
                "Pokhara Metropolitan City",
                "Annapurna Rural Municipality", "Machhapuchhre Rural Municipality",
                "Madi Rural Municipality", "Rupa Rural Municipality"
            ],
            "Lamjung": [
                "Besishahar Municipality", "Madhya Nepal Municipality",
                "Rainas Municipality", "Sundarbazar Municipality",
                "Dordi Rural Municipality", "Kwhlosothar Rural Municipality",
                "Marsyangdi Rural Municipality"
            ],
            "Manang": [
                "Narpa Bhumi Rural Municipality", "Nashong Rural Municipality",
                "Chame Rural Municipality", "Narpabhumi Rural Municipality",
                "Manang Disyang Rural Municipality"
            ],
            "Mustang": [
                "Gharpajhong Rural Municipality", "Thasang Rural Municipality",
                "Lo-Ghekar Damodarkunda Rural Municipality",
                "Barhagaun Muktichhetra Rural Municipality", "Lomanthang Rural Municipality"
            ],
            "Myagdi": [
                "Beni Municipality", "Annapurna Rural Municipality",
                "Dhawalagiri Rural Municipality", "Mangala Rural Municipality",
                "Malika Rural Municipality", "Raghuganga Rural Municipality"
            ],
            "Nawalpur (East Nawalparasi)": [
                "Kawasoti Municipality", "Devchuli Municipality",
                "Gaindakot Municipality", "Madhyabindu Municipality",
                "Binayi Tribeni Rural Municipality", "Bulingtar Rural Municipality",
                "Hupsekot Rural Municipality"
            ],
            "Parbat": [
                "Kushma Municipality", "Jaljala Rural Municipality",
                "Mahashila Rural Municipality", "Modi Rural Municipality",
                "Paiyun Rural Municipality", "Phalewas Municipality"
            ],
            "Syangja": [
                "Putalibazar Municipality", "Bhirkot Municipality",
                "Chapakot Municipality", "Galyang Municipality",
                "Waling Municipality", "Arjunchaupari Rural Municipality",
                "Aandhikhola Rural Municipality", "Biruwa Rural Municipality",
                "Harinas Rural Municipality", "Kaligandaki Rural Municipality"
            ],
            "Tanahun": [
                "Damauli (Byas) Municipality", "Bhimad Municipality",
                "Bhanu Municipality", "Shuklagandaki Municipality",
                "Anbukhaireni Rural Municipality", "Bandipur Rural Municipality",
                "Devghat Rural Municipality", "Myagde Rural Municipality",
                "Rishing Rural Municipality"
            ],
        
            # Lumbini Province (Province 5)
            "Arghakhanchi": [
                "Sandhikharka Municipality", "Sitganga Municipality", 
                "Bhumikasthan Municipality", "Panini Rural Municipality", 
                "Chhatradev Rural Municipality", "Malarani Rural Municipality"
            ],
            "Banke": [
                "Nepalgunj Sub-Metropolitan City", "Kohalpur Municipality",
                "Baijanath Rural Municipality", "Duduwa Rural Municipality",
                "Janaki Rural Municipality", "Khajura Rural Municipality",
                "Narainapur Rural Municipality", "Rapti Sonari Rural Municipality"
            ],
            "Bardiya": [
                "Gulariya Municipality", "Madhuwan Municipality",
                "Rajapur Municipality", "Thakurbaba Municipality",
                "Bansgadhi Municipality", "Barbardiya Municipality",
                "Badaiyaatal Rural Municipality", "Geruwa Rural Municipality"
            ],
            "Dang": [
                "Tulsipur Sub-Metropolitan City", "Ghorahi Sub-Metropolitan City",
                "Lamahi Municipality", "Banglachuli Rural Municipality",
                "Dangisharan Rural Municipality", "Rajpur Rural Municipality",
                "Rapti Rural Municipality", "Shantinagar Rural Municipality",
                "Babai Rural Municipality"
            ],
            "Eastern Rukum": [
                "Bhume Rural Municipality", "Putha Uttarganga Rural Municipality",
                "Sisne Rural Municipality"
            ],
            "Gulmi": [
                "Resunga Municipality", "Musikot Municipality",
                "Isma Rural Municipality", "Chandrakot Rural Municipality",
                "Dhurkot Rural Municipality", "Gulmi Darbar Rural Municipality",
                "Madane Rural Municipality", "Malika Rural Municipality",
                "Ruru Rural Municipality", "Satyawati Rural Municipality"
            ],
            "Kapilvastu": [
                "Kapilvastu Municipality", "Maharajgunj Municipality",
                "Krishnanagar Municipality", "Buddhabhumi Municipality",
                "Shivaraj Municipality", "Banganga Municipality",
                "Yashodhara Rural Municipality", "Suddhodhan Rural Municipality"
            ],
            "Nawalparasi (Bardaghat Susta West)": [
                "Bardaghat Municipality", "Ramgram Municipality",
                "Sunwal Municipality", "Palhinandan Rural Municipality",
                "Pratappur Rural Municipality", "Sarawal Rural Municipality"
            ],
            "Palpa": [
                "Tansen Municipality", "Rampur Municipality",
                "Nisdi Rural Municipality", "Rambha Rural Municipality",
                "Mathagadhi Rural Municipality", "Rainadevi Chhahara Rural Municipality",
                "Baganaskali Rural Municipality", "Purbakhola Rural Municipality",
                "Tinau Rural Municipality"
            ],
            "Pyuthan": [
                "Pyuthan Municipality", "Swargadwari Municipality",
                "Gaumukhi Rural Municipality", "Jhimruk Rural Municipality",
                "Mallarani Rural Municipality", "Naubahini Rural Municipality",
                "Sarumarani Rural Municipality", "Mandavi Rural Municipality"
            ],
            "Rolpa": [
                "Rolpa Municipality", "Triveni Rural Municipality",
                "Runtigadhi Rural Municipality", "Sunil Smriti Rural Municipality",
                "Sunchhahari Rural Municipality", "Paribartan Rural Municipality",
                "Lungri Rural Municipality", "Madi Rural Municipality",
                "Thabang Rural Municipality"
            ],
            "Rupandehi": [
                "Butwal Sub-Metropolitan City", "Siddharthanagar Municipality",
                "Devdaha Municipality", "Tilottama Municipality",
                "Lumbini Sanskritik Municipality", "Sainamaina Municipality",
                "Marchawari Rural Municipality", "Omsatiya Rural Municipality",
                "Kotahimai Rural Municipality", "Gaidahawa Rural Municipality",
                "Suddhodhan Rural Municipality", "Mayadevi Rural Municipality"
            ],
            
        # Karnali Province (Province 6)
            "Dailekh": [
                "Narayan Municipality", "Dullu Municipality", "Chamunda Bindrasaini Municipality",
                "Aathabis Municipality", "Bhagawatimai Rural Municipality",
                "Dungeshwor Rural Municipality", "Gurans Rural Municipality",
                "Mahabu Rural Municipality", "Naumule Rural Municipality"
            ],
            "Dolpa": [
                "Thuli Bheri Municipality", "Tripurasundari Municipality",
                "Dolpo Buddha Rural Municipality", "Jagadulla Rural Municipality",
                "Kaike Rural Municipality", "She Phoksundo Rural Municipality",
                "Mudkechula Rural Municipality"
            ],
            "Humla": [
                "Simkot Rural Municipality", "Namkha Rural Municipality",
                "Chankheli Rural Municipality", "Kharpunath Rural Municipality",
                "Sarkegad Rural Municipality", "Tanjakot Rural Municipality",
                "Adanchuli Rural Municipality"
            ],
            "Jajarkot": [
                "Bheri Municipality", "Chhedagad Municipality",
                "Barekot Rural Municipality", "Kuse Rural Municipality",
                "Junichande Rural Municipality", "Shivalaya Rural Municipality"
            ],
            "Jumla": [
                "Chandannath Municipality", "Guthichaur Rural Municipality",
                "Hima Rural Municipality", "Kankasundari Rural Municipality",
                "Patarasi Rural Municipality", "Sinja Rural Municipality",
                "Tatopani Rural Municipality", "Tila Rural Municipality"
            ],
            "Kalikot": [
                "Raskot Municipality", "Tilagufa Municipality",
                "Narharinath Rural Municipality", "Pachaljharana Rural Municipality",
                "Sanni Triveni Rural Municipality", "Shubha Kalika Rural Municipality",
                "Palata Rural Municipality", "Mahawai Rural Municipality"
            ],
            "Mugu": [
                "Chhayanath Rara Municipality", "Khatyad Rural Municipality",
                "Mugum Karmarong Rural Municipality", "Soru Rural Municipality"
            ],
            "Salyan": [
                "Bangad Kupinde Municipality", "Sharada Municipality",
                "Bagchaur Municipality", "Darma Rural Municipality",
                "Kalimati Rural Municipality", "Kapurkot Rural Municipality",
                "Chatreshwori Rural Municipality", "Siddha Kumakh Rural Municipality",
                "Triveni Rural Municipality"
            ],
            "Surkhet": [
                "Birendranagar Municipality", "Bheriganga Municipality",
                "Gurbhakot Municipality", "Lekbesi Municipality",
                "Panchapuri Municipality", "Barahatal Rural Municipality",
                "Chaukune Rural Municipality", "Simta Rural Municipality"
            ],
            
            # Sudurpashchim Province (Province 7)
            "Kanchanpur": [
                "Bhimdatta Municipality", "Bedkot Municipality", "Krishnapur Municipality",
                "Shuklaphanta Municipality", "Belauri Municipality", "Punarbas Municipality",
                "Mahakali Municipality", "Laljhadi Rural Municipality"
            ],
            "Kailali": [
                "Dhangadhi Sub-Metropolitan City", "Tikapur Municipality", "Lamkichuha Municipality",
                "Ghodaghodi Municipality", "Bhajani Municipality", "Gauriganga Municipality",
                "Gokuleshwar Municipality", "Joshipur Rural Municipality", "Janaki Rural Municipality",
                "Bardagoriya Rural Municipality", "Mohanyal Rural Municipality", "Chure Rural Municipality"
            ],
            "Doti": [
                "Dipayal Silgadhi Municipality", "Shikhar Municipality",
                "Purbichauki Rural Municipality", "Aadarsha Rural Municipality",
                "K I Singh Rural Municipality", "Jorayal Rural Municipality",
                "Sayal Rural Municipality", "Badikedar Rural Municipality"
            ],
            "Achham": [
                "Mangalsen Municipality", "Sanphebagar Municipality",
                "Kamalbazar Municipality", "Panchdeval Binayak Municipality",
                "Chaurpati Rural Municipality", "Dhakari Rural Municipality",
                "Bannigadhi Jayagad Rural Municipality", "Mellekh Rural Municipality",
                "Ramaroshan Rural Municipality", "Turmakhand Rural Municipality"
            ],
            "Bajhang": [
                "Jaya Prithvi Municipality", "Bungal Municipality", "Talkot Rural Municipality",
                "Kedarsyu Rural Municipality", "Surma Rural Municipality", "Chhabis Pathivera Rural Municipality",
                "Durgathali Rural Municipality", "Khaptad Chhanna Rural Municipality", "Masta Rural Municipality",
                "Thalara Rural Municipality", "Bitthadchir Rural Municipality"
            ],
            "Bajura": [
                "Budhinanda Municipality", "Triveni Municipality", "Badimalika Municipality",
                "Himali Rural Municipality", "Gaumul Rural Municipality", "Swami Kartik Rural Municipality",
                "Chhededaha Rural Municipality", "Jagannath Rural Municipality"
            ],
            "Dadeldhura": [
                "Amargadhi Municipality", "Aalital Rural Municipality",
                "Bhageshwar Rural Municipality", "Navadurga Rural Municipality",
                "Ganyapadhura Rural Municipality", "Ajayameru Rural Municipality",
                "Parashuram Municipality"
            ],
            "Baitadi": [
                "Dasharathchand Municipality", "Patan Municipality",
                "Melauli Municipality", "Purchaudi Municipality",
                "Dilasaini Rural Municipality", "Dogadakedar Rural Municipality",
                "Pancheshwar Rural Municipality", "Sigas Rural Municipality",
                "Shivanath Rural Municipality"
            ],
            "Darchula": [
                "Mahakali Municipality", "Shailyashikhar Municipality",
                "Byas Rural Municipality", "Apihimal Rural Municipality",
                "Naugad Rural Municipality", "Duhun Rural Municipality",
                "Malikaarjun Rural Municipality", "Marma Rural Municipality"
            ]
    }
        
        # Return the relevant municipalities based on district selection
        return district_municipality_data.get(district, [])


class UserProfile(models.Model):
    USER_TYPE_CHOICES = [
        ('Faat', 'Faat'),
        ('Branch  Head' , 'Branch  Head'),
        ('Branch Officer', 'Branch Officer'),
        ('Division Head', 'Division Head'),
        ('Admin', 'Admin'),
        ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=100, choices=USER_TYPE_CHOICES)

class Designation(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Tippani(models.Model):
    office = models.ForeignKey(Office, on_delete=models.CASCADE, related_name='tippanis')
    present_file = models.FileField(null=True, blank=True)
    present_subject = models.CharField(max_length=255)
    present_by = models.CharField(max_length=200)
    present_date = models.DateField()
    page_no = models.IntegerField()
    total_page = models.IntegerField()
    approved_by = models.CharField(max_length=200, null=True, blank=True)
    approve_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Tippani: {self.present_subject}"


class LettersAndDocuments(models.Model):
    tippani = models.ForeignKey(Tippani, on_delete=models.CASCADE, related_name='letterandocuments')
    registration_no = models.CharField(max_length=100)
    invoice_no = models.CharField(max_length=100)
    date = models.DateField()
    subject = models.TextField()
    letter_date = models.DateField()
    office = models.CharField(max_length=300)
    page_no = models.IntegerField()

    def __str__(self):
        return f"Document: {self.subject} (Reg No: {self.registration_no})"


class File(models.Model):
    
    letter_document = models.ForeignKey(LettersAndDocuments, on_delete=models.CASCADE, related_name='files', null=True)
    file = models.FileField(upload_to='supporting_files/', null=True)    
    file_number = models.CharField(max_length=50, unique=True, blank=True, editable=False)

    def __str__(self):
        return self.file_number

    def save(self, *args, **kwargs):
        if not self.file_number:
            # Generate a unique file number with "G.U." as a prefix
            while True:
                random_number = random.randint(10000, 99999)  # Generate a 5-digit random number
                file_number = f"G.U.{random_number}"
                if not File.objects.filter(file_number=file_number).exists():
                    self.file_number = file_number
                    break
        super().save(*args, **kwargs)


class Approval(models.Model):
    STATUS_CHOICES = [
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('transferred', 'Transferred'),
        ('pending', 'Pending'),
    ]

    tippani = models.ForeignKey(Tippani, on_delete=models.CASCADE, related_name='approvals')
    submitted_by = models.ForeignKey(Designation, on_delete=models.CASCADE, related_name='submitted_tippanis')
    approved_by = models.ForeignKey(Designation, on_delete=models.CASCADE, related_name='approved_tippanis', null=True,
                                    blank=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='pending')
    remarks = models.TextField(null=True, blank=True)
    approved_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.tippani
