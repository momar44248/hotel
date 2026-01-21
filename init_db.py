import csv
import os

def initialize_csv_files():
    files = {
        'staff_positions.csv': ['id', 'position_name'],
        'users.csv': ['id', 'username', 'password_hash', 'role'],
        'room_amenities.csv': ['room_id', 'amenity_id'],
        'bookings.csv': ['booking_id', 'user_id', 'room_id', 'check_in', 'check_out'],
        'payments.csv': ['payment_id', 'booking_id', 'amount', 'date', 'method'],
        'invoices.csv': ['invoice_id', 'booking_id', 'total_amount'],
        'rooms.csv': ['id', 'room_num', 'capacity', 'status', 'type_id', 'level_id'],
        'amenities.csv': ['id', 'name'],
        'hotels.csv': ['id', 'name', 'location'],
        'room_types.csv': ['id', 'type_name', 'price']
    }
    
    for filename, headers in files.items():
        if not os.path.exists(filename):
            with open(filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(headers)
            print(f"Fichier {filename} créé avec en-têtes.")
        else:
            print(f"Fichier {filename} existe déjà.")

if __name__ == '__main__':
    # Cela créera tous les fichiers listés ci-dessus avec leurs en-têtes
    initialize_csv_files()
