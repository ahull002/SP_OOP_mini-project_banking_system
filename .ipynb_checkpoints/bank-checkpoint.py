class Bank:

    name = 'Springboard Federal Credit Union'
    clients = []

    def update_db(self, client):
        self.clients.append(client)

    def authentication(self, name, address, account_number):
        for i in range(len(self.clients)):
            if name in self.clients[i].account.values() and account_number in self.clients[i].account.values():
                print()
                print("Authentication successful!")
                print("========================================================================================")
                return self.clients[i]