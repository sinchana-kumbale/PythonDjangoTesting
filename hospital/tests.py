from django.test import LiveServerTestCase
from .models import PatientInfor
from .forms import PatientForm
from django.urls import reverse
from django.test import Client
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TransactionModelTests(LiveServerTestCase):
    def setUp(self):
        self.selenium = webdriver.Chrome()

    def test_form_elements(self):
        self.selenium.get(self.live_server_url+'/patient')

        assert 'id_patient_name' in self.selenium.page_source
        assert 'id_patient_age' in self.selenium.page_source
        assert 'id_Issue' in self.selenium.page_source
        assert 'id_doctor_name' in self.selenium.page_source

    def test_link_to_report(self):
        self.selenium.get(self.live_server_url+'/patient')
        a = self.selenium.find_element_by_id('link')
        a.click()
        assert 'Patient Form' == self.selenium.title

    def test_entry_1_item(self):
        self.selenium.get(self.live_server_url+'/patient')

        #Retrieve the form elements based on Django's naming convension
        patient_name = self.selenium.find_element_by_id('id_patient_name')
        patient_age = self.selenium.find_element_by_id('id_patient_age')
        Issue = self.selenium.find_element_by_id('id_Issue')
        doctor = self.selenium.find_element_by_id('id_doctor_name')
        submit = self.selenium.find_element_by_id('submit')

        #populate the form with data
        patient_name.send_keys('ABC')
        patient_age.send_keys('1')
        Issue.send_keys('Diabetes')
        doctor.send_keys('XYZ')

        #submit form
        submit.send_keys(Keys.RETURN)
    def test_doc_returns(self):
        self.selenium.get(self.live_server_url+'/doctor')
        doc = self.selenium.find_element_by_id('name')
        submit = self.selenium.find_element_by_id('submit')
        doc.send_keys('XYZ')
        submit.send_keys(Keys.RETURN)
        self.selenium.get('hospital/patientinfor.html')
        assert "ABC" in selenium.page_source


    def tearDown(self):
        self.selenium.close()
