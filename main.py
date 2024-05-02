import mysql.connector
from datetime import datetime
import exception1
class jobListing:
    def __init__(self,job_id,company_id,job_title,job_description,job_location,salary,job_type,posted_date):
        self.job_id=job_id
        self.company_id=company_id
        self.job_title=job_title
        self.job_description=job_description
        self.job_location=job_location
        self.salary=salary
        self.job_type=job_type
        self.posted_date=posted_date
        self.applicants=[]

    def apply(self, applicant_id, cover_letter):
        application = {
            'applicant_id': applicant_id,
            'cover_letter': cover_letter,
            'application_date': datetime.now()
        }
        self.applicants.append(application)
        print(f"Application submitted for job '{self.job_title}' by applicant ID {applicant_id}.")

    def getApplicants(self):
        applicant_ids = [app['applicant_id'] for app in self.applicants]
        return applicant_ids
class company(jobListing):
    def __init__(self,company_id,company_name,location):
        self.company_id=company_id
        self.company_name=company_name
        self.location=location
        self.jobs=[]
    def postJob(self,job_title,job_description,salary,job_type):
        self.job_title=job_title
        self.job_description=job_description
        self.salary=salary
        self.job_type=job_type
        list1=[self.job_title,self.job_description,self,salary,self.job_type]
        jobs.append(list1)
    def getJobs(self):
        print(self.jobs)

