#/////////////////////////////////////

ticket_type_counter = 0
student_procent = 0
standard_procent = 0
kid_procent = 0
student_counter = 0
standard_counter = 0
kid_counter = 0
full_counter = 0
film_procent = 0

while True:
    film = input()
    if film == 'Finish':
        break
    free_seats = int(input())

    ticket_type_counter = 0
    while True:
        ticket_type = input()

        if ticket_type_counter >= free_seats:
            break
        elif ticket_type == 'End':
            break

        if ticket_type == "student":
            student_counter += 1
        elif ticket_type == "kid":
            kid_counter += 1
        elif ticket_type == "standard":
            standard_counter += 1

        ticket_type_counter += 1
        full_counter += 1

    film_procent = ticket_type_counter / free_seats * 100
    print(f"{film} - {film_procent:.2f}% full.")

student_procent = student_counter / full_counter * 100
standard_procent = standard_counter / full_counter * 100
kid_procent = kid_counter / full_counter * 100
print(f"Total tickets: {full_counter}")
print(f"{student_procent:.2f}% student tickets.")
print(f"{standard_procent:.2f}% standard tickets.")
print(f"{kid_procent:.2f}% kids tickets.")