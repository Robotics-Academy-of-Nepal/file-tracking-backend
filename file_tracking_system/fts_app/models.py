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
        PROVINCE_1 = 'Province 1', _('Province 1')
        PROVINCE_2 = 'Province 2', _('Province 2')
        PROVINCE_3 = 'Province 3', _('Province 3')
        PROVINCE_4 = 'Province 4', _('Province 4')
        PROVINCE_5 = 'Province 5', _('Province 5')
        PROVINCE_6 = 'Province 6', _('Province 6')
        PROVINCE_7 = 'Province 7', _('Province 7')

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
    awards = models.ForeignKey(
        Awards,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='user_awards',
        verbose_name=_('Awards')
    )
    punishments = models.ForeignKey(
        Punishments,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='user_punishments',
        verbose_name=_('Punishments')
    )
    loan = models.ForeignKey(
        Loan,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='user_loans',
        verbose_name=_('Loan')
    )
    education = models.ForeignKey(
        Education,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='user_education',
        verbose_name=_('Education')
    )
    office = models.ForeignKey(
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
    def get_district_choices(self, state):
        # Province data with respective districts
        province_data = {
            "Province 1": ["Jhapa", "Morang", "Sunsari", "Bhojpur", "Ilam", "Khotang", "Okhaldhunga", "Panchthar", "Sankhuwasabha", "Solukhumbu", "Taplejung", "Terhathum", "Udayapur"],
            "Province 2": ["Saptari", "Dhanusha", "Mahottari", "Sarlahi", "Siraha", "Bara", "Parsa", "Rautahat", "Chhathapol"],
            "Province 3": ["Kathmandu", "Bhaktapur", "Lalitpur", "Kavrepalanchok", "Nuwakot", "Rasuwa", "Sindhuli", "Sindhupalchok", "Chitwan", "Makawanpur", "Bhaktapur", "Nawalparasi", "Tanahu"],
            "Province 4": ["Kaski", "Parbat", "Tanahun", "Gorkha", "Lamjung", "Manang", "Mustang", "Syangja", "Nawalparasi", "Syangja"],
            "Province 5": ["Rupandehi", "Kapilvastu", "Palpa", "Nawalparasi", "Arghakhanchi", "Rukum", "Salyan", "Dang", "Banke", "Bardiya"],
            "Province 6": ["Surkhet", "Dailekh", "Jajarkot", "Jumla", "Kalikot", "Mugu", "Humla", "Dolpa", "Rukum", "Salyan"],
            "Province 7": ["Kanchanpur", "Baitadi", "Darchula", "Achham", "Kailali", "Bajura", "Bajhang", "Dadeldhura", "Doti", "Dadeldhura"]
        }
        return province_data.get(state, [])

    def get_municipality_choices(self, state, district):
        # Expanded data for municipalities (to be filled with your data)
        district_municipality_data = {
            # Province 1
            "Jhapa": ["Birtamod", "Mechinagar", "Damak", "Kankai", "Shivasatakshi", "Sunsari", "Basantapur", "Arjundhara"],
            "Morang": ["Biratnagar", "Inaruwa", "Rangeli", "Madhyapur Thimi", "Pathari", "Katahari", "Dhanpalthana"],
            "Sunsari": ["Itahari", "Bharatpur", "Damak", "Bhanjanagar", "Sunsari", "Mahendranagar", "Kishannagar"],
            "Ilam": ["Ilam", "Pashupati", "Suryodaya", "Maihami", "Barshangia"],
            "Bhojpur": ["Bhojpur", "Aadhhar", "Aphun", "Tandi"],
            
            # Province 2
            "Saptari": ["Rajbiraj", "Kanchanpur", "Bardibas", "Saptakoshi", "Mahendra Nagar"],
            "Dhanusha": ["Janakpur", "Dhanushadham", "Chandrapur", "Aurahi"],
            "Mahottari": ["Jaleshwar", "Bhathabara", "Ramnagar", "Kanakpatti", "Hathura"],
            "Sarlahi": ["Madhavpur", "Sarlahi", "Hariharpur"],
            "Siraha": ["Lahan", "Dhangadhimai", "Karjanha", "Lohandigama"],
            "Bara": ["Parsa", "Birgunj", "Nawalpur", "Simraungadh"],
            "Parsa": ["Birgunj", "Bairgania", "Madhav Narayan", "Shivpur"],
            
            # Province 3
            "Kathmandu": ["Kathmandu", "Bhaktapur", "Lalitpur", "Chandragiri", "Kirtipur", "Boudha", "Patan"],
            "Bhaktapur": ["Bhaktapur", "Suryabinayak", "Madhyapur Thimi"],
            "Lalitpur": ["Lalitpur", "Godawari", "Mahankal", "Imadol"],
            "Kavrepalanchok": ["Dhulikhel", "Panauti", "Banepa", "Kavre"],
            "Nuwakot": ["Trisuli", "Bidur", "Taruka", "Ishwarpur"],
            "Rasuwa": ["Dhunche", "Kalika", "Ramche", "Kailash"],
            
            # Province 4
            "Kaski": ["Pokhara", "Lekhnath", "Machhapuchhre", "Syangja", "Ghorepani"],
            "Parbat": ["Jomsom", "Baglung", "Kahwang"],
            "Tanahun": ["Damauli", "Puranchaur", "Bhanu", "Besisahar"],
            "Gorkha": ["Gorkha", "Arughat", "Chhetrapati"],
            "Lamjung": ["Besisahar", "Bhanu", "Syangja"],
            
            # Province 5
            "Rupandehi": ["Butwal", "Bhanu", "Siddharthanagar", "Taulihawa"],
            "Kapilvastu": ["Taulihawa", "Parasi", "Khalwat"],
            "Palpa": ["Tansen", "Rani", "Lumbini"],
            "Nawalparasi": ["Ramgram", "Siddhartha", "Chandranigahapur"],
            "Arghakhanchi": ["Sandhikharka", "Panchanewan", "Bashidharam"],
            "Rukum": ["Rukumkot", "Rukum", "Ghorahi"],
            "Salyan": ["Salyan", "Tulasipur"],
            "Dang": ["Tulsipur", "Ghorahi", "Dangbhuli"],
            "Banke": ["Nepalgunj", "Kohalpur"],
            "Bardiya": ["Gulariya", "Rajapur", "Bardiya"],
            
            # Province 6
            "Surkhet": ["Birendranagar", "Karnali", "Manma"],
            "Dailekh": ["Dailekh", "Chaugan"],
            "Jajarkot": ["Jajarkot", "Chhidrapur"],
            "Jumla": ["Jumla", "Chandannath"],
            "Kalikot": ["Kalikot", "Khandachakra"],
            "Mugu": ["Mugu", "Gamgadhi"],
            "Humla": ["Simkot", "Humla"],
            "Dolpa": ["Dolpa", "Jajarkot"],
            "Rukum": ["Rukumkot", "Salyan"],
            
            # Province 7
            "Kanchanpur": ["Mahendranagar", "Bhimdutta", "Kanchanpur", "Gulariya"],
            "Baitadi": ["Baitadi", "Darchula"],
            "Darchula": ["Darchula", "Dugdiligad"],
            "Achham": ["Achham", "Mugu", "Khaptad"],
            "Kailali": ["Dhangadhi", "Tikapur", "Lamki", "Bajhang"],
            "Bajura": ["Bajura", "Sanphebagar"],
            "Bajhang": ["Bajhang", "Baitadi", "Chhetrapur"],
            "Dadeldhura": ["Dadeldhura", "Doti"],
            "Doti": ["Doti", "Dipayal"]
        }
        
        # Return the relevant municipalities based on district selection
        return district_municipality_data.get(district, [])


