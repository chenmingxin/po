import page
from base.base import Base


class PageLogin(Base):
    def page_input_username(self,username):
        self.base_input(page.loc_name,username)

    def page_input_pwd(self,pwd):
        self.base_input(page.loc_pwd,pwd)

    def page_click_btn(self):
        self.base_click(page.loc_click)