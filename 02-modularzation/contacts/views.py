from contacts.models import contact_list

def run_views() :
    print('Contact List')
    print("-------------")
    for item in contact_list:
        print(item)