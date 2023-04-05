#!/usr/bin/python3

""" Prime Game Algorithm Python """


def isWinner(x, nums):
    """
    The function determines the winner of a game between Maria and Ben based on a list of numbers and a set of prime
    numbers.

    :param x: The number of games played between Maria and Ben
    :param nums: The parameter `nums` is a list of integers representing the numbers in each game played between Maria and
    Ben
    :return: the name of the player who wins the game, either 'Maria' or 'Ben', or None if both players have the same number
    of wins.
    """
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = set()
        for i in range(2, n + 1):
            is_prime = True
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.add(i)

        current_player = 'Maria'
        while primes:
            can_remove = False
            for p in sorted(primes):
                if n % p == 0:
                    can_remove = True
                    primes.remove(p)
                    for i in range(p, n + 1, p):
                        if i in primes:
                            primes.remove(i)
                    break

            if not can_remove:
                if current_player == 'Maria':
                    ben_wins += 1
                else:
                    maria_wins += 1
                break

            if current_player == 'Maria':
                current_player = 'Ben'
            else:
                current_player = 'Maria'

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
