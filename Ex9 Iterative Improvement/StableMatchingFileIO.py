#The input for the program is read from input.txt file .
#The input is the preference lists under sub-division 4 of the question.

# Required Data Structures
men = dict()  # Holds preference list of Men
women = dict()  # Holds preference list of Women
men_pairs = dict()  # Holds the pairing with respect to each Man
women_pairs = dict()  # Holds the pairing with respect to each Woman
preferences = dict()  # Holds the preference dictionary of each Woman
proposal_tries = dict()  # Holds the no. of proposals a Man m has made


def proposal(m):  # Man m proposes a Woman w according to the preference list

    i = proposal_tries[m]
    w_pref = men[m][i]
    men_pairs[m] = w_pref
    return w_pref


def undo_proposal(m):  # Man m retracts his current proposal

    men_pairs[m] = 'nil'


def accept_proposal(m, w):  # Woman w accepts the proposal of Man m

    women_pairs[w] = m


def reject_proposal(w):  # Woman w rejects her current proposal

    men_pairs[women_pairs[w]] = 'nil'
    women_pairs[w] = 'nil'


def woman_is_unmatched(w):  # Find if Woman w is unmatched

    if women_pairs[w] == 'nil':
        return True
    else:
        return False


def is_unstable(m, w):  # Find if the current pairing of Woman w is unstable compared to Man m

    m_old = women_pairs[w]

    if(preferences[w][m_old] > preferences[w][m]):
        return True
    else:
        return False


def unmatched_male():  # Find an unmatched Man m if he exists

    for m in men_pairs:
        if men_pairs[m] == 'nil':
            return m

    return 'nil'


def print_current_iteration(i):  # Print the current pairings

    print("Iteration", i, ":", end=' ')

    for m in men:
        if(men_pairs[m] != 'nil'):
            print(m, '-', men_pairs[m], end=' ')

    print('\n')


def gayle_shapley_stable_matching():  # Perform the Gayle-Shapley Stable Matching Algorithm

    i = 1

    while unmatched_male() != 'nil':
        m = unmatched_male()
        w = proposal(m)

        if woman_is_unmatched(w):
            accept_proposal(m, w)

        else:
            if is_unstable(m, w) == True:
                reject_proposal(w)
                accept_proposal(m, w)

            else:
                undo_proposal(m)

        proposal_tries[m] += 1
        print_current_iteration(i)
        i += 1


def get_input():  # Get the preference lists of Men & Women

    file = open('input.txt', 'r')
    

    while True:  # Filling up the men dictionaries
        line = file.readline()

        if(line.strip() != ''):
            line = line.split()
            men[line[0]] = line[1:]
            men_pairs[line[0]] = 'nil'
            # Keeps count of the no. of Women a Man m has proposed to
            proposal_tries[line[0]] = 0

        else:
            break

    while True:
        line = file.readline()

        if(line.strip() != ''):
            line = line.split()
            women[line[0]] = line[1:]
            women_pairs[line[0]] = 'nil'

            pref = 1
            pref_dict_w = dict()  # Preference dictionary of a Woman w to each Man m

            # Higher the pref number assigned, lower the preference of Man m to Woman w
            for m in women[line[0]]:
                pref_dict_w[m] = pref
                pref += 1

            preferences[line[0]] = pref_dict_w

        else:
            break
    
    file.close()


if __name__ == '__main__':

    get_input()
    print('\n\n\t\tImplementing the Gayle-Shapley Stable Matching Algorithm\n')
    gayle_shapley_stable_matching()
    


"""
OUTPUT:

vishakan@Legion:~/Desktop/Design-and-Analysis-of-Algorithms/Ex9 Iterative Improvement$ python StableMatchingFileIO.py


		Implementing the Gayle-Shapley Stable Matching Algorithm

Iteration 1 : a - u 

Iteration 2 : a - u b - r 

Iteration 3 : a - u b - r c - t 

Iteration 4 : b - r c - t d - u 

Iteration 5 : a - r c - t d - u 

Iteration 6 : a - r c - t d - u 

Iteration 7 : a - r b - u c - t 

Iteration 8 : a - r b - u c - t 

Iteration 9 : a - r b - u c - t 

Iteration 10 : a - r b - u c - t d - s 

"""

