
from faker import Faker
fake = Faker()
day = fake.day_of_month()
month = fake.month_name()


class ProjectData:
    target_url = 'https://pentest-ground.com:81'
    target_endpoint = ''
    target_ip = "192.168.1.1/24"
    response_limit = float(1.0)


class FormData:
    newUser = 'turquoise777777QA!$'  # fake.color_name()+'777777'+'QA!$'
    fname = fake.first_name_male()
    lname = fake.last_name()
    email = fake.email()
    tel = '2123334455'
    birthday = day+" "+month+" "+'1975'
    subj = "English"
    address = fake.address()
    randomString = fake.pystr()
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyTmFtZSI6ImRlbW9RQSIsInBhc3N3b3JkIjoiYmxVZU3Dtm9uOTckIiwiaWF0IjoxNzEzNDYzNTM4fQ.yXI26P4Zl-TvH2_MqbPRS-U5muGwedeKSjvVD1Lv-VQ"# secon
    
    
class StringPayloads:
    simpleAscii = "!@#$%^&'"
    blankString = ""
    simpleString = 'this is a security test'
    mixedCharSet = 'Lorem ipsum dolor sit amet, Римский император Константин I Великий, 北京位於華北平原的西北边缘'
    sanskrit = 'وضع ابن الهيثم تصور واضح للعلاقة بين النموذج الرياضي المثالي ومنظومة الظواهر الملحوظة.'
        
    
class SQLIPayloads:
    sqlInjection = "OR 1=1;##"
    sqlInjection2 = " '+OR+1=1-- "
    sqlInjection3 = '%27+OR+1=1--%27'
    sqlInjection_lowercase = " '+or+1=1-- "
    sqlInjection_encoded = "%22%27%20OR%20%271%27%3D%271%22"
    sqlInjection_nullBytes = "%00' UNION SELECT password FROM Users WHERE username='admin'--' "
    sqlInjection_inline = "/**/UNION/**/SELECT/**/password/**/FROM/**/Users/**/WHERE/**/name/**/LIKE/**/'admin'-- "
    
    
class XSSPayloads:
    simpleHTML = '<h1>test</h1>'
    htmlEntities = '&lt;test&lt;'
    jsInjection = "Nice site,  I think I'll take it. <script>alert('Executing JS')</script>"
    jsInjectionAllCaps = "Another one <SCRIPT>ALERT('DOCUMENT.COOKIE')</SCRIPT>"
    scriptTagVariation = '<ScRiPt>alert("XSS")</ScRiPt>'
    brokenHTML = '<i><b>Bold</i></b>'
    anchorTag = '<ahref="<script>alert("Executing JS")</script>">Home</a>'
    xssImageTag = "<img src=x onerror=alert(‘boo’)>"
    escapeSequence = " `<img src=x onerror=alert(‘boo’)>` "
    encoding = '?search=%22%3E%3Csvg%3E%3Canimatetransform%20onbegin=alert(1)%3E'
    recursiveFilter = "-prompt()-"
    

class URLPayloads:
    parameterList = [
        StringPayloads.blankString,
        StringPayloads.simpleAscii,
        StringPayloads.simpleString,
        XSSPayloads.scriptTagVariation,
        XSSPayloads.jsInjection,
        SQLIPayloads.sqlInjection,
        "&url=https://mysite.com"]

    
class InvalidEmailAddresses:
    badEmails = ['badEmail', 'email.domain.com', '@domain.com',
                 '#@%^%#$@#$@#.com', 'email@domain.com (Joe Smith)', 'email@domain@domain.com', '.email@domain.com',
                 'email.@domain.com', 'email..email@domain.com', 'あいうえお@domain.com', 'email@-domain.com', 'email@.domain.com',
                 'email@111.222.333.44444', 'email@domain..com']