class Applicant(jobListing):
    def __init__(self,applicant_id,first_name,last_name,email,phone,resume):
           self.applicant_id = applicant_id
           self.first_name = first_name
           self.last_name = last_name
           self.email = email
           self.phone = phone
           self.resume = resume
           self.cover_letter = " "
    def CreateProfile(self,email,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
    def ApplyForJob(self,job_id,cover_letter):
            self.job_id=job_id
            self.cover_letter=cover_letter

class jobApplication(Applicant,jobListing):
    def __init__(self,application_id,job_id,applicant_id,application_date,cover_letter):
        self.application_id=application_id
        self.job_id = job_id
        self.applicant_id=applicant_id
        self.application_date=application_date
        self.cover_letter=cover_letter

class DatabaseManager:
    def email_check(self,email):
        if "@" not in email or "." not in email:
            raise exception1.InvalidEmailError()
    def upload_file(file):
        try:
            with open(file, 'rb') as f:
                # Upload the file
                print(f"File {file} uploaded successfully.")
        except FileNotFoundError:
            raise exception1.FileUploadError("File not found.")
        except Exception as e:
            raise exception1.FileUploadError(f"File upload failed: {e}")

    def check_deadline(application_date, deadline):
        if application_date > deadline:
            raise exception1.DeadlineExceededError()

    def calculate_average_salary(salaries):
        total_salary = sum(salaries)
        count = len(salaries)
        if count == 0:
            return 0
        for salary in salaries:
            if salary < 0:
                raise exception1.NegativeSalaryError()
        return total_salary / count

    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
    def initializeDatabase(self):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                database='exam',
                user='root',
                password='Vishnu@542'
            )
            if connection.is_connected():
                print('Connected to MySQL database')
        except mysql.connector.Error as e:
            print(f"Error Connecting the database")
    def  insertJobListings(self,jobListing):
        connection = mysql.connector.connect(
            host='localhost',
            database='exam',
            user='root',
            password='Vishnu@542'
        )
        query="insert into jobs values(%s,%s,%s,%s,%s,%s,%s,%s)"
        data=(jobListing.job_id,jobListing.company_id,jobListing.job_title,jobListing.job_description,jobListing.job_location,jobListing.salary,jobListing.job_type,jobListing.posted_date)
        cursor=connection.cursor()
        cursor.execute(query,data)
        '''try:
            q1="select salary from jobs"
            cursor.execute(q1)
            salaries=cursor.fetchall()
            avg_salaries=dm.calculate_average_salary()
            print(f"average salaries {avg_salaries}")
        except exception1.NegativeSalaryError as e:
            print(e)'''
        print("values inserted")
        connection.commit()
        cursor.close()
    def insertcompany(self,company):
        connection = mysql.connector.connect(
            host='localhost',
            database='exam',
            user='root',
            password='Vishnu@542'
        )
        query="insert into companies values(%s,%s,%s)"
        cursor=connection.cursor()
        data=(company.company_id,company.company_name,company.location)
        cursor.execute(query,data)
        connection.commit()
        cursor.close()
        print("values entered into companies tables")
    def insertApplicant(self,Applicant):
        connection = mysql.connector.connect(
            host='localhost',
            database='exam',
            user='root',
            password='Vishnu@542'
        )
        data=(Applicant.applicant_id,Applicant.first_name,Applicant.last_name,Applicant.email,Applicant.phone,Applicant.resume)
        try:
            query="insert into applicants values(%s,%s,%s,%s,%s,%s)"
            dm.email_check(Applicant.email)
        except exception1.InvalidEmailError as e:
            print(e)
        cursor=connection.cursor()
        cursor.execute(query,data)
        connection.commit()
        cursor.close()
        print("values entered into applicants")
    def insertJobApplications(self,jobApplication):
        connection = mysql.connector.connect(
            host='localhost',
            database='exam',
            user='root',
            password='Vishnu@542'
        )
        query="insert into applications values(%s,%s,%s,%s,%s)"
        data=(jobApplication.application_id,jobApplication.job_id,jobApplication.applicant_id,jobApplication.application_date,jobApplication.cover_letter)
        cursor=connection.cursor()
        cursor.execute(query,data)
        connection.commit()
        cursor.close()
        print("values entered into applications")
    def getJobListings(self):
        connection = mysql.connector.connect(
            host='localhost',
            database='exam',
            user='root',
            password='Vishnu@542'
        )
        cursor=connection.cursor()
        query="select * from jobs"
        cursor.execute(query)
        joblist=cursor.fetchall()
        for x in joblist:
            print(x)
    def getCompanies(self):
        connection = mysql.connector.connect(
            host='localhost',
            database='exam',
            user='root',
            password='Vishnu@542'
        )
        cursor = connection.cursor()
        query = "select * from companies"
        cursor.execute(query)
        joblist = cursor.fetchall()
        for x in joblist:
            print(x)
    def getApplicants(self):
        connection = mysql.connector.connect(
            host='localhost',
            database='exam',
            user='root',
            password='Vishnu@542'
        )
        cursor=connection.cursor()
        cursor.execute("select * from applicants")
        applicants=cursor.fetchall()
        for x in applicants:
            print(x)
    def getApplications(self):
        connection = mysql.connector.connect(
            host='localhost',
            database='exam',
            user='root',
            password='Vishnu@542'
        )
        cursor=connection.cursor()
        cursor.execute("select * from applications")
        applications=cursor.fetchall()
        for x in applications:
            print(x)

    def get_job_listings(self):
        try:
            connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )

            if connection.is_connected():
                cursor = connection.cursor()
                query = "SELECT JobTitle, CompanyName, Salary FROM jobs INNER JOIN companies ON jobs.CompanyID = companies.CompanyID"
                cursor.execute(query)
                job_listings = cursor.fetchall()
                for job in job_listings:
                    print("Job Title:", job[0])
                    print("Company Name:", job[1])
                    print("Salary:", job[2])
                    print()
                cursor.close()

            else:
                print('Connection to MySQL database failed')

        except mysql.connector.Error as e:
            print(f"Error retrieving job listings from MySQL database: {e}")

    def create_applicant_profile(self, applicant):
        try:
            connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if connection.is_connected():
                cursor = connection.cursor()
                query = "INSERT INTO applicants (FirstName, LastName, Email, Phone, Resume) VALUES (%s, %s, %s, %s, %s)"
                data = (applicant.first_name, applicant.last_name, applicant.email, applicant.phone, applicant.resume)
                cursor.execute(query, data)
                connection.commit()
                print("Applicant profile created successfully")
                cursor.close()
            else:
                print('Connection to MySQL database failed')
        except mysql.connector.Error as e:
            print(f"Error creating applicant profile in MySQL database: {e}")

            def submit_job_application(self, job_id, applicant_id, application_date, cover_letter):
                try:
                    connection = mysql.connector.connect(
                        host=self.host,
                        database=self.database,
                        user=self.user,
                        password=self.password
                    )

                    if connection.is_connected():
                        cursor = connection.cursor()
                        query = "INSERT INTO job_applications (JobID, ApplicantID, ApplicationDate, CoverLetter) VALUES (%s, %s, %s, %s)"
                        data = (job_id, applicant_id, application_date, cover_letter)
                        cursor.execute(query, data)
                        connection.commit()
                        print("Job application submitted successfully")
                        cursor.close()
                    else:
                        print('Connection to MySQL database failed')

                except mysql.connector.Error as e:
                    print(f"Error submitting job application in MySQL database: {e}")
    def post_job_listing(self, company_id, job_title, job_description, job_location, salary, job_type, posted_date):
        try:
            connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )

            if connection.is_connected():
                cursor = connection.cursor()
                query = "INSERT INTO jobs (CompanyID, JobTitle, JobDescription, JobLocation, Salary, JobType, PostedDate) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                data = (company_id, job_title, job_description, job_location, salary, job_type, posted_date)
                cursor.execute(query, data)
                connection.commit()
                print("Job listing posted successfully")
                cursor.close()

            else:
                print('Connection to MySQL database failed')

        except mysql.connector.Error as e:
            print(f"Error posting job listing in MySQL database: {e}")

    def search_job_listings_by_salary_range(self, min_salary, max_salary):
        try:
            connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )

            if connection.is_connected():
                cursor = connection.cursor()
                query = "SELECT JobTitle, CompanyName, Salary FROM jobs INNER JOIN companies ON jobs.CompanyID = companies.CompanyID WHERE Salary BETWEEN %s AND %s"
                data = (min_salary, max_salary)
                cursor.execute(query, data)
                job_listings = cursor.fetchall()
                for job in job_listings:
                    print("Job Title:", job[0])
                    print("Company Name:", job[1])
                    print("Salary:", job[2])
                    print()
                cursor.close()

            else:
                print('Connection to MySQL database failed')

        except mysql.connector.Error as e:
            print(f"Error searching job listings by salary range in MySQL database: {e}")


dm=DatabaseManager("localhost","exam","root","Vishnu@542")
dm.getApplicants()