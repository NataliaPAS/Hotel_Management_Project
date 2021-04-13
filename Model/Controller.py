

def client_menu(self):
    """
    Display the client menu
    """
    while True:
        option = self.client_view.client_menu()
        if option == '1':
            self.add_client()
        elif option == '2':
            self.update_client()
        elif option == '3':
            self.delete_client()
        elif option == '4':
            self.display_one_client()
        elif option == '5':
            self.display_all_clients()
        elif option == 'x':
            return
        else:
            self.general_view.display_wrong_option()

