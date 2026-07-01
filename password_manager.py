import argparse
import getpass
from crypto_utils import encrypt, decrypt
from storage import add_entry, get_entry, delete_entry, list_services

def handle_add(args):
    password = getpass.getpass("enter password: ")
    encrypted_password = encrypt(password)
    add_entry(args.service, args.username, encrypted_password)
    print(f"saved credentials for '{args.service}'.")

def handle_get(args):
    entry = get_entry(args.service)
    if entry is None:
        print(f"no entry is found for '{args.service}'.")
        return
    decrypted_password = decrypt(entry["password"])
    print(f"service: {args.service}")
    print(f"username: {entry['username']}")
    print(f"password: {decrypted_password}")

def handle_list(args):
    services = list_services()
    if not services:
        print("no saved credentials yet")
        return
    print("saved services:")
    for s in services:
        print(f" - {s}")

def handle_delete(args):
    deleted = delete_entry(args.service)
    if deleted:
        print(f"deleted entry for '{args.service}'.")
    else:
        print(f"No entry found for '{args.service}'.")

def main():
    parser = argparse.ArgumentParser(description = " encrypted CLI password manager")
    subparsers = parser.add_subparsers(dest="command", required = True)
    add_parser = subparsers.add_parser("add", help = "add a new credential")
    add_parser.add_argument("service", help = "name of the service: ")
    add_parser.add_argument("username", help = "username for the service")
    add_parser.set_defaults(func=handle_add)
    
    get_parser = subparsers.add_parser("get", help = "retrieve a credential")
    get_parser.add_argument("service", help = "name of service to retrieve")
    get_parser.set_defaults(func=handle_get)

    list_parser = subparsers.add_parser("list", help = "list all saved service names")
    list_parser.set_defaults(func=handle_list)

    delete_parser = subparsers.add_parser("delete", help = "delete a credential")
    delete_parser.add_argument("service", help = "name of service to delete")
    delete_parser.set_defaults(func=handle_delete)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()


