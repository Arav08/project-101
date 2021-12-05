import dropbox
import os

from dropbox.files import WriteMode

class TransferData:
     def __init__(self, access_token):
        self.access_token = access_token
    
     def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):
            local_path = input("nter the file path to transfer: ")
            relative_path = os.path.relpath(local_path, file_from)
            dropbox_path = os.path.join(file_to, relative_path)

            with open(local_path, 'rb') as f:
                dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.A9mScZ8O7Mo8Z8IVEujAgcYy5Y7WfTWuKNJT38TO6OVmk2Ovrrpw-QQ1VlQsWgLZ6QRgQAAgK0RTEuql83OjHEZVaTS0Skw6EWES7dG-jseuhBkU9Ax6b4ah9ZcXO8RRnSuw5wo'

    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer: ")
    file_to = input("Enter the full path to upload to the dropbox: ")

    transferData.upload_file(file_from, file_to)

    print("The file has been moved!")

if __name__ == "__main__":
    main()