import pytest
from Config.config import TestData
from Pages.ContactMenuPage import ContactMenuPage
from Tests.test_base import BaseTest

class Test_Contact_Menu(BaseTest):
    
    # @pytest.mark.skip(reason="Test not implemented yet")
    # def test_contact_menu_visible(self):
    #     self.contactMenu = ContactMenuPage(self)
    #     flag = self.contactMenu.is_contact_menu_link_exist()
    #     assert flag
     
    # @pytest.mark.skip(reason="Test not implemented yet")   
    # def test_open_contact_menu(self):
    #     self.contactMenu =ContactMenuPage(self)
    #     self.contactMenu.do_open_contact_menu()
        
    def test_send_message(self):
        self.contactMenu = ContactMenuPage(self.driver)
        self.contactMenu.do_open_contact_menu()
        self.contactMenu.do_send_message(TestData.CM_EMAIL_VALID, TestData.CM_NAME, TestData.CM_MESSAGE)
        