while True:
    try:
        num=int(input("enter the number"))
        break
    except ValueError:
        print("Sorry not valid input")
    except KeyboardInterrupt:
        print("Sorry no input taken")
    except:
        print("Unknown error")
    finally:
        print("input attempted")


def myfuns():
    cookies=10
    people=0

    try:
        num_each = cookies // people
        leftovers = cookies % people
    except ZeroDivisionError:
        print("Oops, you entered 0 people will be attending.")
        print("Please enter a good number of people for a party.")


