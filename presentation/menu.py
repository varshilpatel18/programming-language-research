"""
Programmer: Varshil Patel
File: menu.py
Description: Console interface for the project.
"""

from business import service
from model.record import Record
from persistence.repository import save_records


def show_menu() -> None:
    print("\n=========================================")
    print("CST8002 – Practical Project Part 02")
    print("Program by: VARSHIL PATEL")
    print("=========================================\n")
    print("1. Reload dataset")
    print("2. Display all records")
    print("3. Create new record")
    print("4. Edit a record")
    print("5. Delete a record")
    print("6. Save records to new CSV (UUID filename)")
    print("0. Exit\n")


def display_records() -> None:
    """Displays all records with index and your name printed regularly."""
    all_records = service.get_all_records()

    if not all_records:
        print("No records loaded. Try reloading the dataset.")
        return

    for i, r in enumerate(all_records):
        print(f"{i}: {r}")

        # Requirement: Your name appears frequently in output
        if i % 10 == 0:
            print("---- Program by: VARSHIL PATEL ----")


def create_record() -> None:
    """Prompts user to create a new Record."""
    print("Enter new record fields for a camera observation:")

    site_identification = input("Site identification (number): ").strip()
    camera_set_datetime = input("Camera set date-time (e.g. 09/05/2014 8:35): ").strip()
    camera_check_datetime = input("Camera check date-time: ").strip()
    lure_type = input("Lure type: ").strip()
    species_common_name = input("Species common name: ").strip()
    count_str = input("Count of individuals (number): ").strip()
    observation_datetime = input("Observation date-time: ").strip()

    # basic validation for count:
    try:
        count_of_individuals = int(count_str)
    except ValueError:
        print("Invalid count entered, defaulting to 0.")
        count_of_individuals = 0

    new_rec = Record(
        site_identification,
        camera_set_datetime,
        camera_check_datetime,
        lure_type,
        species_common_name,
        count_of_individuals,
        observation_datetime,
    )
    service.add_record(new_rec)
    print("Record added.")


def edit_record() -> None:
    """Prompts user to edit an existing record by index."""
    index_str = input("Enter index to edit: ").strip()

    if not index_str.isdigit():
        print("Invalid index (not a number).")
        return

    index = int(index_str)
    old = service.get_record(index)
    if old is None:
        print("Invalid index.")
        return

    print(f"Editing record: {old}")
    print("Press Enter to keep the existing value shown in [brackets].")

    site_identification_input = input(
        f"Site identification [{old.site_identification}]: "
    ).strip()
    site_identification = (
        site_identification_input if site_identification_input != "" else old.site_identification
    )

    camera_set_datetime = input(
        f"Camera set date-time [{old.camera_set_datetime}]: "
    ).strip() or old.camera_set_datetime

    camera_check_datetime = input(
        f"Camera check date-time [{old.camera_check_datetime}]: "
    ).strip() or old.camera_check_datetime

    lure_type = input(
        f"Lure type [{old.lure_type}]: "
    ).strip() or old.lure_type

    species_common_name = input(
        f"Species common name [{old.species_common_name}]: "
    ).strip() or old.species_common_name

    count_str = input(
        f"Count of individuals [{old.count_of_individuals}]: "
    ).strip()
    if count_str == "":
        count_of_individuals = old.count_of_individuals
    else:
        try:
            count_of_individuals = int(count_str)
        except ValueError:
            print("Invalid count; keeping old value.")
            count_of_individuals = old.count_of_individuals

    observation_datetime = input(
        f"Observation date-time [{old.observation_datetime}]: "
    ).strip() or old.observation_datetime

    updated = Record(
        site_identification,
        camera_set_datetime,
        camera_check_datetime,
        lure_type,
        species_common_name,
        count_of_individuals,
        observation_datetime,
    )
    service.update_record(index, updated)
    print("Record updated.")


def delete_record_ui() -> None:
    """Prompts user to delete a record by index."""
    index_str = input("Enter index to delete: ").strip()

    if not index_str.isdigit():
        print("Invalid index (not a number).")
        return

    index = int(index_str)
    if service.delete_record(index):
        print("Record deleted.")
    else:
        print("Invalid index.")


def run() -> None:
    """Main loop for the menu-driven application."""
    service.reload_data()

    while True:
        show_menu()
        choice = input("Choice: ").strip()

        if choice == "1":
            service.reload_data()
            print("Dataset reloaded.")

        elif choice == "2":
            display_records()

        elif choice == "3":
            create_record()

        elif choice == "4":
            edit_record()

        elif choice == "5":
            delete_record_ui()

        elif choice == "6":
            path = save_records(service.get_all_records())
            print(f"Saved to file: {path}")

        elif choice == "0":
            print("Goodbye! Program by: VARSHIL PATEL")
            break

        else:
            print("Invalid choice.")
